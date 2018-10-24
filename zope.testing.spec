#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.testing
Version  : 4.7
Release  : 23
URL      : https://files.pythonhosted.org/packages/a2/95/2a2ed23bbb3dcf7916ff39bf349314304f6e4c4dd77d86e3930def52b45e/zope.testing-4.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/a2/95/2a2ed23bbb3dcf7916ff39bf349314304f6e4c4dd77d86e3930def52b45e/zope.testing-4.7.tar.gz
Summary  : Zope testing helpers
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.testing-python3
Requires: zope.testing-license
Requires: zope.testing-python
Requires: setuptools
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : tox
BuildRequires : virtualenv

%description
``zope.testing``
        =================

%package legacypython
Summary: legacypython components for the zope.testing package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the zope.testing package.


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

%description python3
python3 components for the zope.testing package.


%prep
%setup -q -n zope.testing-4.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538679345
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1538679345
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/zope.testing
cp LICENSE.txt %{buildroot}/usr/share/doc/zope.testing/LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/zope.testing/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
