
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://github.com/AdoptOpenJDK/openjdk17-binaries/releases/download/jdk-2021-05-07-13-31/OpenJDK-jdk_x64_linux_openj9_2021-05-06-23-30.tar.gz" -o "/tmp/jdk-17+18.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-17+18.tar.gz" \
    && rm -f "/tmp/jdk-17+18.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-17+18/bin/java 10 \
    && for i in /opt/jdk-17+18/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-17+18/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-17+18/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-17+18/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-17+18/lib/security/ \
    && /opt/jdk-17+18/bin/java -version


CMD ["/bin/bash"]

