
# WARNING: generated file, use update.py for updates

FROM fedora:42
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v16-openj9-openjdk21
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openj9-openjdk21)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && dnf clean all && rm -rf /var/log/*

RUN curl -L "https://github.com/ibmruntimes/semeru21-binaries/releases/download/jdk-21.0.7%2B6_openj9-0.51.0/ibm-semeru-open-jdk_x64_linux_21.0.7_6_openj9-0.51.0.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-21.0.7+6/bin/java 10 \
    && for i in /opt/jdk-21.0.7+6/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-21.0.7+6/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-21.0.7+6/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-21.0.7+6/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-21.0.7+6/lib/security/ \
    && /opt/jdk-21.0.7+6/bin/java -version

CMD ["/bin/bash"]
