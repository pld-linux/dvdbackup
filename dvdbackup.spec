Summary:	Backup DVD structure to disk
Summary(pl.UTF-8):	Kopiowanie na dysk struktury DVD
Name:		dvdbackup
Version:	0.1.1
Release:	2
License:	GPL
Group:		Applications
Source0:	http://dvd-create.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	53a071d1def5ee49d702a4dd080d25ac
Patch0:		%{name}-dvdread.patch
URL:		http://dvd-create.sourceforge.net/
BuildRequires:	libdvdread-devel >= 0.9.5-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dvdbackup lets you make exact backup of DVD structure to disk in such
a way that you can use it to master DVD, or as an input for video
editing tools on Windows or Linux.

%description -l pl.UTF-8
Dvdbackup pozwala stworzyć dokładną kopię struktury DVD w taki sposób,
że można ją później wykorzystać do nagrania dysku DVD, albo jako dane
dla programów do edycji wideo pod Windows czy Linuksem.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__cc} %{rpmldflags} %{rpmcflags} src/%{name}.c -ldvdread -o dvdbackup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p dvdbackup $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dvdbackup
