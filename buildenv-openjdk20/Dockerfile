
# WARNING: generated file, use update.py for updates

FROM fedora:39
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v10-openjdk20
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk20)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && rm -rf /var/log/* /var/lib/dnf/* /var/cache/dnf/* \
    && rpm --rebuilddb

RUN curl -L "https://download.java.net/java/GA/jdk20.0.2/6e380f22cbe7469fa75fb448bd903d8e/9/GPL/openjdk-20.0.2_linux-x64_bin.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-20.0.2/bin/java 10 \
    && for i in /opt/jdk-20.0.2/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-20.0.2/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-20.0.2/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-20.0.2/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-20.0.2/lib/security/ \
    && /opt/jdk-20.0.2/bin/java -version

CMD ["/bin/bash"]
