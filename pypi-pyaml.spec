#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pyaml
Version  : 23.5.6
Release  : 59
URL      : https://files.pythonhosted.org/packages/2b/46/f03557fae63fb8deb4bde3c6f42d126b0b2d6812c45009691f5c764ebf1c/pyaml-23.5.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/46/f03557fae63fb8deb4bde3c6f42d126b0b2d6812c45009691f5c764ebf1c/pyaml-23.5.6.tar.gz
Summary  : PyYAML-based module to produce a bit more pretty and readable YAML-serialized data
Group    : Development/Tools
License  : WTFPL
Requires: pypi-pyaml-license = %{version}-%{release}
Requires: pypi-pyaml-python = %{version}-%{release}
Requires: pypi-pyaml-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
pretty-yaml (or pyaml)
======================
PyYAML_-based python module to produce a bit more pretty and human-readable YAML-serialized data.

%package license
Summary: license components for the pypi-pyaml package.
Group: Default

%description license
license components for the pypi-pyaml package.


%package python
Summary: python components for the pypi-pyaml package.
Group: Default
Requires: pypi-pyaml-python3 = %{version}-%{release}

%description python
python components for the pypi-pyaml package.


%package python3
Summary: python3 components for the pypi-pyaml package.
Group: Default
Requires: python3-core
Provides: pypi(pyaml)
Requires: pypi(pyyaml)

%description python3
python3 components for the pypi-pyaml package.


%prep
%setup -q -n pyaml-23.5.6
cd %{_builddir}/pyaml-23.5.6
pushd ..
cp -a pyaml-23.5.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683300873
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyaml
cp %{_builddir}/pyaml-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-pyaml/4263532d38628c3adc51dbce2419bc2b3cab4795 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyaml/4263532d38628c3adc51dbce2419bc2b3cab4795

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
