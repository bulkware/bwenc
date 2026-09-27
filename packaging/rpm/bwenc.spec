Name:           bwenc
Version:        1.6.0
Release:        1%{?dist}
Summary:        Desktop application for converting text-file encodings

License:        GPL-3.0-or-later
URL:            https://github.com/bulkware/bwenc
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pyside6
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  appstream
Requires:       python3-pyside6

%description
bwEnc converts supported text files between common character encodings.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
install -D -m 644 data/org.bulkware.bwenc.desktop \
    %{buildroot}%{_datadir}/applications/org.bulkware.bwenc.desktop
install -D -m 644 data/org.bulkware.bwenc.metainfo.xml \
    %{buildroot}%{_metainfodir}/org.bulkware.bwenc.metainfo.xml
install -D -m 644 data/icons/hicolor/512x512/apps/org.bulkware.bwenc.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/org.bulkware.bwenc.png

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/bwenc
%{python3_sitelib}/bwenc
%{python3_sitelib}/bwenc-*.dist-info
%{_datadir}/applications/org.bulkware.bwenc.desktop
%{_metainfodir}/org.bulkware.bwenc.metainfo.xml
%{_datadir}/icons/hicolor/512x512/apps/org.bulkware.bwenc.png

%changelog
* Sat Sep 27 2026 Antti-Pekka Meronen <antice@kapsi.fi> - 1.6.0-1
- Packaging system for Debian (deb) and Red Hat (rpm) based distros.
