
# WARNING: generated file, use update.py for updates

FROM fedora:39
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v10-openj9-openjdk17
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openj9-openjdk17)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && rm -rf /var/log/* /var/lib/dnf/* /var/cache/dnf/* \
    && rpm --rebuilddb

RUN curl -L "https://github.com/ibmruntimes/semeru17-binaries/releases/download/jdk-17.0.9%2B9_openj9-0.41.0/ibm-semeru-open-jdk_x64_linux_17.0.9_9_openj9-0.41.0.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-17.0.9+9/bin/java 10 \
    && for i in /opt/jdk-17.0.9+9/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-17.0.9+9/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-17.0.9+9/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-17.0.9+9/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-17.0.9+9/lib/security/ \
    && /opt/jdk-17.0.9+9/bin/java -version

CMD ["/bin/bash"]
