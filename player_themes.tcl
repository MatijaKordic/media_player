# Copyright © 2021 rdbende <rdbende@gmail.com>

source [file join [file dirname [info script]] theme azure-light.tcl]
source [file join [file dirname [info script]] theme azure-dark.tcl]
source [file join [file dirname [info script]] theme forest-dark.tcl]
source [file join [file dirname [info script]] theme forest-light.tcl]
source [file join [file dirname [info script]] theme dark.tcl]
source [file join [file dirname [info script]] theme light.tcl]

option add *tearOff 0

proc set_theme {mode} {
	if {$mode == "azure-dark"} {
		ttk::style theme use "azure-dark"

		array set colors {
            -fg             "#ffffff"
            -bg             "#333333"
            -disabledfg     "#ffffff"
            -disabledbg     "#737373"
            -selectfg       "#ffffff"
            -selectbg       "#007fff"
        }
        
        ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -focuscolor $colors(-selectbg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -insertcolor $colors(-fg) \
            -insertwidth 1 \
            -fieldbackground $colors(-selectbg) \
            -font {"Segoe Ui" 10} \
            -borderwidth 1 \
            -relief flat

        tk_setPalette background [ttk::style lookup . -background] \
            foreground [ttk::style lookup . -foreground] \
            highlightColor [ttk::style lookup . -focuscolor] \
            selectBackground [ttk::style lookup . -selectbackground] \
            selectForeground [ttk::style lookup . -selectforeground] \
            activeBackground [ttk::style lookup . -selectbackground] \
            activeForeground [ttk::style lookup . -selectforeground]

        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        option add *font [ttk::style lookup . -font]
        option add *Menu.selectcolor $colors(-fg)
    
	} elseif {$mode == "azure-light"} {
		ttk::style theme use "azure-light"

        array set colors {
            -fg             "#000000"
            -bg             "#ffffff"
            -disabledfg     "#737373"
            -disabledbg     "#ffffff"
            -selectfg       "#ffffff"
            -selectbg       "#007fff"
        }

		ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -focuscolor $colors(-selectbg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -insertcolor $colors(-fg) \
            -insertwidth 1 \
            -fieldbackground $colors(-selectbg) \
            -font {"Segoe Ui" 10} \
            -borderwidth 1 \
            -relief flat

        tk_setPalette background [ttk::style lookup . -background] \
            foreground [ttk::style lookup . -foreground] \
            highlightColor [ttk::style lookup . -focuscolor] \
            selectBackground [ttk::style lookup . -selectbackground] \
            selectForeground [ttk::style lookup . -selectforeground] \
            activeBackground [ttk::style lookup . -selectbackground] \
            activeForeground [ttk::style lookup . -selectforeground]

        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        option add *font [ttk::style lookup . -font]
        option add *Menu.selectcolor $colors(-fg)
	} elseif {$mode == "dark"} {
        ttk::style theme use "sun-valley-dark"
    
        ttk::style configure . \
        -background $ttk::theme::sv_dark::theme_colors(-bg) \
        -foreground $ttk::theme::sv_dark::theme_colors(-fg) \
        -troughcolor $ttk::theme::sv_dark::theme_colors(-bg) \
        -focuscolor $ttk::theme::sv_dark::theme_colors(-selbg) \
        -selectbackground $ttk::theme::sv_dark::theme_colors(-selbg) \
        -selectforeground $ttk::theme::sv_dark::theme_colors(-selfg) \
        -insertwidth 1 \
        -insertcolor $ttk::theme::sv_dark::theme_colors(-fg) \
        -fieldbackground $ttk::theme::sv_dark::theme_colors(-bg) \
        -font SunValleyBodyFont \
        -borderwidth 0 \
        -relief flat

        tk_setPalette \
        background $ttk::theme::sv_dark::theme_colors(-bg) \
        foreground $ttk::theme::sv_dark::theme_colors(-fg) \
        highlightColor $ttk::theme::sv_dark::theme_colors(-selbg) \
        selectBackground $ttk::theme::sv_dark::theme_colors(-selbg) \
        selectForeground $ttk::theme::sv_dark::theme_colors(-selfg) \
        activeBackground $ttk::theme::sv_dark::theme_colors(-selbg) \
        activeForeground $ttk::theme::sv_dark::theme_colors(-selfg)
        
        ttk::style map . -foreground [list disabled $ttk::theme::sv_dark::theme_colors(-disfg)]

        option add *tearOff 0
        option add *Menu.selectColor $ttk::theme::sv_dark::theme_colors(-fg)
  
    } elseif {$mode == "light"} {
        ttk::style theme use "sun-valley-light"
        
        ttk::style configure . \
        -background $ttk::theme::sv_light::theme_colors(-bg) \
        -foreground $ttk::theme::sv_light::theme_colors(-fg) \
        -troughcolor $ttk::theme::sv_light::theme_colors(-bg) \
        -focuscolor $ttk::theme::sv_light::theme_colors(-selbg) \
        -selectbackground $ttk::theme::sv_light::theme_colors(-selbg) \
        -selectforeground $ttk::theme::sv_light::theme_colors(-selfg) \
        -insertwidth 1 \
        -insertcolor $ttk::theme::sv_light::theme_colors(-fg) \
        -fieldbackground $ttk::theme::sv_light::theme_colors(-bg) \
        -font SunValleyBodyFont \
        -borderwidth 0 \
        -relief flat

        tk_setPalette \
        background $ttk::theme::sv_light::theme_colors(-bg) \
        foreground $ttk::theme::sv_light::theme_colors(-fg) \
        highlightColor $ttk::theme::sv_light::theme_colors(-selbg) \
        selectBackground $ttk::theme::sv_light::theme_colors(-selbg) \
        selectForeground $ttk::theme::sv_light::theme_colors(-selfg) \
        activeBackground $ttk::theme::sv_light::theme_colors(-selbg) \
        activeForeground $ttk::theme::sv_light::theme_colors(-selfg)
        
        ttk::style map . -foreground [list disabled $ttk::theme::sv_light::theme_colors(-disfg)]

        option add *tearOff 0
        option add *Menu.selectColor $ttk::theme::sv_light::theme_colors(-fg)
    }
}

font create SunValleyCaptionFont -family "Segoe UI Variable Static Small" -size -12
font create SunValleyBodyFont -family "Segoe UI Variable Static Text" -size -14
font create SunValleyBodyStrongFont -family "Segoe UI Variable Static Text Semibold" -size -14
font create SunValleyBodyLargeFont -family "Segoe UI Variable Static Text" -size -18
font create SunValleySubtitleFont -family "Segoe UI Variable Static Display Semibold" -size -20
font create SunValleyTitleFont -family "Segoe UI Variable Static Display Semibold" -size -28
font create SunValleyTitleLargeFont -family "Segoe UI Variable Static Display Semibold" -size -40
font create SunValleyDisplayFont -family "Segoe UI Variable Static Display Semibold" -size -68
