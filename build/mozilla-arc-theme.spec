%global moz_extensions %{_datadir}/mozilla/extensions

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global src_ext_id \{52c2877e-44e1-11e5-8874-a62d1d5d46B0\} 
%global inst_dir %{moz_extensions}/%{firefox_app_id}/%{src_ext_id}
%global firefox_inst_dir %{moz_extensions}/%{firefox_app_id}

Name:           mozilla-arc-theme
Version:        44.20160126
Release:        1%{?dist}
Summary:        Arc theme for Firefox

Group:          Applications/Internet
License:        MPLv2.0
URL:            https://github.com/horst3180/arc-firefox-theme
Source0:        https://addons.cdn.mozilla.net/user-media/addons/656096/arc_theme-%{version}-fx-linux.xpi
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
Arc theme for Firefox.

Arc is a flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell 
which supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, 
Budgie, Pantheon, XFCE, Mate, etc.

%prep
#%setup -q -c

%build
rm -rf %{buildroot}

install -Dp -m 644 %SOURCE0 %{buildroot}%{firefox_inst_dir}/%{src_ext_id}.xpi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{firefox_inst_dir}/%{src_ext_id}.xpi

%changelog
* Wed Feb 10 2016 Chris Smart <csmart@kororaproject.org> - 44.20160126-1
- Initial spec.
