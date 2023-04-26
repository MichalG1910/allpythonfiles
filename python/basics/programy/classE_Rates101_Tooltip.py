#======================
# imports
#======================
import tkinter as ttk

class ToolTip(object): # object?
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text): # funkcja odpowiedzialna za wyświetlenie naszej podpowiedzi(tooltip)
        "Display text in tooltip window"
        self.text = text # nasz wyświetlany text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert") # pwrdpd. tworzy ramke naszego okna podpowiedzi (x - wsp.x, y - wsp.y, _cx - szerokość, cy - wysokość). Wysokość, szerokość na podstawie naszego wprowadzonego tekstu podpowiedzi
        print(cy)
        x = x + self.widget.winfo_rootx() + 27 # ustalamy naszą wsp.x - winfo_rootx() - pobiera współrzędną x naszego widgeta (+27 - przesunięcie naszej podpowiedzi)
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = ttk.Toplevel(self.widget) # tworzymy zmienną na nasze okienko z klasy Toplevel
        tw.wm_overrideredirect(1) # otwieramy małe okienko klasy Toplevel bez ramek
        tw.wm_geometry("+%d+%d" % (x, y)) # współrzędne wyświetlenia naszego okienka

        label = ttk.Label(tw, text=self.text, justify=ttk.LEFT, # tworzymy label do wyświetlenia w naszym oknie podpowiedzi Toplewel
                      background="grey", foreground="black", relief=ttk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.grid(ipadx=1) # dodajemy padding do naszego label. (ipadx - powoduje, że nie przesłania części naszego widgeta- usuń i a zobaczysz różnice)

    def hidetip(self): # funkcja howa nasze okienko i niszczy zmienną tw
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            
#===================================================================          
    def createToolTip(self, widget, text): # funkcja (przekazujemy do niej nasz widget do wyś. podpowiedzi i tekst podpowiedzi)
        toolTip = ToolTip(widget) # # tworzymy nasz obiekt na  klasie ToolTip
        def enter(event): # event - zdarzenie. (pwrdpd. zdarzenie - najechanie myszą na nasz widget) 
            toolTip.showtip(text)
        def leave(event): # (pwrdpd zdarzenie - zjechanie myszą z naszego widgetu
            toolTip.hidetip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave) # widget.bind(event - jakie zdarzęnie ma wystąpić, handler - powiązana funkcja do zdarzenia) - funkcja wiązania zdarzeń

