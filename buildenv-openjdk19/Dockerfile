
FROM fedora:39
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v8-openjdk19
LABEL vendor=renaissance.dev

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && rm -rf /var/log/* /var/lib/dnf/* /var/cache/dnf/* \
    && rpm --rebuilddb

RUN curl -L "https://download.java.net/java/GA/jdk19.0.2/fdb695a9d9064ad6b064dc6df578380c/7/GPL/openjdk-19.0.2_linux-x64_bin.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-19.0.2/bin/java 10 \
    && for i in /opt/jdk-19.0.2/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-19.0.2/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-19.0.2/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-19.0.2/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-19.0.2/lib/security/ \
    && /opt/jdk-19.0.2/bin/java -version

CMD ["/bin/bash"]
