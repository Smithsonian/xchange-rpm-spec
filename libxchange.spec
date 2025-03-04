%global upstream_version	1.0.0-rc5

Name:			libxchange
Version:		1.0.0.rc5
Release:		%autorelease
Summary:		Structured data representation and JSON support for C/C++
License:		Unlicense
URL:			https://smithsonian.github.io/xchange
Source0:		https://github.com/Smithsonian/xchange/archive/refs/tags/v%{upstream_version}.tar.gz
BuildRequires:		gcc
BuildRequires:		sed
BuildRequires:		doxygen >= 1.9.0

%description

The xchange library provides a free framework for structured data 
representation in C/C++ (C99 or later), and includes JSON parsing and 
emitting functions. It is free to use, in any way you like, without 
licensing restrictions.

%package devel
Summary:		C development files for the xchange C/C++ library
Requires:		%{name}%{_isa} = %{version}-%{release}

%description devel
This sub-package provides C headers and non-versioned shared library symbolic 
links for the xchange C/C++ library.

%package doc
Summary:		Documentation for the xchange C/C++ astronomy library
BuildArch:		noarch

%description doc
This package provides HTML documentation for the xchange C/C++ library. It can 
also be used as documentation for the Eclipse IDE.

%prep
%setup -q -n xchange-%{upstream_version}

%build

make %{?_smp_mflags}

%check

make test

%install

make DESTDIR=%{buildroot} libdir=%{_libdir} install

# Reflect name change in package doc dir name
# (xchange -> libxchange for Fedora packaging purposes)
mv %{buildroot}/%{_docdir}/xchange %{buildroot}/%{_docdir}/%{name}

%files
%license LICENSE
%doc CHANGELOG.md
%{_libdir}/%{name}.so.1{,.*}

%files devel
%doc CONTRIBUTING.md
%{_prefix}/include/*
%{_libdir}/*.so

%files doc
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/xchange.tag
%doc %{_docdir}/%{name}/html

%changelog
%autochangelog

