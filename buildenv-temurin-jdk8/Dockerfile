
# WARNING: generated file, use update.py for updates

FROM fedora:42
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v19-temurin-jdk8
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant temurin-jdk8)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && dnf clean all && rm -rf /var/log/*

RUN curl -L "https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u482-b08/OpenJDK8U-jdk_x64_linux_hotspot_8u482b08.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk8u482-b08/bin/java 10 \
    && for i in /opt/jdk8u482-b08/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk8u482-b08/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk8u482-b08/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk8u482-b08/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk8u482-b08/lib/security/ \
    && /opt/jdk8u482-b08/bin/java -version

CMD ["/bin/bash"]
