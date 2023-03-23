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
    echo "To push everything, following command could be useful."
    echo
    sed -n 's#.*\(podman push .*\)#\1#p' "$my_temp/report.txt" | paste '-sd#' | sed 's:#: \&\& :g' 2>/dev/null
    echo
    rm -rf "$my_temp"
}

trap on_exit INT QUIT TERM EXIT

echo "To push any of the built images, following commands may be used." >"$my_temp/report.txt"
echo >>"$my_temp/report.txt"

. ./version.rc

for i in "$@"; do
    if echo "$i" | grep -q '^buildenv-'; then
        version="$( echo "$i" | cut '-d-' -f 2- | cut '-d/' -f 1)"
    else
        version="$i"
    fi
    dockerfile="buildenv-$version/Dockerfile"

    banner "Will build $DOCKER_IMAGE_VERSION_TAG-$version from $dockerfile."

    buildah bud --iidfile "$my_temp/id-$version.txt" "$dockerfile"
    echo "$version ==> podman push $( cut -d: -f 2 "$my_temp/id-$version.txt" ) docker://docker.io/renaissancebench/buildenv:$DOCKER_IMAGE_VERSION_TAG-$version" >>"$my_temp/report.txt"
done
