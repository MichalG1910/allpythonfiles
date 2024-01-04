from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12,8), facecolor = "grey") # obiekt (prostokąt 12 x 8 pikseli) - będzie to prostokąt na którym umieścimy wykres

axis = fig.add_subplot(211) # rozmieszczenie naszego wykresu w oknie fig (211- 2 to dwa rzędy w oknie, 1 to jedna kolumna, 1 to umieszczenie wykresu w 1 rzędzie )

xValues = [1,2,3,4] # wartości na naszym wykresie
yValues = [5,7,6,8]
axis.plot(xValues, yValues) # drukowanie wartości na naszym wykresie

axis.set_xlabel("Horizontal Label") # etykiety naszych osi
axis.set_ylabel("Vertical Label")

axis.grid(linestyle=":") # typ linii w naszym wykresie ('-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted')

def _destroyWindow(): # funkcja zamknięcia naszego wykresu/okna
    root.quit()
    root.destroy()

root = tk.Tk() # obiekt głównego okna bibliteki tkinter
root.configure(background='black')
root.withdraw() # 
root.protocol("WM_DELETE_WINDOW", _destroyWindow) # nasza akcja jęsli będziemy chcieli zamknąc wykres/okno

canvas = FigureCanvasTkAgg(fig, master=root) # umieszczamy nasze okno wykresu fig na naszym głównym oknie root
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1) # ułożenie naszego okna w głównym oknie

root.update()
root.deiconify()
root.mainloop()
