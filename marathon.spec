%define		oname		Marathon
%define		oversion	20120128

Name:		marathon
Version:	1.0.1
Release:	3
Summary:	3D first-person shooter game
License:	GPL
Group:		Games/Arcade
Source0:	%{oname}-%{oversion}-Data.zip
URL:		http://sourceforge.net/projects/marathon/
Requires:	alephone
BuildArch:	noarch

%description
Marathon is a first-person shooter video game with a science fiction theme
developed and published by Bungie released in December 1994 for the Apple
Macintosh. Marathon was released at a time when other early first-person
shooters such as Doom were enjoying popularity amongst PC users, and it was
widely seen as a Macintosh counterpart to Doom (which would not be ported to
the Macintosh platform until 1995).

The game takes place several centuries into the future in outer space and sets
the player as a security officer attempting to defeat an alien invasion aboard
a colony ship named the Marathon. Although Marathon features action-heavy,
first-person shooter gameplay similar to Doom and other contemporaries, the
game is renowned for having an intricate story line that is also an essential
element of its gameplay whereas most similar games devote minimal attention to
plot for the sake of faster, simpler, more action-oriented gameplay.

Just prior to its acquisition by Microsoft in 2000, Bungie released the source
code to the Marathon 2 engine, and the Marathon Open Source project began,
resulting in the new Marathon engine called Aleph One. Since then, the fan
community has made improvements that feature OpenGL-based, high-resolution
graphics, support for Lua, a slew of internal structural changes allowing for
more advanced 3rd party mods, and Internet-capable TCP/IP-based multiplayer.

While the fundamental technology underlying the Marathon engine is still
considered rather outdated by today's standards, Aleph One has added
significant improvements and a more modern polish to its capabilities and
ported it to a wide variety of platforms, bringing Marathon and its derivatives
far beyond their Mac roots.

%prep
%setup -q -n Marathon\ (A1)
find . -type f -exec %__chmod 0644 {} \;

%build

%install
mkdir -p %{buildroot}%{_gamesdatadir}/AlephOne/%{name}
cp -r * %{buildroot}%{_gamesdatadir}/AlephOne/%{name}/

mkdir -p %{buildroot}%{_gamesbindir}
cat > %{buildroot}%{_gamesbindir}/%{name} << EOF
#!/bin/bash

alephone %{_gamesdatadir}/AlephOne/%{name}/
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Marathon
Comment=3D first-person shooter
Exec=%{name}
Icon=/usr/share/pixmaps/marathon.png
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamesbindir}/%{name}
%{_gamesdatadir}/AlephOne/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Mon Apr 02 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 788631
- imported package marathon

