%global upstream_version	1.0.0-rc3

Name:			libxchange
Version:		1.0.0.rc3
Release:		%autorelease
Summary:		Structured data representation and JSON support for C/C++
License:		Unlicense
URL:			https://smithsonian.github.io/xchange
Source0:		https://github.com/Smithsonian/xchange/archive/refs/tags/v%{upstream_version}.tar.gz
BuildRequires:		gcc
BuildRequires:		sed
BuildRequires:		doxygen >= 1.9.0

%description

The xchange library provides a free framework for platform independent data 
exchange for structured data in C/C++, and includes a JSON parser and emitter. 
It is free to use, in any way you like, without licensing restrictions.

While there are many excellent libraries out there that offer such 
capabilities for C++ and/or other object-oriented languages, support for 
structured data exchange is notably rare for standard C. The xchange library 
aims to fill that niche, by providing a data exchange framework with a 
C99-compatible API that supports the interchange of arbitrary structured data 
between different platforms and different serialization formats with ease. The 
xchange library also provides support for JSON formatting and parsing using 
the C99 standard out of the box. All that in a light-weight and fast package.

%package devel
Summary:		C development files for the xchange C/C++ library
Requires:		%{name}%{_isa} = %{version}-%{release}

%description devel
This sub-package provides C headers and the non-versioned shared library 
symbolic links for the xchange C/C++ library. It also includes API 
documentation in HTML format, which may be used with the Eclipse IDE also.


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
mv %{buildroot}/%{_docdir}/xchange %{buildroot}/%{_docdir}/libxchange

%files
%license LICENSE
%doc CHANGELOG.md
%{_libdir}/%{name}.so.1{,.*}

%files devel
%doc CONTRIBUTING.md
%doc %{_docdir}/%{name}/*
%{_prefix}/include/*
%{_libdir}/*.so

%changelog
%autochangelog

