#!/bin/bash

set -ueo pipefail

source ./version.rc

podman image ls \
	--format "podman push {{ .ID }} docker://${DOCKER_REGISTRY}/${DOCKER_REGISTRY_NAMESPACE}/${DOCKER_IMAGE_NAME}:{{ .Tag }}" \
	"${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_VERSION_TAG}-*"
