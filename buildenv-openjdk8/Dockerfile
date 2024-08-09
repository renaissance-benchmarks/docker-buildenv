
# WARNING: generated file, use update.py for updates

FROM fedora:39
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v9-openjdk8
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk8)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && dnf -y --setopt install_weak_deps=false --repo fedora --repo updates update

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install java-1.8.0-openjdk-devel \
    && rm -rf /var/log/* /var/lib/dnf/* /var/cache/dnf/* \
    && rpm --rebuilddb

CMD ["/bin/bash"]
