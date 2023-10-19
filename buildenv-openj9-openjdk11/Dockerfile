
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://github.com/ibmruntimes/semeru11-binaries/releases/download/jdk-11.0.20.1%2B1_openj9-0.40.0/ibm-semeru-open-jdk_x64_linux_11.0.20.1_1_openj9-0.40.0.tar.gz" -o "/tmp/jdk-11.0.20.1+1.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-11.0.20.1+1.tar.gz" \
    && rm -f "/tmp/jdk-11.0.20.1+1.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-11.0.20.1+1/bin/java 10 \
    && for i in /opt/jdk-11.0.20.1+1/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-11.0.20.1+1/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-11.0.20.1+1/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-11.0.20.1+1/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-11.0.20.1+1/lib/security/ \
    && /opt/jdk-11.0.20.1+1/bin/java -version


CMD ["/bin/bash"]

