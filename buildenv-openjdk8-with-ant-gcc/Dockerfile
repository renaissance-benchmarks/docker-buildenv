
FROM fedora:40
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v8-openjdk8-with-ant-gcc
LABEL vendor=renaissance.dev

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip gcc bzip2 which jq \
    && dnf -y --setopt install_weak_deps=false --repo fedora --repo updates update

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install java-1.8.0-openjdk-devel \
    && rm -rf /var/log/* /var/lib/dnf/* /var/cache/dnf/* \
    && rpm --rebuilddb \
    && curl https://downloads.apache.org/ant/binaries/apache-ant-1.10.14-bin.tar.bz2 \
    | tar xjf - --strip-components=1 --one-top-level=/opt/ant \
    && ln -s /opt/ant/bin/ant /usr/local/bin/ant

CMD ["/bin/bash"]
