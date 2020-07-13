#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gridBase
Version  : 0.4.7
Release  : 28
URL      : https://cran.r-project.org/src/contrib/gridBase_0.4-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gridBase_0.4-7.tar.gz
Summary  : Integration of base and grid graphics
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n gridBase
cd %{_builddir}/gridBase

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589521992

%install
export SOURCE_DATE_EPOCH=1589521992
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gridBase
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gridBase
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gridBase
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gridBase || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gridBase/DESCRIPTION
/usr/lib64/R/library/gridBase/INDEX
/usr/lib64/R/library/gridBase/Meta/Rd.rds
/usr/lib64/R/library/gridBase/Meta/demo.rds
/usr/lib64/R/library/gridBase/Meta/features.rds
/usr/lib64/R/library/gridBase/Meta/hsearch.rds
/usr/lib64/R/library/gridBase/Meta/links.rds
/usr/lib64/R/library/gridBase/Meta/nsInfo.rds
/usr/lib64/R/library/gridBase/Meta/package.rds
/usr/lib64/R/library/gridBase/Meta/vignette.rds
/usr/lib64/R/library/gridBase/NAMESPACE
/usr/lib64/R/library/gridBase/R/gridBase
/usr/lib64/R/library/gridBase/R/gridBase.rdb
/usr/lib64/R/library/gridBase/R/gridBase.rdx
/usr/lib64/R/library/gridBase/demo/gridBase.R
/usr/lib64/R/library/gridBase/doc/changes.txt
/usr/lib64/R/library/gridBase/doc/chinasea.txt
/usr/lib64/R/library/gridBase/doc/gridBase.R
/usr/lib64/R/library/gridBase/doc/gridBase.Rnw
/usr/lib64/R/library/gridBase/doc/gridBase.pdf
/usr/lib64/R/library/gridBase/doc/index.html
/usr/lib64/R/library/gridBase/help/AnIndex
/usr/lib64/R/library/gridBase/help/aliases.rds
/usr/lib64/R/library/gridBase/help/gridBase.rdb
/usr/lib64/R/library/gridBase/help/gridBase.rdx
/usr/lib64/R/library/gridBase/help/paths.rds
/usr/lib64/R/library/gridBase/html/00Index.html
/usr/lib64/R/library/gridBase/html/R.css
