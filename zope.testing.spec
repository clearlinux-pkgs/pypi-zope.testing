#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.testing
Version  : 4.9
Release  : 51
URL      : https://files.pythonhosted.org/packages/28/2c/91b2082cba956e28433785bc3cd67ab51bfc9b2965fa9b62216c16bf6239/zope.testing-4.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/28/2c/91b2082cba956e28433785bc3cd67ab51bfc9b2965fa9b62216c16bf6239/zope.testing-4.9.tar.gz
Summary  : Zope testing helpers
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.testing-license = %{version}-%{release}
Requires: zope.testing-python = %{version}-%{release}
Requires: zope.testing-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(setuptools)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
``zope.testing``
        =================

%package license
Summary: license components for the zope.testing package.
Group: Default

%description license
license components for the zope.testing package.


%package python
Summary: python components for the zope.testing package.
Group: Default
Requires: zope.testing-python3 = %{version}-%{release}

%description python
python components for the zope.testing package.


%package python3
Summary: python3 components for the zope.testing package.
Group: Default
Requires: python3-core
Provides: pypi(zope.testing)
Requires: pypi(setuptools)

%description python3
python3 components for the zope.testing package.


%prep
%setup -q -n zope.testing-4.9
cd %{_builddir}/zope.testing-4.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641415069
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.testing
cp %{_builddir}/zope.testing-4.9/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.testing/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.testing/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
