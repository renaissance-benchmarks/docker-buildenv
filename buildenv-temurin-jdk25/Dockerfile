
# WARNING: generated file, use update.py for updates

FROM fedora:42
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v18-temurin-jdk25
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant temurin-jdk25)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && dnf clean all && rm -rf /var/log/*

RUN curl -L "https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25.0.2%2B10/OpenJDK25U-jdk_x64_linux_hotspot_25.0.2_10.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-25.0.2+10/bin/java 10 \
    && for i in /opt/jdk-25.0.2+10/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-25.0.2+10/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-25.0.2+10/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-25.0.2+10/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-25.0.2+10/lib/security/ \
    && /opt/jdk-25.0.2+10/bin/java -version

CMD ["/bin/bash"]
