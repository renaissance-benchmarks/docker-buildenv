
# WARNING: generated file, use update.py for updates

FROM fedora:40
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v12-openjdk23
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk23)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && dnf clean all && rm -rf /var/log/*

RUN curl -L "https://download.java.net/java/GA/jdk23/3c5b90190c68498b986a97f276efd28a/37/GPL/openjdk-23_linux-x64_bin.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-23/bin/java 10 \
    && for i in /opt/jdk-23/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-23/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-23/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-23/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-23/lib/security/ \
    && /opt/jdk-23/bin/java -version

CMD ["/bin/bash"]
