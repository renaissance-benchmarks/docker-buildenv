
FROM fedora:39
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v9-openj9-openjdk11
LABEL vendor=renaissance.dev

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip \
    && rm -rf /var/log/* /var/lib/dnf/* /var/cache/dnf/* \
    && rpm --rebuilddb

RUN curl -L "https://github.com/ibmruntimes/semeru11-binaries/releases/download/jdk-11.0.22%2B7_openj9-0.43.0/ibm-semeru-open-jdk_x64_linux_11.0.22_7_openj9-0.43.0.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-11.0.22+7/bin/java 10 \
    && for i in /opt/jdk-11.0.22+7/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-11.0.22+7/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-11.0.22+7/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-11.0.22+7/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-11.0.22+7/lib/security/ \
    && /opt/jdk-11.0.22+7/bin/java -version

CMD ["/bin/bash"]
