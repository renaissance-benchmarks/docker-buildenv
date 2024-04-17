#!/bin/sh

set -ue

banner() {
    (
        echo "##"
        echo "## $( date '+%Y-%m-%d %H:%M:%S |' )" "$@"
        echo "##"
    ) >&2
}


my_temp="$( mktemp -d )"

on_exit() {
    echo
    cat "$my_temp/report.txt" 2>/dev/null
    echo
    echo "To push everything, the following command could be useful."
    echo
    sed -n 's#.*\(podman push .*\)#\1#p' "$my_temp/report.txt" | paste '-sd#' | sed 's:#: \&\& :g' 2>/dev/null
    echo
    if ! $exit_okay; then
        echo
        echo Something went wrong during image generation.
        echo Consult the logs above for details.
        echo
    fi
    rm -rf "$my_temp"
}

exit_okay=false
trap on_exit INT QUIT TERM EXIT

echo "To push any of the built images, following commands may be used." >"$my_temp/report.txt"
echo >>"$my_temp/report.txt"

source ./version.rc

for i in "$@"; do
    if echo "$i" | grep -q '^buildenv-'; then
        version="$( echo "$i" | cut '-d-' -f 2- | cut '-d/' -f 1)"
    else
        version="$i"
    fi
    dockerfile="buildenv-$version/Dockerfile"
    image_tag="${DOCKER_IMAGE_VERSION_TAG}-${version}"
    image_name="${DOCKER_REGISTRY}/${DOCKER_REGISTRY_NAMESPACE}/${DOCKER_IMAGE_NAME}:$image_tag"

    banner "Will build $image_tag from $dockerfile."

    buildah bud --iidfile "$my_temp/id-$version.txt" -t "$image_name" "$dockerfile"
    image_hash="$( cut -d: -f 2 "$my_temp/id-$version.txt" )"
    echo "$version ==> podman push $image_hash docker://$image_name" >>"$my_temp/report.txt"
done

exit_okay=true
