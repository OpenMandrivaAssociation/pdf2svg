Name:		pdf2svg
Version:	0.2.1
Release:	4
Summary:	Small tool to convert PDF files into SVG
Group:		Office
License:	GPLv2+
URL:		http://www.cityinthesky.co.uk/pdf2svg.html
Source0:	http://www.cityinthesky.co.uk/files/pdf2svg-%{version}.tar.gz
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(poppler-glib)

%description
A small tool to convert PDF files into SVG using poppler and cairo.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING AUTHORS ChangeLog
%{_bindir}/pdf2svg

