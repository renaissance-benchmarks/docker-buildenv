
FROM fedora:35
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf install -y java-1.8.0-openjdk-devel \
    && dnf clean all


CMD ["/bin/bash"]

