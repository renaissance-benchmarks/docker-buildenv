
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf install -y java-11-openjdk-devel \
    && dnf clean all


CMD ["/bin/bash"]

