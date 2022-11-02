#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-config
Version  : 0.3.1
Release  : 34
URL      : https://cran.r-project.org/src/contrib/config_0.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/config_0.3.1.tar.gz
Summary  : Manage Environment Specific Configuration Values
Group    : Development/Tools
License  : GPL-3.0
Requires: R-yaml
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
development, test, production). Read values using a function that determines
  the current environment and returns the appropriate value.

%prep
%setup -q -c -n config
cd %{_builddir}/config

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640992297

%install
export SOURCE_DATE_EPOCH=1640992297
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library config
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library config
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library config
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc config || :


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
/usr/lib64/R/library/config/NEWS.md
/usr/lib64/R/library/config/R/config
/usr/lib64/R/library/config/R/config.rdb
/usr/lib64/R/library/config/R/config.rdx
/usr/lib64/R/library/config/WORDLIST
/usr/lib64/R/library/config/doc/index.html
/usr/lib64/R/library/config/doc/introduction.R
/usr/lib64/R/library/config/doc/introduction.Rmd
/usr/lib64/R/library/config/doc/introduction.html
/usr/lib64/R/library/config/help/AnIndex
/usr/lib64/R/library/config/help/aliases.rds
/usr/lib64/R/library/config/help/config.rdb
/usr/lib64/R/library/config/help/config.rdx
/usr/lib64/R/library/config/help/figures/logo.png
/usr/lib64/R/library/config/help/figures/logo.svg
/usr/lib64/R/library/config/help/paths.rds
/usr/lib64/R/library/config/html/00Index.html
/usr/lib64/R/library/config/html/R.css
/usr/lib64/R/library/config/tests/spelling.R
/usr/lib64/R/library/config/tests/testthat.R
/usr/lib64/R/library/config/tests/testthat/config-inheritself.yml
/usr/lib64/R/library/config/tests/testthat/config-multiple.yml
/usr/lib64/R/library/config/tests/testthat/config.yml
/usr/lib64/R/library/config/tests/testthat/config/conf.yml
/usr/lib64/R/library/config/tests/testthat/config/config.yml
/usr/lib64/R/library/config/tests/testthat/errors/nodefault.yml
/usr/lib64/R/library/config/tests/testthat/parent/config.yaml
/usr/lib64/R/library/config/tests/testthat/test-active.R
/usr/lib64/R/library/config/tests/testthat/test-errors.R
/usr/lib64/R/library/config/tests/testthat/test-inherit.R
/usr/lib64/R/library/config/tests/testthat/test-parent.R
/usr/lib64/R/library/config/tests/testthat/test-read.R
