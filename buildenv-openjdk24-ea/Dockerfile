
# WARNING: generated file, use update.py for updates

FROM fedora:40
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v12-openjdk24-ea
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk24-ea)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && dnf clean all && rm -rf /var/log/*

RUN curl -L "https://download.java.net/java/early_access/jdk24/16/GPL/openjdk-24-ea+16_linux-x64_bin.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-24/bin/java 10 \
    && for i in /opt/jdk-24/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-24/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-24/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-24/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-24/lib/security/ \
    && /opt/jdk-24/bin/java -version

CMD ["/bin/bash"]
