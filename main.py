from os.path import basename, splitext
import tkinter as tk
from tkinter import *


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Směnárna"

    def __init__(self):
        super().__init__(className=self.name)
        self.v1 = tk.IntVar(self)
        self.v2 = tk.IntVar(self)
        self.title(self.name)
        self.lbl = tk.Label(self, text="Směnárna", borderwidth=14)
        self.lbl.pack()
        
        listek=open("listek.txt", "r")

        self.lbl1 = tk.Label(self, text="Transakce:")
        self.lbl1.pack(anchor=W)
        self.radiobutton1 = Radiobutton(self, text="Nákup", variable=self.v1, value=1).pack(anchor=W)
        self.radiobutton2 = Radiobutton(self, text="Prodej", variable=self.v1, value=2).pack(anchor=W)
        self.v1.set(1)
        
        self.lbl1 = tk.Label(self, text="Měna:")
        self.lbl1.pack(anchor=W)
        self.radiobutton3 = Radiobutton(self, text="EUR", variable=self.v2, value=1).pack(anchor=W)
        self.radiobutton4 = Radiobutton(self, text="GBP", variable=self.v2, value=2).pack(anchor=W)
        self.radiobutton5 = Radiobutton(self, text="USD", variable=self.v2, value=3).pack(anchor=W)
        self.radiobutton6 = Radiobutton(self, text="JPY", variable=self.v2, value=4).pack(anchor=W)
        self.radiobutton7 = Radiobutton(self, text="IDR", variable=self.v2, value=5).pack(anchor=W)
        self.v2.set(1)
        
        self.lbl1 = tk.Label(self, text="Kurz:")
        self.lbl1.pack(anchor=W)
        self.kurz=Text(self, height=1, width=16)
        self.kurz.insert(tk.END, "100 CZK")
        self.kurz.configure(state='disabled')
        self.kurz.pack()
        self.prevod=Text(self, height=1, width=16)
        prevod100=100/kurz
        self.prevod.insert(tk.END, prevod100)
        self.prevod.configure(state="disabled")
        self.prevod.pack()
       
        self.lbl1 = tk.Label(self, text="Výpočet:")
        self.lbl1.pack(anchor=W)
        self.listbox3 = Listbox(self,height=1)
        self.listbox3.pack(anchor=W)
        for item in [u""]:
            self.listbox3.insert(END, item)
        self.listbox4 = Listbox(self,height=1)
        self.listbox4.pack(anchor=W)
        for item in [u""]:
            self.listbox4.insert(END, item)

        self.bind("<Escape>", self.quit)
        self.btn1 = tk.Button(self, text="Quit", command=self.quit)
        self.btn1.pack()

    def vypocet(self):  
        pass



    def listBoxFill(self):
        f = open('listek.txt', 'r')
        slovnik = {}
        for line in f:
            self.listBox.insert(tk.END,line.split()[0])
            slovnik[line.split()[0]] = (line.split()[1:])
        

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()