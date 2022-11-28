import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

#===================================================================
def createToolTip( widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

win = tk.Tk()
win.title("Python GUI - Strefa Kursów")

# Tab Control 
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both", padx=10, pady=10)
# End Tab Control

# Widgets
#lFrame = ttk.LabelFrame(tab1, text="Jestem elementem z tab1")
#lFrame.grid(column=0, row=0, padx=10, pady=10)
#ttk.Label(lFrame, text="Label 1:").grid(column=0, row=0, sticky='W')


mainFrame = ttk.LabelFrame(tab1, text="Main Label Frame")
mainFrame.grid(column=0, row=0, columnspan=3, sticky='W', padx=10, pady=10)

mainFrame2 = ttk.LabelFrame(tab2, text="Main Label Frame Tab2")
mainFrame2.grid(column=0, row=0, columnspan=3, sticky='W', padx=10, pady=10)

#Label
aLabel = ttk.Label(mainFrame, text="Tekst bez zmiany")
aLabel.grid(column=0, row=0)

# Modyfikacja funkcj klik button
def clickMe():
    action.configure(text='Hello ' + name.get() + " " + numberChosen.get())

# Zmien naszą label
aLabel.configure(text="Enter a name:")

# Dodanie Textbox
name = tk.StringVar()
nameEntered = ttk.Entry(mainFrame, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)

# Dodanie przycisku
action = ttk.Button(mainFrame, text="Kliknij mnie", command=clickMe)
action.grid(column=2, row=1)
#action.configure(state='disabled')
nameEntered.focus()

ttk.Label(mainFrame, text="Wybierz numer:").grid(column=1,row=0)
number = tk.StringVar
numberChosen = ttk.Combobox(mainFrame, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# CheckBox

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mainFrame2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mainFrame2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mainFrame2, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

#spinbox

def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

spin = Spinbox(mainFrame, values=(10, 20, 30, 40, 50, 60), width=4, bd=10, command=_spin, relief=tk.FLAT)
spin.grid(column=0, row=2, sticky=tk.W)

createToolTip(spin, "To nasz object spin :)")

#Using scrolled Text Control

scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(mainFrame, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, sticky='WE')

createToolTip(scr, 'To nasz obiekt ScrolledText')

# RadioButton

colors = ["Blue", "Gold", "Red"]

def radCall():
    radSel = radVar.get()
    if radSel == 0: mainFrame2.configure(text=colors[0])
    elif radSel == 1: mainFrame2.configure(text=colors[1])
    elif radSel == 2: mainFrame2.configure(text=colors[2])

radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(mainFrame2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Label Frame
labelsFrame = ttk.LabelFrame(mainFrame, text=' --- Labels in Frame ---')
labelsFrame.grid(column=0, row=7, sticky='WE') # in pixel

ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=10, pady=10)

def _quit():
    win.quit()
    win.destroy()
    exit()

#Menu

menuBar = Menu(win)
win.config(menu=menuBar)

#Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

win.iconbitmap(r'D:\\ico.ico')

win.mainloop()