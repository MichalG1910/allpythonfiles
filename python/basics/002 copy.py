from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import time

class a:
# root window
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x120')
        self.root.title('Progressbar Demo')
        self.pbbar()
        self.pb.start()
        self.start_button()
        self.loop()
    # progressbar
    def pbbar(self):
        self.pb = ttk.Progressbar(
            self.root,
            orient='horizontal',
            mode='determinate',
            length=280, phase=1
        )
        # place the progressbar
        self.pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        self.value_label = ttk.Label(self.root, text=self.update_progress_label())
        self.value_label.grid(column=0, row=1, columnspan=2)
        
    def update_progress_label(self):
        return f"Current Progress: {self.pb['value']}%"


    def progress(self):
        if self.pb['value'] < 100:
            self.pb['value'] += 20
            self.value_label['text'] = self.update_progress_label()
        else:
            showinfo(message='The progress completed!')
        


    def stop(self):
        self.pb.stop()
        self.value_label['text'] = self.update_progress_label()

    def loop(self):
        while self.pb['value'] < 100:
            self.pb.step(20)
            self.progress()
            self.root.update()
            time.sleep(1)

    def start_button(self):
        start_button = ttk.Button(
            self.root,
            text='Progress',
            command=self.progress
        )
        start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
    
    def stopbutton(self):
        stop_button = ttk.Button(
            self.root,
            text='Stop',
            command=self.stop
        )
        stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

b = a()
b.root.mainloop()
