#!/usr/bin/env python3

import os
import re
import sys

VERSIONS = [
    {
        "name": "openjdk8",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/openjdk/jdk8u44/ri/openjdk-8u44-linux-x64.tar.gz",
        "basedir": "java-se-8u44-ri",
    },
    {
        "name": "openjdk8-with-ant-gcc",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/openjdk/jdk8u44/ri/openjdk-8u44-linux-x64.tar.gz",
        "basedir": "java-se-8u44-ri",
        "extra_packages": [
            "gcc",
            "bzip2",
            "which",
            "jq",
        ],
        "commands": [
            "curl https://downloads.apache.org/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.bz2 -o /tmp/apache-ant-${ANT_VERSION}-bin.tar.bz2",
            "tar -xjf /tmp/apache-ant-${ANT_VERSION}-bin.tar.bz2 -C /opt",
            "rm -f /tmp/apache-ant-${ANT_VERSION}-bin.tar.bz2",
            "ln -s /opt/apache-ant-${ANT_VERSION}/bin/ant /usr/local/bin/ant",
        ],
        "command_vars": {
            "ANT_VERSION": "1.10.14",
        },
        "dependabot_checks": True,
    },
    {
        "name": "openjdk9",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_linux-x64_bin.tar.gz",
        "basedir": "jdk-9.0.4",
    },
    {
        "name": "openjdk10",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk10/10.0.2/19aef61b38124481863b1413dce1855f/13/openjdk-10.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-10.0.2",
    },
    {
        "name": "openjdk11",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/openjdk/jdk11.0.0.2/ri/openjdk-11.0.0.2_linux-x64.tar.gz",
        "basedir": "jdk-11.0.0.2",
    },
    {
        "name": "openjdk11-with-ant-gcc",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/openjdk/jdk11.0.0.2/ri/openjdk-11.0.0.2_linux-x64.tar.gz",
        "basedir": "jdk-11.0.0.2",
        "extra_packages": [
            "gcc",
            "bzip2",
            "which",
            "jq",
        ],
        "commands": [
            "curl https://downloads.apache.org/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.bz2 -o /tmp/apache-ant-${ANT_VERSION}-bin.tar.bz2",
            "tar -xjf /tmp/apache-ant-${ANT_VERSION}-bin.tar.bz2 -C /opt",
            "rm -f /tmp/apache-ant-${ANT_VERSION}-bin.tar.bz2",
            "ln -s /opt/apache-ant-${ANT_VERSION}/bin/ant /usr/local/bin/ant",
        ],
        "command_vars": {
            "ANT_VERSION": "1.10.14",
        },
    },
    {
        "name": "openjdk12",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk12.0.2/e482c34c86bd4bf8b56c0b35558996b9/10/GPL/openjdk-12.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-12.0.2",
    },
    {
        "name": "openjdk13",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk13.0.2/d4173c853231432d94f001e99d882ca7/8/GPL/openjdk-13.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-13.0.2",
    },
    {
        "name": "openjdk14",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk14.0.2/205943a0976c4ed48cb16f1043c5c647/12/GPL/openjdk-14.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-14.0.2",
    },
    {
        "name": "openjdk15",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-15.0.2",
    },
    {
        "name": "openjdk16",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk16.0.2/d4a915d82b4c4fbb9bde534da945d746/7/GPL/openjdk-16.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-16.0.2",
    },
    {
        "name": "openjdk17",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "package": "java-17-openjdk-devel",
    },
    {
        "name": "openjdk18",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk18.0.2/f6ad4b4450fd4d298113270ec84f30ee/9/GPL/openjdk-18.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-18.0.2",
    },
    {
        "name": "openjdk19",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk19.0.2/fdb695a9d9064ad6b064dc6df578380c/7/GPL/openjdk-19.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-19.0.2",
    },
    {
        "name": "openjdk20",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk20.0.2/6e380f22cbe7469fa75fb448bd903d8e/9/GPL/openjdk-20.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-20.0.2",
    },
    {
        "name": "openjdk21",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "package": "java-21-openjdk-devel",
    },
    {
        "name": "openjdk22",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk22.0.2/c9ecb94cd31b495da20a27d4581645e8/9/GPL/openjdk-22.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-22.0.2",
    },
    {
        "name": "openjdk23",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk23.0.2/6da2a6609d6e406f85c491fcb119101b/7/GPL/openjdk-23.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-23.0.2",
    },
    {
        "name": "openjdk24",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk24/1f9ff9062db4449d8ca828c504ffae90/36/GPL/openjdk-24_linux-x64_bin.tar.gz",
        "basedir": "jdk-24",
    },
    {
        "name": "openjdk25-ea",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/early_access/jdk25/16/GPL/openjdk-25-ea+16_linux-x64_bin.tar.gz",
        "basedir": "jdk-25",
    },
    {
        "name": "openj9-openjdk8",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://github.com/ibmruntimes/semeru8-binaries/releases/download/jdk8u452-b09_openj9-0.51.0/ibm-semeru-open-jdk_x64_linux_8u452b09_openj9-0.51.0.tar.gz",
        "basedir": "jdk8u452-b09",
    },
    {
        "name": "openj9-openjdk11",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://github.com/ibmruntimes/semeru11-binaries/releases/download/jdk-11.0.27%2B6_openj9-0.51.0/ibm-semeru-open-jdk_x64_linux_11.0.27_6_openj9-0.51.0.tar.gz",
        "basedir": "jdk-11.0.27+6",
    },
    {
        "name": "openj9-openjdk17",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://github.com/ibmruntimes/semeru17-binaries/releases/download/jdk-17.0.15%2B6_openj9-0.51.0/ibm-semeru-open-jdk_x64_linux_17.0.15_6_openj9-0.51.0.tar.gz",
        "basedir": "jdk-17.0.15+6",
    },
    {
        "name": "openj9-openjdk21",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://github.com/ibmruntimes/semeru21-binaries/releases/download/jdk-21.0.7%2B6_openj9-0.51.0/ibm-semeru-open-jdk_x64_linux_21.0.7_6_openj9-0.51.0.tar.gz",
        "basedir": "jdk-21.0.7+6",
    },
]

