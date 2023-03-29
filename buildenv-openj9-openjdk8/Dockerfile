
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u292-b10_openj9-0.26.0/OpenJDK8U-jdk_x64_linux_openj9_8u292b10_openj9-0.26.0.tar.gz" -o "/tmp/jdk8u292-b10.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk8u292-b10.tar.gz" \
    && rm -f "/tmp/jdk8u292-b10.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk8u292-b10/bin/java 10 \
    && for i in /opt/jdk8u292-b10/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk8u292-b10/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk8u292-b10/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk8u292-b10/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk8u292-b10/lib/security/ \
    && /opt/jdk8u292-b10/bin/java -version


CMD ["/bin/bash"]

