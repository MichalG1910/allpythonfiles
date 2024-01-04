from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12, 5), facecolor='white')

axis = fig.add_subplot(111)

xValues = [0, 5, 10, 15]

yValues0 = [5.7, 7.5, 6.6, 0]
yValues1 = [5.0, 100, 8.5, 0]
yValues2 = [6.5, 7.1, 8.7, 0]
yAll = [yValues0, yValues1, yValues2]

minY = min([y for yValues in yAll for y in yValues])

yUperrLimit = 20

maxY = max([y for yValues in yAll for y in yValues if y < yUperrLimit])

axis.set_ylim(minY, maxY)
axis.set_xlim(min(xValues), max(xValues))

t0, = axis.plot(xValues, yValues0, color='red')
t1, = axis.plot(xValues, yValues1, color='green')
t2, = axis.plot(xValues, yValues2, color='gray')

axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')

axis.grid(linestyle='dashed')

fig.legend((t0, t1, t2), ('First line', 'Second line', 'Third line'),'upper right')

def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()
