Summary:	Backup DVD structure to disk
Summary(pl.UTF-8):	Kopiowanie na dysk struktury DVD
Name:		dvdbackup
Version:	0.1
Release:	2
License:	GPL
Group:		Applications
Source0:	http://dvd.chevelless230.com/%{name}.c
# Source0-md5:	1db5d6c8b095995457bba6bf38e8a6b5
Source1:	http://dvd.chevelless230.com/README
# Source1-md5:	a80ef21a26c767c7fbb3e558ed50de29
Patch0:		%{name}-dvdread.patch
URL:		http://dvd.chevelless230.com/dvdbackup.html
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
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .
%patch0 -p1

%build
%{__cc} %{rpmcflags} %{name}.c -ldvdread -o dvdbackup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install dvdbackup $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
