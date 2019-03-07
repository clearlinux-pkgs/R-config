#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-config
Version  : 0.3
Release  : 3
URL      : https://cran.r-project.org/src/contrib/config_0.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/config_0.3.tar.gz
Summary  : Manage Environment Specific Configuration Values
Group    : Development/Tools
License  : GPL-3.0
Requires: R-rlang
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
development, test, production). Read values using a function that determines
  the current environment and returns the appropriate value.

%prep
%setup -q -c -n config

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541772950

%install
export SOURCE_DATE_EPOCH=1541772950
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library config
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library config
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library config
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library config|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/config/DESCRIPTION
/usr/lib64/R/library/config/INDEX
/usr/lib64/R/library/config/Meta/Rd.rds
/usr/lib64/R/library/config/Meta/features.rds
/usr/lib64/R/library/config/Meta/hsearch.rds
/usr/lib64/R/library/config/Meta/links.rds
/usr/lib64/R/library/config/Meta/nsInfo.rds
/usr/lib64/R/library/config/Meta/package.rds
/usr/lib64/R/library/config/Meta/vignette.rds
/usr/lib64/R/library/config/NAMESPACE
/usr/lib64/R/library/config/NEWS
/usr/lib64/R/library/config/R/config
/usr/lib64/R/library/config/R/config.rdb
/usr/lib64/R/library/config/R/config.rdx
/usr/lib64/R/library/config/doc/index.html
/usr/lib64/R/library/config/doc/introduction.R
/usr/lib64/R/library/config/doc/introduction.Rmd
/usr/lib64/R/library/config/doc/introduction.html
/usr/lib64/R/library/config/help/AnIndex
/usr/lib64/R/library/config/help/aliases.rds
/usr/lib64/R/library/config/help/config.rdb
/usr/lib64/R/library/config/help/config.rdx
/usr/lib64/R/library/config/help/paths.rds
/usr/lib64/R/library/config/html/00Index.html
/usr/lib64/R/library/config/html/R.css