COMMON_PACKAGES = [
    "ca-certificates",
    "git",
    "unzip",
]

DOCKER_CONFIG = "version.rc"

DOCKERFILE_COMMON = {
    # Do not use:
    #   rm -rf /var/lib/dnf/* /var/cache/dnf/* && rpm --rebuilddb
    # as it fails on overlayfs due to unhandled rename exception:
    #   https://github.com/rpm-software-management/rpm/issues/2355
    'final_cleanup_commands': 'dnf clean all && rm -rf /var/log/*',
}

DOCKERFILE_TEMPLATE_FROM_PACKAGE = '''
# WARNING: generated file, use update.py for updates

FROM {base_image}
LABEL org.opencontainers.image.authors="{maintainer_email}"
LABEL maintainer="{maintainer_email}"
LABEL name={image_name}
LABEL version={image_version}-{image_variant}
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant {image_variant})"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install {install_packages} \\
    && dnf -y --setopt install_weak_deps=false --repo fedora --repo updates update

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install {package} \\
    && {common[final_cleanup_commands]}{extra_commands}

CMD ["/bin/bash"]
'''

# The following is not needed because we install Java via alternatives:
# printf 'export JAVA_HOME="%s"\\nexport PATH="$JAVA_HOME/bin:$PATH"\\n' "/opt/{tarball_basedir}" >/etc/profile.d/java_from_opt.sh \\

DOCKERFILE_TEMPLATE_FROM_TARBALL = '''
# WARNING: generated file, use update.py for updates

FROM {base_image}
LABEL org.opencontainers.image.authors="{maintainer_email}"
LABEL maintainer="{maintainer_email}"
LABEL name={image_name}
LABEL version={image_version}-{image_variant}
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant {image_variant})"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install {install_packages} \\
    && {common[final_cleanup_commands]}

RUN curl -L "{tarball_url}" | tar -xz -C /opt \\
    && alternatives --install /usr/bin/java java /opt/{tarball_basedir}/bin/java 10 \\
    && for i in /opt/{tarball_basedir}/bin/*; do \\
        ii="$( basename "$i" )"; \\
        [ "$ii" != "java" ] \\
            && alternatives --add-slave java "/opt/{tarball_basedir}/bin/java" "/usr/bin/$ii" "$ii" "/opt/{tarball_basedir}/bin/$ii"; \\
    done \\
    && mkdir -p /opt/{tarball_basedir}/lib/security/ \\
    && ln -sf /etc/pki/java/cacerts /opt/{tarball_basedir}/lib/security/ \\
    && /opt/{tarball_basedir}/bin/java -version{extra_commands}

CMD ["/bin/bash"]
'''

