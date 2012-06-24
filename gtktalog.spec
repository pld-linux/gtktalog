Summary:	The Gnome disk catalog.
Name:		gtktalog
Version:	0.18.1
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	ftp://gtktalog.sourceforge.net/pub/gtktalog/gtktalog/tgz/%{name}-%{version}.tar.gz
Patch0:   %{name}-path.patch
URL:		http://gtktalog.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gnome-libs
Requires: zlib
BuildRequires: gnome-libs-devel
BuildRequires: zlib-devel

%define   _prefix   /usr/X11R6
%define   _mandir   %{_prefix}/man

%description
GTKtalog is a disk catalog, it means you can use it to create a really
small database with images of files and folders of your CD-rom. So you
can browse all your CD's very quickly, see contents of certain files
(tar.gz, rpm files ...). You can give to each folder and file a
category and a description. You can search for files in your database
with filename, category, description or file information parameter,
and find in which CD the file you are looking for is.

%description -l pl
GTKtalog jest katalogiem dysk�w. Oznacza to, �e mo�esz u�ywac go do stworzenia
ma�ej bazy zawarto�ci swoich p�yt cd. Dzi�ku temu odnalezienie pliku o znanej
nazwie (lub cz�ci nazwy) staje si� kwesti� sekund a nie godzin.
GTKtalog automatycznie rozpoznaje i odpowiedni kataloguje pliki wielu r�nych
typ�w (tar, rpm, mp3, avi, html, mpeg).

%description -l fr
GTKtalog est un catalogueur de disque. En d'autres termes, vous pouvez
l'utiliser pour cr�er une vraiment petite base de donn�es avec les
images des fichiers et r�pertoires de votre CD-rom. Vous pouvez ainsi
lire tous vos CD tr�s rapidement, voir le contenu de certains fichiers
(tar.gz, fichiers rpm...). Vous pouvez attribuer � chaque r�pertoire
ou fichier une cat�gorie, une description ou des param�tres concernant
les informations du fichier. Et ainsi vous pouvez trouver dans quel CD
se trouve le fichier que vous cherchez.

%description -l nl
GTKtalog is een schijvencatalogeerder. Je kan er kleine databanken mee
maken, die informatie van vele CD-roms en diskettes bevatten. Dus kan
je heel snel al je CD's doorzoeken, de inhoud van sommige bestanden
bekijken (tar.gz, rpm bestanden ...). Je kan iedere map en ieder
bestand een categorie en beschrijving geven. Je kan bestanden zoeken
op naam, categorie, beschrijving of bestandsinformatie. Zo vind je
snel op welke CD het bestand dat je zoekt staat.

%description -l cs
GTKtalog je katalog disk�, co� znamen� �e jej m��ete pou��t k
vytvo�en� velmi mal� datab�ze s obrazem soubor� a adres��� na va�em
CD-ROMu. M��ete si pak snadno a rychle prohl�et va�e CD, vid�t obsah
n�kter�ch soubor� (tar.gz, rpm bal��ky, ...). M��ete d�t ka�d�mu
adres��i a souboru kategorii a popis. M��ete v datab�zi hledat soubory
podle n�zvu, kategorie, popisu �i dal��ch informac� o souboru a naj�t,
na kter�m CD se hledan� soubory nach�z�.

%prep
%setup -q
#%patch0 -p1

%build
%{__aclocal} -I macros
%{__autoheader}
%{__automake} --add-missing --copy
%{__autoconf}
%configure \
	--enable-pthreads \
	--enable-catalog2 \
	--enable-catalog3 \
	--enable-htmltitle \
	--enable-mp3info \
	--enable-modinfo \
	--enable-aviinfo \
	--enable-mpeginfo \
	--disable-eject
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog Docs/README.catalog3 Docs/README.data_representation NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*
%{_libdir}/gtktalog
%{_applnkdir}/gtktalog.desktop
%{_datadir}/gnome/help/gtktalog
%{_datadir}/gtktalog
%{_datadir}/locale/*/LC_MESSAGES/gtktalog.mo
%{_datadir}/pixmaps/gtktalog.png
