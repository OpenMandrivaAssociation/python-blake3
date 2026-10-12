%undefine _debugsource_packages

# Recreate the vendor archive after a version bump:
#   tar xf blake3-VERSION.tar.gz && cd blake3-VERSION
#   cargo vendor --locked vendor
#   tar cJf python-blake3-VERSION-vendor.tar.xz vendor
#   abb store python-blake3-VERSION-vendor.tar.xz

Name:		python-blake3
Version:	1.0.11
Release:	1
Summary:	Python bindings for the BLAKE3 hash function
License:	CC0-1.0 OR Apache-2.0
Group:		Development/Python
URL:		https://github.com/oconnor663/blake3-py
Source0:	https://files.pythonhosted.org/packages/source/b/blake3/blake3-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz
BuildSystem:	python
BuildRequires:	cargo
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	rust-packaging

%description
BLAKE3 is a fast cryptographic hash. ComfyUI uses it for asset
content addressing (blake3:… widget values).

%prep -a
tar xf %{SOURCE1}
%cargo_prep -v vendor

%build -p
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true

%build -a
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%files
%doc README.md
%license LICENSE LICENSES.dependencies
%{python_sitearch}/blake3
%{python_sitearch}/blake3-%{version}.dist-info
