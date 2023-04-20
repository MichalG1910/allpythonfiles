from Tkinter import *
class Application(Frame):

    def Donothing(self):
        pass
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(height=500, width=1240)
        #*** Menu Bar ***
        menu=Menu(root)
        root.config(menu=menu)
        filemenu=Menu(menu,tearoff=False)

        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.Donothing)

        helpmenu=Menu(menu,tearoff=False)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=self.Donothing)


        #*** ToolBar ***
        tool_bar=Frame(root,bg="blue")

        self.button_1=Button(tool_bar,text="Add Employee",command=self.Donothing)
        self.button_1.pack(side=LEFT)

        self.button_2=Button(tool_bar,text="Add Client",command=self.Donothing)
        self.button_2.pack(side=LEFT)
        tool_bar.pack(side=TOP)
        self.pack()


root = Tk()
root.title("Learnings")
app = Application(master=root)
app.mainloop()