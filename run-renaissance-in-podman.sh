#!/bin/bash

set -ueo pipefail

source ./version.rc

indent() {
    sed 's#.*#      &#'
}

get_image_ids_and_labels() {
    podman image ls \
        --format '{{ .ID }} {{ .Repository }}:{{ .Tag }}' \
        "${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_VERSION_TAG}-*" "$@"
}

images_filter="${images:-.}"
jvm_args="${jvm_args:-}"
renaissance_jar="${1:-}"
shift

    if ! [ -f "$renaissance_jar" ]; then
    echo "Unable to find Renaissance JAR '$renaissance_jar'. Terminating." >&2
    exit 1
fi

if [ "$#" -eq 0 ]; then
    set -- -r 1 -c test all
fi

get_image_ids_and_labels | grep -e "$images_filter" | (
    failed_images=""
    counter=0
    while read image_id image_label; do
        echo ">>> $image_label ($image_id)"

        echo "  -> java $jvm_args -jar renaissance.jar $*"
        if podman run --rm --volume "$renaissance_jar:/renaissance.jar:ro" "$image_id" \
            /bin/bash -c "java $jvm_args -jar /renaissance.jar $*" 2>&1 | indent; then
            echo " -> $image_label ($image_id) looks okay."
        else
            echo " !!"
            echo " !! Failed Renaissance run on $image_label ($image_id), see above."
            echo " !!"
            echo " !!"
            failed_images="$failed_images $image_label"
        fi
        counter=$(( counter + 1 ))
    done

    echo ">>> Finished testing $counter images matching ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_VERSION_TAG}-* ..."
    if [ -z "$failed_images" ]; then
        echo " -> Everything looks good."
    else
        echo " -> Issues found with following images:$failed_images."
    fi

    if [ -n "$failed_images" ]; then
        exit 2
    fi
)
