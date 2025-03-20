Name:		pdf2svg
Version:	0.2.4
Release:	1
Summary:	Small tool to convert PDF files into SVG
Group:		Office
License:	GPLv2+
URL:		https://cityinthesky.co.uk/opensource/pdf2svg/
Source0:	https://github.com/dawbarton/pdf2svg/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(poppler-glib)

%description
A small tool to convert PDF files into SVG using poppler and cairo.

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%files
%doc COPYING AUTHORS ChangeLog
%{_bindir}/pdf2svg
