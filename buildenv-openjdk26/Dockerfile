
# WARNING: generated file, use update.py for updates

FROM fedora:42
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v19-openjdk26
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk26)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && dnf clean all && rm -rf /var/log/*

RUN curl -L "https://download.java.net/java/GA/jdk26/c3cc523845074aa0af4f5e1e1ed4151d/35/GPL/openjdk-26_linux-x64_bin.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-26/bin/java 10 \
    && for i in /opt/jdk-26/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-26/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-26/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-26/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-26/lib/security/ \
    && /opt/jdk-26/bin/java -version

CMD ["/bin/bash"]
