
# WARNING: generated file, use update.py for updates

FROM fedora:41
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v13-openjdk11
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk11)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && dnf -y --setopt install_weak_deps=false --repo fedora --repo updates update

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install java-11-openjdk-devel \
    && dnf clean all && rm -rf /var/log/*

CMD ["/bin/bash"]
