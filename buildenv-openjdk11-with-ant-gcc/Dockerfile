
# WARNING: generated file, use update.py for updates

FROM fedora:40
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v12-openjdk11-with-ant-gcc
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk11-with-ant-gcc)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip gcc bzip2 which jq \
    && dnf -y --setopt install_weak_deps=false --repo fedora --repo updates update

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install java-11-openjdk-devel \
    && dnf clean all && rm -rf /var/log/* \
    && curl https://downloads.apache.org/ant/binaries/apache-ant-1.10.14-bin.tar.bz2 -o /tmp/apache-ant-1.10.14-bin.tar.bz2 \
    && tar -xjf /tmp/apache-ant-1.10.14-bin.tar.bz2 -C /opt \
    && rm -f /tmp/apache-ant-1.10.14-bin.tar.bz2 \
    && ln -s /opt/apache-ant-1.10.14/bin/ant /usr/local/bin/ant

CMD ["/bin/bash"]
