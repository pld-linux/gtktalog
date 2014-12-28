#
# Note: it doesn't work with --enable-gnome20 and gtk2
#
Summary:	The GNOME disk catalog
Summary(pl.UTF-8):	Program do katalogowania płyt CD dla środowiska GNOME
Name:		gtktalog
Version:	1.0.4
Release:	5
License:	GPL
Group:		Applications/Archiving
Source0:	http://savannah.nongnu.org/download/gtktalog/%{name}-%{version}.tar.bz2
# Source0-md5:	54ed43256a0d11d078f67485e0a80e0a
Patch0:		%{name}-path.patch
Patch1:		%{name}-amfix.patch
Patch2:		%{name}-desktop.patch
URL:		http://www.freesoftware.fsf.org/gtktalog/
BuildRequires:	STLport-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	compat-gcc-34-c++
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	eject
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTKtalog is a disk catalog, it means you can use it to create a really
small database with images of files and folders of your CD-rom. So you
can browse all your CD's very quickly, see contents of certain files
(tar.gz, rpm files ...). You can give to each folder and file a
category and a description. You can search for files in your database
with filename, category, description or file information parameter,
and find in which CD the file you are looking for is.

%description -l cs.UTF-8
GTKtalog je katalog disků, což znamená že jej můžete použít k
vytvoření velmi malé databáze s obrazem souborů a adresářů na vašem
CD-ROMu. Můžete si pak snadno a rychle prohlížet vaše CD, vidět obsah
některých souborů (tar.gz, rpm balíčky, ...). Můžete dát každému
adresáři a souboru kategorii a popis. Můžete v databázi hledat soubory
podle názvu, kategorie, popisu či dalších informací o souboru a najít,
na kterém CD se hledané soubory nachází.

%description -l fr.UTF-8
GTKtalog est un catalogueur de disque. En d'autres termes, vous pouvez
l'utiliser pour créer une vraiment petite base de données avec les
images des fichiers et répertoires de votre CD-rom. Vous pouvez ainsi
lire tous vos CD très rapidement, voir le contenu de certains fichiers
(tar.gz, fichiers rpm...). Vous pouvez attribuer à chaque répertoire
ou fichier une catégorie, une description ou des paramètres concernant
les informations du fichier. Et ainsi vous pouvez trouver dans quel CD
se trouve le fichier que vous cherchez.

%description -l nl.UTF-8
GTKtalog is een schijvencatalogeerder. Je kan er kleine databanken mee
maken, die informatie van vele CD-roms en diskettes bevatten. Dus kan
je heel snel al je CD's doorzoeken, de inhoud van sommige bestanden
bekijken (tar.gz, rpm bestanden ...). Je kan iedere map en ieder
bestand een categorie en beschrijving geven. Je kan bestanden zoeken
op naam, categorie, beschrijving of bestandsinformatie. Zo vind je
snel op welke CD het bestand dat je zoekt staat.

%description -l pl.UTF-8
GTKtalog jest katalogiem dysków. Oznacza to, że możesz używać go do
stworzenia małej bazy zawartości swoich płyt cd. Dzięki temu
odnalezienie pliku o znanej nazwie (lub części nazwy) staje się
kwestią sekund a nie godzin. GTKtalog automatycznie rozpoznaje i
odpowiednio kataloguje pliki wielu różnych typów (tar, rpm, MP3, avi,
html, mpeg).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}

%configure \
	CPPFLAGS="-I%{_libdir}/gcc/i686-pld-linux/3.4.6/include/c++/backward" \
	--disable-gnomevfs \
	--enable-gnome20 \
	--enable-pthreads \
	--enable-catalog2 \
	--enable-catalog3 \
	--enable-htmltitle \
	--enable-mp3info \
	--enable-modinfo \
	--enable-aviinfo \
	--enable-mpeginfo \
	--enable-fixcd \
	--disable-eject
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Docs/README.{catalog*,data_representation,Linux} NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*
