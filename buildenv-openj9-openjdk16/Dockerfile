
FROM fedora:35
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://github.com/AdoptOpenJDK/openjdk16-binaries/releases/download/jdk-16.0.1%2B9_openj9-0.26.0/OpenJDK16U-jdk_x64_linux_openj9_16.0.1_9_openj9-0.26.0.tar.gz" -o "/tmp/jdk-16.0.1+9.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-16.0.1+9.tar.gz" \
    && rm -f "/tmp/jdk-16.0.1+9.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-16.0.1+9/bin/java 10 \
    && for i in /opt/jdk-16.0.1+9/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-16.0.1+9/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-16.0.1+9/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-16.0.1+9/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-16.0.1+9/lib/security/ \
    && /opt/jdk-16.0.1+9/bin/java -version


CMD ["/bin/bash"]

