#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8FE99503132D7742 (ant_diaz@teleline.es)
#
Name     : lzip
Version  : 1.20
Release  : 5
URL      : http://mirror.easyname.at/nongnu/lzip/lzip-1.20.tar.gz
Source0  : http://mirror.easyname.at/nongnu/lzip/lzip-1.20.tar.gz
Source99 : http://mirror.easyname.at/nongnu/lzip/lzip-1.20.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: lzip-bin
Requires: lzip-doc

%description
Description
Lzip is a lossless data compressor with a user interface similar to the
one of gzip or bzip2. Lzip can compress about as fast as gzip (lzip -0),
or compress most files more than bzip2 (lzip -9). Decompression speed is
intermediate between gzip and bzip2. Lzip is better than gzip and bzip2
from a data recovery perspective.

%package bin
Summary: bin components for the lzip package.
Group: Binaries

%description bin
bin components for the lzip package.


%package doc
Summary: doc components for the lzip package.
Group: Documentation

%description doc
doc components for the lzip package.


%prep
%setup -q -n lzip-1.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521082243
%configure --disable-static CXXFLAGS="$CXXFLAGS"
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1521082243
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lzip

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
