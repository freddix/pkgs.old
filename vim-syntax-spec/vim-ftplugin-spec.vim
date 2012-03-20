" Vim filetype plugin file
" Language: RPM spec file
" Author:   Elan Ruusamäe <glen@pld-linux.org>, Zsolt Udvari <uzsolt@pld-linux.org>
" Copyright:    Copyright (c) 2005-2010 PLD Linux
" Licence:  You may redistribute this under the same terms as Vim itself
"
" This sets up filetype specific options for RPM spec files.

"setlocal tw=70

map <F5> :!builder -5 %<CR>
map <F6> :!adapter %<CR>
map <F8> :!rpmbuild -bb %<CR>
map <F9> :!. /etc/shrc.d/rpm-build.sh; cvs diff -u % \| diffcol \| less -nR<CR>
map <F10> :!builder -bb -R -u %<CR>

" which langs do you use, you can modify
" should use ""
let langlist = ["","hu"]

let UTF8 = ".UTF-8"

" default Group of some subpackages
let groups = { "devel":"Development/Libraries" , "static":"Development/Libraries" }

" This function queries the subpackage name
function! QuerySubpackage()
	return input("Subpackage name: ","")
endfunction

" Returns a Summary field (with 'lang')
function! GetSummary(lang)
	let sumstr = "Summary"
	let sumstr .= a:lang != "" ? "(" . a:lang . g:UTF8 . "):" : ""
	let sumstr .= "\t"
	return sumstr
endfunction

" Returns a %description, with lang and -n
function! GetDescription(lang,subpackage,n)
	let descstr = "%description "
	if a:subpackage != ""
		if a:n > 0
			descstr .= "-n "
		endif
		let descstr .= a:subpackage
	endif
	if a:lang != ""
		let descstr .= " -l " . a:lang . g:UTF8
	endif
	return descstr . "\n"
endfunction

" Write Summary fielad
function! Summary(lang)
	execute "normal O" . GetSummary(a:lang)
endfunction

" Write %description
function! Description(lang,subpackage,n)
	execute "normal O" . GetDescription(a:lang,a:subpackage,a:n)
endfunction

" Complete create a subpackage
function! CreateSubpackage(n)
	let subpackstr = "%package "
	if a:n > 0 
		let subpackstr .= "-n "
	endif
	let subpackname = QuerySubpackage()
	let subpackstr .= subpackname . "\n"
	for lang in g:langlist 
		let subpackstr .= GetSummary(lang) . input("Summary" . (lang!="" ? "(" . lang . g:UTF8 . ")" : "") . ": ","") . "\n"
	endfor
	let subpackstr .= "Group:\t\t" . input("Group: ",has_key(g:groups,subpackname) ? g:groups[subpackname] : "") . "\n"
	for lang in g:langlist
		let subpackstr .= "\n" . GetDescription(lang,subpackname,a:n)
	endfor
	execute "normal O" . subpackstr
endfunction

" Search a subpackage
function! SearchSubpackage()
	let searched = QuerySubpackage()
	call search("%package .*" . searched)
endfunction

nmap <buffer>\r :call execute "normal ORequires:\t"
nmap <buffer>\br :call execute "normal OBuildRequires:\t"
nmap <buffer>\se :call Summary("")<CR>
nmap <buffer>\sh :call Summary("hu")<CR>
nmap <buffer>\sp :call Summary("pl")<CR>

nmap <buffer>\de :call Description("",QuerySubpackage(),0)<CR>
nmap <buffer>\dh :call Description("hu",QuerySubpackage(),0)<CR>
nmap <buffer>\dp :call Description("pl",QuerySubpackage(),0)<CR>

nmap <buffer>\ps :call CreateSubpackage(0)<CR>
nmap <buffer>\pn :call CreateSubpackage(1)<CR>

" Jumpings
nmap <buffer>\jc /%changelog<CR>
nmap <buffer>\jv /^Version:<CR>9l
nmap <buffer>\jp :call SearchSubpackage()<CR>

" PLD specfiles are in UTF-8 encoding
setlocal fileencodings=ucs-bom,utf-8,default,latin2

