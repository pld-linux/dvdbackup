Summary:	Backup DVD structure to disk
Summary(pl):	Kopiowanie na dysk struktury DVD
Name:		dvdbackup
Version:	0.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dvd.chevelless230.com/%{name}.c
# Source0-md5:	1db5d6c8b095995457bba6bf38e8a6b5
URL:		http://dvd.chevelless230.com/dvdbackup.html
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dvdbackup lets you make exact backup of DVD structure to disk in such
a way that you can use it to master DVD, or as an input for video
editing tools on Windows or Linux.

%description -l pl
Dvdbackup pozwala stworzyæ dok³adn± kopiê struktury DVD w taki sposób,
¿e mo¿na j± pó¼niej wykorzystaæ do nagrania dysku DVD, albo jako dane
dla programów do edycji wideo pod Windows czy Linuksem.

%prep

%build
%{__cc} %{rpmcflags} %{SOURCE0} -ldvdread -o dvdbackup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install dvdbackup $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
