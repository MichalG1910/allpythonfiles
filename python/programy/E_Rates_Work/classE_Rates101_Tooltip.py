import tkinter as ttk

class ToolTip(object): 
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text, changeCoordinatesX, changeCoordinatesY): 
        "Display text in tooltip window"
        self.text = text 
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert") 
        x = x + self.widget.winfo_rootx() + 27 + changeCoordinatesX
        y = y + cy + self.widget.winfo_rooty() +27 + changeCoordinatesY
        self.tipwindow = tw = ttk.Toplevel(self.widget) 
        tw.wm_overrideredirect(1)
        tw.wm_geometry(f"+{x}+{y}") 

        label = ttk.Label(tw, text=self.text, justify=ttk.LEFT,
                      background="grey", foreground="black", relief=ttk.SOLID, borderwidth=1,
                      font=("Segoe Ui", "10", "normal"))
        label.grid(ipadx=1) 

    def hidetip(self): 
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            

