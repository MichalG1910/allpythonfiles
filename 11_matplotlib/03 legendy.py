from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12,5), facecolor = "grey") # obiekt (prostokąt 12 x 8 pikseli) - będzie to prostokąt na którym umieścimy wykres

axis = fig.add_subplot(111) # rozmieszczenie naszego wykresu w oknie fig (211- 2 to dwa rzędy w oknie, 1 to jedna kolumna, 1 to umieszczenie wykresu w 1 rzędzie )

axis.set_facecolor("black") # kolor tła naszego pola wykresu
axis.set_title("Wykres 1", fontsize=20, color="white") # tytuł wykresu
axis.grid(linestyle=":", color="white") # typ/kolor linii w naszym wykresie ('-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted')
# axis.set_axis_off() # brak osi
# axis.set_ylim(5,10) # skalowanie osi y(oś przyjmie wartości między 5 a 10)(axis.set_xlim())

xValues = [1, 2, 3, 4] # wartości na naszym wykresie

yValues0 = [5.7, 7.5, 6.6, 9] 
yValues1 = [5.5, 100, 8.5, 9]
yValues2 = [6.5, 7.1, 8.7, 9]

# dynamiczne skalowanie wykresu --------------------------------------------------------------------
yAll = [yValues0, yValues1, yValues2] # lista zawierająca kisty naszych wartości

minY = min([y for yValues in yAll for y in yValues ]) # szukamy minimalnej  wartości y na naszym wykresie
yUpperLimit = 20 # nasz limit dla mksymalnej wartości y

maxY = max([y for yValues in yAll for y in yValues if y < yUpperLimit]) # szukamy maksymalnej wartości y na naszym wykresie , ale nie większejniż  limitem yUpperLimit
# maxY = (max([y for yValues in yAll for y in yValues if y < yUpperLimit])) + (max([y for yValues in yAll for y in yValues if y < yUpperLimit])) * 0.05 # to samo co wyżej tylko 5 % więcej
axis.set_ylim(minY,maxY)
axis.set_xlim(min(xValues),max(xValues))
# koniec dynamicznego skalowania ----------------------------------------------------------------------


# axis.bar(xValues,yValues0) # wykres słupkowy

axis.scatter(xValues,yValues0, marker='o', alpha=1, color="yellow",edgecolors="orange",) # wykres scatter (same punkty)(marker="x")

# axis.pie([5,10,22,34], labels=['10', '5', 'c', "asdfg"]) # wykres tortowy(kołowy)
# axis.legend()

t0, = axis.plot(xValues, yValues0, color="green") # drukowanie wartości na naszym wykresie. 
t1, = axis.plot(xValues, yValues1, color="red") # t0, - przecinek jest konieczny, jeżeli chcemy dodać legendę
t2, = axis.plot(xValues, yValues2, color="blue") # możemy definiować kolor naszych linii
axis.set_xlabel("Horizontal Label", color="white", fontsize=20) # etykiety naszych osi
axis.set_ylabel("Vertical Label", fontsize=16, fontstyle="italic")




# fig.legend((t0, t1, t2), ("First line", "Second line", "third line"),"upper right") # umieszczamy legendę w obiekcie fig 
# t0,t1,t2 - nasze krzywe do opisania, first/second/tird line - opis naszych krzywych, upper right - rozmieszczenie legendy (warianty poniżej) )
# 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
def _destroyWindow(): # funkcja zamknięcia naszego wykresu/okna
    root.quit()
    root.destroy()

root = tk.Tk() # obiekt głównego okna bibliteki tkinter
root.withdraw() # 
root.protocol("WM_DELETE_WINDOW", _destroyWindow) # nasza akcja jęsli będziemy chcieli zamknąc wykres/okno

canvas = FigureCanvasTkAgg(fig, master=root) # umieszczamy nasze okno wykresu fig na naszym głównym oknie root
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1) # ułożenie naszego okna w głównym oknie

root.update()
root.deiconify()
root.mainloop()