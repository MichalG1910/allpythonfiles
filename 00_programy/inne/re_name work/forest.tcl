# Copyright © 2021 rdbende <rdbende@gmail.com>

source [file join [file dirname [info script]]  forest-light.tcl]
source [file join [file dirname [info script]]  forest-dark.tcl]

option add *tearOff 0

proc set_theme {mode} {
	if {$mode == "forest-dark"} {
		ttk::style theme use "forest-dark"

		array set colors {
            -fg             "#eeeeee"
            -bg             "#313131"
            -disabledfg     "#595959"
            -disabledbg     "#ffffff"
            -selectfg       "#ffffff"
            -selectbg       "#217346"
        }
        
        ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -focuscolor $colors(-selectbg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -insertwidth 1 \
            -insertcolor $colors(-fg) \
            -fieldbackground $colors(-selectbg) \
            -font {TkDefaultFont 10} \
            -borderwidth 1 \
            -relief flat

        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        tk_setPalette background [ttk::style lookup . -background] \
            foreground [ttk::style lookup . -foreground] \
            highlightColor [ttk::style lookup . -focuscolor] \
            selectBackground [ttk::style lookup . -selectbackground] \
            selectForeground [ttk::style lookup . -selectforeground] \
            activeBackground [ttk::style lookup . -selectbackground] \
            activeForeground [ttk::style lookup . -selectforeground]
        
        option add *font [ttk::style lookup . -font]
    
	} elseif {$mode == "forest-light"} {
		ttk::style theme use "forest-light"

        array set colors {
            -fg             "#313131"
            -bg             "#ffffff"
            -disabledfg     "#595959"
            -disabledbg     "#ffffff"
            -selectfg       "#ffffff"
            -selectbg       "#217346"
        }

		ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -focuscolor $colors(-selectbg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -insertwidth 1 \
            -insertcolor $colors(-fg) \
            -fieldbackground $colors(-selectbg) \
            -font {TkDefaultFont 10} \
            -borderwidth 1 \
            -relief flat

        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        tk_setPalette background [ttk::style lookup . -background] \
            foreground [ttk::style lookup . -foreground] \
            highlightColor [ttk::style lookup . -focuscolor] \
            selectBackground [ttk::style lookup . -selectbackground] \
            selectForeground [ttk::style lookup . -selectforeground] \
            activeBackground [ttk::style lookup . -selectbackground] \
            activeForeground [ttk::style lookup . -selectforeground]
        
        option add *font [ttk::style lookup . -font]
	}
}
