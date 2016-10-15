#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python LESS Compiler
Summary(pl.UTF-8):	Kompilator języka LESS w Pythonie
Name:		python-lesscpy
Version:	0.12.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/lesscpy
Source0:	https://files.pythonhosted.org/packages/source/l/lesscpy/lesscpy-%{version}.tar.gz
# Source0-md5:	0a5a3ca4091ad3fb62ac6f705f8463d4
Patch0:		%{name}-tests.patch
URL:		https://pypi.python.org/pypi/lesscpy
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-coverage
BuildRequires:	python-flake8
BuildRequires:	python-nose
BuildRequires:	python-ply
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage
BuildRequires:	python3-flake8
BuildRequires:	python3-nose
BuildRequires:	python3-six
%endif
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A compiler written in Python for the LESS language. For those of us
not willing or able to have node.js installed in our environment. Not
all features of LESS are supported (yet). Some features wil probably
never be supported (JavaScript evaluation). This program uses PLY
(Python Lex-Yacc) to tokenize / parse the input and is considerably
slower than the NodeJS compiler. The plan is to utilize this to build
in proper syntax checking and perhaps YUI compressing.

%description -l pl.UTF-8
Napisany w Pythonie kompilator języka LESS, przeznaczony głównie dla
tych, którzy nie chcą lub nie mogą mieć zainstalowanego środowiska
node.js. (Jeszcze) nie wszystkie możliwości języka LESS są
obsługiwane; niektóre pewnie nigdy nie będą (wykonywania JavaScriptu).
Ten kod do analizy wejścia wykorzystuje moduł PLY (Python Lex-Yacc) i
jest znacząco wolniejszy od kompilatora NodeJS. Jest plan
wykorzystania takiego rozwiązania do stworzenia sprawdzania właściwej
składni i może kompresji YUI.

%package -n python3-lesscpy
Summary:	Python LESS Compiler
Summary(pl.UTF-8):	Kompilator języka LESS w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-lesscpy
A compiler written in Python for the LESS language. For those of us
not willing or able to have node.js installed in our environment. Not
all features of LESS are supported (yet). Some features wil probably
never be supported (JavaScript evaluation). This program uses PLY
(Python Lex-Yacc) to tokenize / parse the input and is considerably
slower than the NodeJS compiler. The plan is to utilize this to build
in proper syntax checking and perhaps YUI compressing.

%description -n python3-lesscpy -l pl.UTF-8
Napisany w Pythonie kompilator języka LESS, przeznaczony głównie dla
tych, którzy nie chcą lub nie mogą mieć zainstalowanego środowiska
node.js. (Jeszcze) nie wszystkie możliwości języka LESS są
obsługiwane; niektóre pewnie nigdy nie będą (wykonywania JavaScriptu).
Ten kod do analizy wejścia wykorzystuje moduł PLY (Python Lex-Yacc) i
jest znacząco wolniejszy od kompilatora NodeJS. Jest plan
wykorzystania takiego rozwiązania do stworzenia sprawdzania właściwej
składni i może kompresji YUI.

%prep
%setup -q -n lesscpy-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
LC_ALL=en_US.UTF-8 \
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/lesscpy{,-3}
%endif

%if %{with python2}
%py_install
%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/lesscpy{,-2}
ln -sf lesscpy-2 $RPM_BUILD_ROOT%{_bindir}/lesscpy
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/lesscpy
%attr(755,root,root) %{_bindir}/lesscpy-2
%{py_sitescriptdir}/lesscpy
%{py_sitescriptdir}/lesscpy-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-lesscpy
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/lesscpy-3
%{py3_sitescriptdir}/lesscpy
%{py3_sitescriptdir}/lesscpy-%{version}-py*.egg-info
%endif
