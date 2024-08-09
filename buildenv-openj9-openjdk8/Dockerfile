
FROM fedora:40
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v8-openj9-openjdk8
LABEL vendor=renaissance.dev

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && rm -rf /var/log/* /var/lib/dnf/* /var/cache/dnf/* \
    && rpm --rebuilddb

RUN curl -L "https://github.com/ibmruntimes/semeru8-binaries/releases/download/jdk8u402-b06_openj9-0.43.0/ibm-semeru-open-jdk_x64_linux_8u402b06_openj9-0.43.0.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk8u402-b06/bin/java 10 \
    && for i in /opt/jdk8u402-b06/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk8u402-b06/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk8u402-b06/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk8u402-b06/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk8u402-b06/lib/security/ \
    && /opt/jdk8u402-b06/bin/java -version

CMD ["/bin/bash"]
