Name: pdf2svg
Version: 0.2.1
Release: %mkrel 2
Summary: Small tool to convert PDF files into SVG
Group: Office
License: GPLv2+
URL: http://www.cityinthesky.co.uk/pdf2svg.html
Source0: http://www.cityinthesky.co.uk/files/pdf2svg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpoppler-glib-devel
BuildRequires: cairo-devel

%description
A small tool to convert PDF files into SVG using poppler and cairo.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog
%{_bindir}/pdf2svg