GITHUB_WORKFLOW_FILENAME = '.github/workflows/docker.yml'
GITHUB_WORKFLOW_HEADER = '''
name: Docker images

# WARNING: generated file, use update.py for updates

on: [push, pull_request]

jobs:
'''
GITHUB_WORKFLOW_TEMPLATE = '''
  image-{name}:
    permissions:
      contents: read
      packages: write
      id-token: write
    uses: ./.github/workflows/lib-build-image.yml
    with:
      name: {name}
      push: ${{{{ ((github.event_name == 'push') && contains(github.ref, '/tags/v')) }}}}

'''

GITHUB_DEPENDABOT_FILENAME = '.github/dependabot.yml'
GITHUB_DEPENDABOT_HEADER = '''
version: 2

# WARNING: generated file, use update.py for updates

# Multiple directories not working properly
# See https://github.com/dependabot/dependabot-core/issues/2178

updates:
'''
GITHUB_DEPENDABOT_TEMPLATE = '''
  - package-ecosystem: docker
    directory: /buildenv-{name}
    schedule:
      interval: weekly
'''


def replace_shell_pseudo_variables(where, variables):
    if not variables:
        return where
    # https://stackoverflow.com/a/15448887
    variables_escaped = [
        '\\$\\{(' + re.escape(name) + ')\\}'
        for name in sorted(variables, key=len, reverse=True)
    ]
    all_variables = re.compile("|".join(variables_escaped), flags=re.DOTALL)
    return all_variables.sub(lambda x: variables[x.group(1)], where)


def update_version(dockerfile, config: dict, docker_config: dict):
    install_packages = " ".join(COMMON_PACKAGES + config.get('extra_packages', []))
    extra_commands = "".join(
        " \\\n    && {}".format(replace_shell_pseudo_variables(cmd, config.get('command_vars', {})))
        for cmd in config.get('commands', [])
    )

    dockerfile_vars = dict(
        base_image=docker_config['DOCKER_BASE_IMAGE'],
        image_name=docker_config['DOCKER_IMAGE_NAME'],
        image_variant=config['name'],
        image_version=docker_config['DOCKER_IMAGE_VERSION_TAG'],
        install_packages=install_packages,
        maintainer_email=config['maintainer'],
        extra_commands=extra_commands,
        common=DOCKERFILE_COMMON,
    )

    if 'package' in config:
        dockerfile_content = DOCKERFILE_TEMPLATE_FROM_PACKAGE.format(
            package=config['package'],
            **dockerfile_vars
        )
    else:
        dockerfile_content = DOCKERFILE_TEMPLATE_FROM_TARBALL.format(
            tarball_basename=config['basedir'],
            tarball_basedir=config['basedir'],
            tarball_url=config['tarball'],
            **dockerfile_vars
        )

    dockerfile.write(dockerfile_content)


def load_config(filename: str):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        pairs = [line.split("=", maxsplit=2) for line in lines]
        return dict(pairs)


def main():
    docker_config = load_config(DOCKER_CONFIG)

    for version_config in VERSIONS:
        base_dir = "buildenv-{name}".format(**version_config)
        try:
            os.mkdir(base_dir, mode = 0o777)
        except FileExistsError:
            pass
        with open(os.path.join(base_dir, 'Dockerfile'), 'w') as f:
            print("Updating {name} ...".format(**version_config), file=sys.stderr)
            update_version(f, version_config, docker_config)

    with open(GITHUB_WORKFLOW_FILENAME, 'w') as f:
        print(GITHUB_WORKFLOW_HEADER, file=f)
        for version_config in VERSIONS:
            print(GITHUB_WORKFLOW_TEMPLATE.format(**version_config), file=f)

    with open(GITHUB_DEPENDABOT_FILENAME, 'w') as f:
        print(GITHUB_DEPENDABOT_HEADER, file=f)
        for version_config in VERSIONS:
            if version_config.get('dependabot_checks', False):
                print(GITHUB_DEPENDABOT_TEMPLATE.format(**version_config), file=f)

if __name__ == '__main__':
    main()
