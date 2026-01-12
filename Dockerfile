FROM rockylinux:8

RUN dnf install -y dnf-plugins-core \
 && dnf config-manager --set-enabled powertools \
 && dnf -y update \
 && dnf -y install epel-release.noarch \
 && dnf -y install \
    cmake \
    dpkg \
    expect \
    gcc \
    gcc-aarch64-linux-gnu \
    git \
    glibc-devel \
    glibc-devel.i686 \
    gnupg2 \
    gnupg1 \
    https://vault.centos.org/centos/7/updates/x86_64/Packages/java-1.8.0-openjdk-1.8.0.412.b08-1.el7_9.i686.rpm \
    https://vault.centos.org/centos/7/updates/x86_64/Packages/java-1.8.0-openjdk-headless-1.8.0.412.b08-1.el7_9.i686.rpm \
    https://vault.centos.org/centos/7/updates/x86_64/Packages/java-1.8.0-openjdk-devel-1.8.0.412.b08-1.el7_9.i686.rpm \
    https://vault.centos.org/centos/7/os/x86_64/Packages/giflib-4.1.6-9.el7.i686.rpm \
    make \
    perl-ExtUtils-MakeMaker \
    rpm-build \
    rpm-sign \
    wget \
    yasm \
 && dnf -y install java-1.8.0-openjdk-devel \
 && pushd /opt \
 && wget 'https://developer.arm.com/-/media/Files/downloads/gnu-a/9.2-2019.12/binrel/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz?revision=61c3be5d-5175-4db6-9030-b565aae9f766&hash=CB9A16FCC54DC7D64F8BBE8D740E38A8BF2C8665' \
 && tar xf 'gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz?revision=61c3be5d-5175-4db6-9030-b565aae9f766&hash=CB9A16FCC54DC7D64F8BBE8D740E38A8BF2C8665' \
 && rm 'gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz?revision=61c3be5d-5175-4db6-9030-b565aae9f766&hash=CB9A16FCC54DC7D64F8BBE8D740E38A8BF2C8665' \
 && mv gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu gcc.arm64 \
 && rm -rf /opt/gcc.arm64/aarch64-none-linux-gnu/bin \
           /opt/gcc.arm64/aarch64-none-linux-gnu/include \
           /opt/gcc.arm64/aarch64-none-linux-gnu/lib \
           /opt/gcc.arm64/aarch64-none-linux-gnu/lib64 \
           /opt/gcc.arm64/aarch64-none-linux-gnu/libc/sbin \
           /opt/gcc.arm64/aarch64-none-linux-gnu/libc/usr/bin \
           /opt/gcc.arm64/aarch64-none-linux-gnu/libc/usr/lib64/*atomic* \
           /opt/gcc.arm64/aarch64-none-linux-gnu/libc/usr/lib64/*fortran* \
           /opt/gcc.arm64/aarch64-none-linux-gnu/libc/usr/lib64/*gomp* \
           /opt/gcc.arm64/aarch64-none-linux-gnu/libc/usr/lib64/*san* \
           /opt/gcc.arm64/aarch64-none-linux-gnu/libc/usr/lib64/*stdc++* \
           /opt/gcc.arm64/aarch64-none-linux-gnu/libc/usr/sbin \
           /opt/gcc.arm64/bin \
           /opt/gcc.arm64/include \
           /opt/gcc.arm64/lib \
           /opt/gcc.arm64/lib64 \
           /opt/gcc.arm64/libexec \
           /opt/gcc.arm64/share \
 && chown -R root:root gcc.arm64 \
 && wget https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u462-b08/OpenJDK8U-jdk_aarch64_linux_hotspot_8u462b08.tar.gz \
 && tar xf OpenJDK8U-jdk_aarch64_linux_hotspot_8u462b08.tar.gz \
 && rm OpenJDK8U-jdk_aarch64_linux_hotspot_8u462b08.tar.gz \
 && mv jdk8u462-b08 openjdk.arm64 \
 && rm -rf /opt/openjdk.arm64/bin \
           /opt/openjdk.arm64/jre/bin \
           /opt/openjdk.arm64/man \
           /opt/openjdk.arm64/sample \
           /opt/openjdk.arm64/src.zip \
 && shopt -s extglob \
 && find /opt/openjdk.arm64/jre/lib/* -maxdepth 0 ! -name aarch64 | xargs rm -rf \
 && find /opt/openjdk.arm64/lib/* -maxdepth 0 ! -name aarch64 | xargs rm -rf \
 && popd \
 && git clone --depth=1 https://gitlab.com/debsigs/debsigs.git -b debsigs-0.1.18-debian ~/src/debsigs \
 && pushd ~/src/debsigs \
 && echo -e '--- a/debsigs\n+++ b/debsigs\n@@ -101,7 +101,7 @@ sub cmd_sign($) {\n   #  my $gpgout = forktools::forkboth($arfd, $sigfile, "/usr/bin/gpg",\n   #"--detach-sign");\n \n-  my @cmdline = ("gpg", "--openpgp", "--detach-sign");\n+  my @cmdline = ("gpg1", "--openpgp", "--detach-sign");\n \n   if ($key) {\n     push (@cmdline, "--default-key", $key);' >patch \
 && patch -p1 <patch \
 && perl Makefile.PL \
 && make install \
 && popd \
 && rm -rf ~/src \
 && dnf -y autoremove \
    perl-ExtUtils-MakeMaker \
 && mkdir /usr/java \
 && ln -fs /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.412.b08-1.el7_9.i386 /usr/java/default32 \
 && cd / \
 && dnf clean all \
 && find /usr/lib/locale/ -mindepth 1 -maxdepth 1 -type d -not -path '*en_US*' -exec rm -rf {} \; \
 && find /usr/share/locale/ -mindepth 1 -maxdepth 1 -type d -not -path '*en_US*' -exec rm -rf {} \; \
 && localedef --list-archive | grep -v -i ^en | xargs localedef --delete-from-archive \
 && mv /usr/lib/locale/locale-archive /usr/lib/locale/locale-archive.tmpl \
 && echo "" >/usr/lib/locale/locale-archive.tmpl \
 && find /usr/share/{man,doc,info} -type f -delete \
 && rm -rf /etc/ld.so.cache \ && rm -rf /var/cache/ldconfig/* \
 && rm -rf /tmp/* \
 && git config --system --add safe.directory '*' \
 && echo '%debug_package %{nil}' >/etc/rpm/macros

# Set default command
CMD ["/bin/bash"]
