#!/bin/bash

set -ueo pipefail

indent() {
    sed 's#.*#    &#'
}

podman image ls --format '{{ .ID }} {{ .Repository }}:{{ .Tag }}' "$@" | while read image_id image_label; do
    echo "$image_label [$image_id]"
    podman run --rm "$image_id" /bin/bash -c "java -version" 2>&1 | indent || true
done
