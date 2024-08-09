
# WARNING: generated file, use update.py for updates

FROM fedora:39
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v9-openjdk12
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk12)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && rm -rf /var/log/* /var/lib/dnf/* /var/cache/dnf/* \
    && rpm --rebuilddb

RUN curl -L "https://download.java.net/java/GA/jdk12.0.2/e482c34c86bd4bf8b56c0b35558996b9/10/GPL/openjdk-12.0.2_linux-x64_bin.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-12.0.2/bin/java 10 \
    && for i in /opt/jdk-12.0.2/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-12.0.2/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-12.0.2/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-12.0.2/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-12.0.2/lib/security/ \
    && /opt/jdk-12.0.2/bin/java -version

CMD ["/bin/bash"]
