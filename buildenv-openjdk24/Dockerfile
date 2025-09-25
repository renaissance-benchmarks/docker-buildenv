
# WARNING: generated file, use update.py for updates

FROM fedora:42
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v17-openjdk24
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk24)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && dnf clean all && rm -rf /var/log/*

RUN curl -L "https://download.java.net/java/GA/jdk24.0.2/fdc5d0102fe0414db21410ad5834341f/12/GPL/openjdk-24.0.2_linux-x64_bin.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-24.0.2/bin/java 10 \
    && for i in /opt/jdk-24.0.2/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-24.0.2/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-24.0.2/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-24.0.2/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-24.0.2/lib/security/ \
    && /opt/jdk-24.0.2/bin/java -version

CMD ["/bin/bash"]
