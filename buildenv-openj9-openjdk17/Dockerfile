
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://github.com/ibmruntimes/semeru17-binaries/releases/download/jdk-17.0.8.1%2B1_openj9-0.40.0/ibm-semeru-open-jdk_x64_linux_17.0.8.1_1_openj9-0.40.0.tar.gz" -o "/tmp/jdk-17.0.8.1+1.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-17.0.8.1+1.tar.gz" \
    && rm -f "/tmp/jdk-17.0.8.1+1.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-17.0.8.1+1/bin/java 10 \
    && for i in /opt/jdk-17.0.8.1+1/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-17.0.8.1+1/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-17.0.8.1+1/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-17.0.8.1+1/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-17.0.8.1+1/lib/security/ \
    && /opt/jdk-17.0.8.1+1/bin/java -version


CMD ["/bin/bash"]

