
# WARNING: generated file, use update.py for updates

FROM fedora:39
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v9-openjdk9
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk9)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && rm -rf /var/log/* /var/lib/dnf/* /var/cache/dnf/* \
    && rpm --rebuilddb

RUN curl -L "https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_linux-x64_bin.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-9.0.4/bin/java 10 \
    && for i in /opt/jdk-9.0.4/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-9.0.4/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-9.0.4/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-9.0.4/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-9.0.4/lib/security/ \
    && /opt/jdk-9.0.4/bin/java -version

CMD ["/bin/bash"]
