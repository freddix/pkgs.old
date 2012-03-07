%define		abi	5.14.0

%define		perlthread	-thread-multi
%define		perl_vendorarch	%{_libdir}/perl5/vendor_perl/%{abi}/%{_target_platform}%{perlthread}
%define		perl_vendorlib	%{_datadir}/perl5/vendor_perl

%define		rel	1
Summary:	Common dirs for Perl modules
Name:		perl-dirs
Version:	4
Release:	%{rel}@%{abi}
License:	Public Domain
Group:		Development/Languages/Perl
BuildRequires:	perl-base
Provides:	%{name}(%{_target_cpu}) = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no binary blobs packaged
%define		_enable_debug_packages	0

%description
Common dirs for Perl modules.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorarch},%{perl_vendorlib}}

while read dir; do
	install -d $RPM_BUILD_ROOT$dir
done <<EOF
%{perl_vendorarch}/AI
%{perl_vendorarch}/Algorithm
%{perl_vendorarch}/Apache
%{perl_vendorarch}/Astro
%{perl_vendorarch}/Audio
%{perl_vendorarch}/Authen
%{perl_vendorarch}/B
%{perl_vendorarch}/BSD
%{perl_vendorarch}/Bit
%{perl_vendorarch}/Chemistry
%{perl_vendorarch}/Class
%{perl_vendorarch}/Compress
%{perl_vendorarch}/Compress/Raw
%{perl_vendorarch}/Convert
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/Crypt/OpenSSL
%{perl_vendorarch}/Data
%{perl_vendorarch}/DateTime
%{perl_vendorarch}/Devel
%{perl_vendorarch}/Device
%{perl_vendorarch}/Digest
%{perl_vendorarch}/Encode
%{perl_vendorarch}/Event
%{perl_vendorarch}/File
%{perl_vendorarch}/HTML
%{perl_vendorarch}/IO
%{perl_vendorarch}/IPC
%{perl_vendorarch}/IPTables
%{perl_vendorarch}/IPTables/IPv4
%{perl_vendorarch}/Image
%{perl_vendorarch}/Inline
%{perl_vendorarch}/Linux
%{perl_vendorarch}/Locale
%{perl_vendorarch}/MIME
%{perl_vendorarch}/Math
%{perl_vendorarch}/Math/BigInt
%{perl_vendorarch}/Net
%{perl_vendorarch}/Ogg
%{perl_vendorarch}/Ogg/Vorbis
%{perl_vendorarch}/Params
%{perl_vendorarch}/PerlIO
%{perl_vendorarch}/Speech
%{perl_vendorarch}/Speech/Recognizer
%{perl_vendorarch}/String
%{perl_vendorarch}/Sub
%{perl_vendorarch}/Sys
%{perl_vendorarch}/Template
%{perl_vendorarch}/Term
%{perl_vendorarch}/Test
%{perl_vendorarch}/Text
%{perl_vendorarch}/Time
%{perl_vendorarch}/Unicode
%{perl_vendorarch}/Unix
%{perl_vendorarch}/Variable
%{perl_vendorarch}/WWW
%{perl_vendorarch}/XML
%{perl_vendorarch}/auto/AI
%{perl_vendorarch}/auto/Algorithm
%{perl_vendorarch}/auto/Astro
%{perl_vendorarch}/auto/Audio
%{perl_vendorarch}/auto/Authen
%{perl_vendorarch}/auto/BSD
%{perl_vendorarch}/auto/Bit
%{perl_vendorarch}/auto/Chemistry
%{perl_vendorarch}/auto/Class
%{perl_vendorarch}/auto/Clone
%{perl_vendorarch}/auto/Compress
%{perl_vendorarch}/auto/Compress/Raw
%{perl_vendorarch}/auto/Convert
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/auto/Crypt/OpenSSL
%{perl_vendorarch}/auto/Data
%{perl_vendorarch}/auto/Devel
%{perl_vendorarch}/auto/Device
%{perl_vendorarch}/auto/Digest
%{perl_vendorarch}/auto/Encode
%{perl_vendorarch}/auto/Event
%{perl_vendorarch}/auto/File
%{perl_vendorarch}/auto/HTML
%{perl_vendorarch}/auto/IO
%{perl_vendorarch}/auto/IPC
%{perl_vendorarch}/auto/IPTables
%{perl_vendorarch}/auto/IPTables/IPv4
%{perl_vendorarch}/auto/Image
%{perl_vendorarch}/auto/Inline
%{perl_vendorarch}/auto/Linux
%{perl_vendorarch}/auto/List
%{perl_vendorarch}/auto/Locale
%{perl_vendorarch}/auto/MIME
%{perl_vendorarch}/auto/Math
%{perl_vendorarch}/auto/Math/BigInt
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/auto/Ogg
%{perl_vendorarch}/auto/Ogg/Vorbis
%{perl_vendorarch}/auto/Params
%{perl_vendorarch}/auto/Params/Util
%{perl_vendorarch}/auto/PerlIO
%{perl_vendorarch}/auto/Regexp
%{perl_vendorarch}/auto/Speech
%{perl_vendorarch}/auto/Speech/Recognizer
%{perl_vendorarch}/auto/String
%{perl_vendorarch}/auto/Sub
%{perl_vendorarch}/auto/Sys
%{perl_vendorarch}/auto/Term
%{perl_vendorarch}/auto/Test
%{perl_vendorarch}/auto/Text
%{perl_vendorarch}/auto/Time
%{perl_vendorarch}/auto/Unicode
%{perl_vendorarch}/auto/Unix
%{perl_vendorarch}/auto/Variable
%{perl_vendorarch}/auto/WWW
%{perl_vendorarch}/auto/XML
%{perl_vendorlib}/AI
%{perl_vendorlib}/AI/NeuralNet
%{perl_vendorlib}/Algorithm
%{perl_vendorlib}/Any
%{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache2
%{perl_vendorlib}/App
%{perl_vendorlib}/App/Packer
%{perl_vendorlib}/App/Prove
%{perl_vendorlib}/App/Prove/State
%{perl_vendorlib}/App/Prove/State/Result
%{perl_vendorlib}/Archive
%{perl_vendorlib}/Array
%{perl_vendorlib}/Astro
%{perl_vendorlib}/Attribute
%{perl_vendorlib}/Audio
%{perl_vendorlib}/Authen
%{perl_vendorlib}/B
%{perl_vendorlib}/Barcode
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/Business
%{perl_vendorlib}/CGI
%{perl_vendorlib}/CGI/Emulate
%{perl_vendorlib}/CSS
%{perl_vendorlib}/Cache
%{perl_vendorlib}/Carp
%{perl_vendorlib}/Chart
%{perl_vendorlib}/Cisco
%{perl_vendorlib}/Class/Data
%{perl_vendorlib}/Class/Inspector
%{perl_vendorlib}/Class/Method
%{perl_vendorlib}/Clone
%{perl_vendorlib}/Compress
%{perl_vendorlib}/Config
%{perl_vendorlib}/Convert
%{perl_vendorlib}/Crypt
%{perl_vendorlib}/DBD
%{perl_vendorlib}/DNS
%{perl_vendorlib}/Data
%{perl_vendorlib}/Date
%{perl_vendorlib}/Date/Japanese
%{perl_vendorlib}/DateTime
%{perl_vendorlib}/Devel
%{perl_vendorlib}/Device
%{perl_vendorlib}/Digest
%{perl_vendorlib}/Email
%{perl_vendorlib}/Email/Simple
%{perl_vendorlib}/Error
%{perl_vendorlib}/Event
%{perl_vendorlib}/Expect
%{perl_vendorlib}/Exporter
%{perl_vendorlib}/ExtUtils
%{perl_vendorlib}/File
%{perl_vendorlib}/File/Path
%{perl_vendorlib}/Filesys
%{perl_vendorlib}/Filter
%{perl_vendorlib}/Font
%{perl_vendorlib}/Games
%{perl_vendorlib}/Getopt
%{perl_vendorlib}/GnuPG
%{perl_vendorlib}/Graph
%{perl_vendorlib}/Graphics
%{perl_vendorlib}/HTML
%{perl_vendorlib}/HTTP
%{perl_vendorlib}/HTTP/Message
%{perl_vendorlib}/Hash
%{perl_vendorlib}/Hook
%{perl_vendorlib}/I18N
%{perl_vendorlib}/IO
%{perl_vendorlib}/IO/Socket
%{perl_vendorlib}/IPC
%{perl_vendorlib}/Image
%{perl_vendorlib}/Inline
%{perl_vendorlib}/Jabber
%{perl_vendorlib}/JavaScript
%{perl_vendorlib}/Language
%{perl_vendorlib}/Lingua
%{perl_vendorlib}/Lingua/EN
%{perl_vendorlib}/Lingua/Stem
%{perl_vendorlib}/Lingua/Stem/Snowball
%{perl_vendorlib}/Linux
%{perl_vendorlib}/List
%{perl_vendorlib}/Locale
%{perl_vendorlib}/Locale/Maketext
%{perl_vendorlib}/LockFile
%{perl_vendorlib}/Log
%{perl_vendorlib}/MIME
%{perl_vendorlib}/Mail
%{perl_vendorlib}/Math
%{perl_vendorlib}/Math/BigInt
%{perl_vendorlib}/Math/Business
%{perl_vendorlib}/Math/Calc
%{perl_vendorlib}/Math/Fractal
%{perl_vendorlib}/Modem
%{perl_vendorlib}/Module
%{perl_vendorlib}/Module/Pluggable
%{perl_vendorlib}/Mozilla
%{perl_vendorlib}/Net
%{perl_vendorlib}/Net/IDN
%{perl_vendorlib}/Net/SMTP
%{perl_vendorlib}/NetAddr
%{perl_vendorlib}/NetAddr/IP
%{perl_vendorlib}/NetServer
%{perl_vendorlib}/Netscape
%{perl_vendorlib}/News
%{perl_vendorlib}/Number
%{perl_vendorlib}/OLE
%{perl_vendorlib}/Object
%{perl_vendorlib}/PAR
%{perl_vendorlib}/PHP
%{perl_vendorlib}/Package
%{perl_vendorlib}/Parallel
%{perl_vendorlib}/Params
%{perl_vendorlib}/Parse
%{perl_vendorlib}/PerlIO
%{perl_vendorlib}/PerlIO/via
%{perl_vendorlib}/Pod
%{perl_vendorlib}/PostScript
%{perl_vendorlib}/Probe
%{perl_vendorlib}/Proc
%{perl_vendorlib}/Quantum
%{perl_vendorlib}/RADIUS
%{perl_vendorlib}/RPC
%{perl_vendorlib}/RPM
%{perl_vendorlib}/RTF
%{perl_vendorlib}/Regexp
%{perl_vendorlib}/Regexp/common
%{perl_vendorlib}/Rose
%{perl_vendorlib}/SNMP
%{perl_vendorlib}/SOAP
%{perl_vendorlib}/SOAP/Transport
%{perl_vendorlib}/SQL
%{perl_vendorlib}/SVN
%{perl_vendorlib}/Schedule
%{perl_vendorlib}/Sendmail
%{perl_vendorlib}/Server
%{perl_vendorlib}/Set
%{perl_vendorlib}/Sort
%{perl_vendorlib}/Speech
%{perl_vendorlib}/Spreadsheet
%{perl_vendorlib}/Statistics
%{perl_vendorlib}/String
%{perl_vendorlib}/Sub
%{perl_vendorlib}/Sys
%{perl_vendorlib}/TAP
%{perl_vendorlib}/TAP/Formatter
%{perl_vendorlib}/TAP/Formatter/Console
%{perl_vendorlib}/TAP/Formatter/File
%{perl_vendorlib}/TAP/Parser
%{perl_vendorlib}/TAP/Parser/Iterator
%{perl_vendorlib}/TAP/Parser/Result
%{perl_vendorlib}/TAP/Parser/Scheduler
%{perl_vendorlib}/TAP/Parser/Source
%{perl_vendorlib}/TAP/Parser/YAMLish
%{perl_vendorlib}/TeX
%{perl_vendorlib}/Template
%{perl_vendorlib}/Term
%{perl_vendorlib}/Term/ReadLine
%{perl_vendorlib}/Term/Screen
%{perl_vendorlib}/Test
%{perl_vendorlib}/Test/HTTP
%{perl_vendorlib}/Test/Perl
%{perl_vendorlib}/Test/WWW
%{perl_vendorlib}/Text
%{perl_vendorlib}/Text/Password
%{perl_vendorlib}/Text/Query
%{perl_vendorlib}/Tie
%{perl_vendorlib}/Time
%{perl_vendorlib}/Tree
%{perl_vendorlib}/UNIVERSAL
%{perl_vendorlib}/Unicode
%{perl_vendorlib}/Unix
%{perl_vendorlib}/WWW
%{perl_vendorlib}/WWW/Google
%{perl_vendorlib}/WebService
%{perl_vendorlib}/X500
%{perl_vendorlib}/XML
%{perl_vendorlib}/XML/Filter
%{perl_vendorlib}/XML/Handler
%{perl_vendorlib}/XML/Parser
%{perl_vendorlib}/XML/RSS
%{perl_vendorlib}/XML/XPath
%{perl_vendorlib}/auto
%{perl_vendorlib}/auto/AI
%{perl_vendorlib}/auto/Array
%{perl_vendorlib}/auto/Compress
%{perl_vendorlib}/auto/Config
%{perl_vendorlib}/auto/Crypt
%{perl_vendorlib}/auto/Data
%{perl_vendorlib}/auto/Devel
%{perl_vendorlib}/auto/GnuPG
%{perl_vendorlib}/auto/Mail
%{perl_vendorlib}/auto/Math
%{perl_vendorlib}/auto/Net
%{perl_vendorlib}/auto/Schedule
%{perl_vendorlib}/auto/Statistics
%{perl_vendorlib}/auto/Text
%{perl_vendorlib}/auto/WWW
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/perl5/vendor_perl
%dir %{_libdir}/perl5/vendor_perl/%{abi}
%{perl_vendorarch}
%{perl_vendorlib}

