%global pkg     xmltodict

Name:           python-xmltodict
Version:        0.9.0
Release:        1%{?dist}
Summary:        Makes working with XML feel like you are working with JSON

Group:          Development/Languages
License:        MIT
URL:            https://github.com/martinblech/xmltodict
Source0:        https://pypi.python.org/packages/source/x/%{pkg}/%{pkg}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-setuptools


%description
xmltodict is a Python module that makes working with XML feel like you are
working with JSON, as in this "spec":

>>> doc = xmltodict.parse("""
... <mydocument has="an attribute">
...   <and>
...     <many>elements</many>
...     <many>more elements</many>
...   </and>
...   <plus a="complex">
...     element as well
...   </plus>
... </mydocument>
... """)
>>>
>>> doc['mydocument']['@has']
u'an attribute'
>>> doc['mydocument']['and']['many']
[u'elements', u'more elements']
>>> doc['mydocument']['plus']['@a']
u'complex'
>>> doc['mydocument']['plus']['#text']
u'element as well'


%prep
%setup -q -n %{pkg}-%{version}


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}
 

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python_sitelib}/*


%changelog
* Fri Aug 22 2014 Eugene G. Zamriy <eugene@zamriy.info> - 0.9.0-1
- Initial release: 0.9.0 version
