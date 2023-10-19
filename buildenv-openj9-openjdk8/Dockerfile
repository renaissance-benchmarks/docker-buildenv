
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://github.com/ibmruntimes/semeru8-binaries/releases/download/jdk8u382-b05_openj9-0.40.0/ibm-semeru-open-jdk_x64_linux_8u382b05_openj9-0.40.0.tar.gz" -o "/tmp/jdk8u382-b05.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk8u382-b05.tar.gz" \
    && rm -f "/tmp/jdk8u382-b05.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk8u382-b05/bin/java 10 \
    && for i in /opt/jdk8u382-b05/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk8u382-b05/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk8u382-b05/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk8u382-b05/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk8u382-b05/lib/security/ \
    && /opt/jdk8u382-b05/bin/java -version


CMD ["/bin/bash"]

