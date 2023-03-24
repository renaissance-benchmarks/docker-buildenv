
FROM fedora:34
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://download.java.net/java/GA/jdk20/bdc68b4b9cbc4ebcb30745c85038d91d/36/GPL/openjdk-20_linux-x64_bin.tar.gz" -o "/tmp/jdk-20.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-20.tar.gz" \
    && rm -f "/tmp/jdk-20.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-20/bin/java 10 \
    && for i in /opt/jdk-20/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-20/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-20/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-20/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-20/lib/security/ \
    && /opt/jdk-20/bin/java -version


CMD ["/bin/bash"]

