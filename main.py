from tkinter import *


def kurzy():
    f=open('listek.txt','r')
    meny=[]
    while 1:
        radek = f.readline()
        if radek == '':
            break
        if radek.strip()[0] == '#':
            continue
        meny += [ radek.replace(',','.').split() ]
    f.close()
    for radek in meny:
        radek[1]=float(radek[1])
        radek[2]=float(radek[2])
        radek[3]=float(radek[3])
    return meny
mnozstvi = 1
kurz = 1
def prevody(*args):
    global mnozstvi
    global kurz
    mnozstviVar.set(str(meny[menaVar.get()][1]))
    count=meny[menaVar.get()][1]
    if transakceVar.get()==0:
        kurzVar.set(str(meny[menaVar.get()][2]))
        kurz=meny[menaVar.get()][2]
    else:
        kurzVar.set(str(meny[menaVar.get()][3]))
        kurz=meny[menaVar.get()][3]

def prepocet():
    global mnozstvi
    global kurz
    vstup =  float(vstupVar.get())
    vystup= kurz/mnozstvi * vstup
    vystupVar.set(str(vystup))

okno = Tk()
Label(okno, text=u"Směnárna").pack()


transakceVar =  IntVar()
transakceVar.set(0)

transakceRam = LabelFrame(okno, text="Transakce", padx=5, pady=5)
transakceRam.pack(anchor=W)

Radiobutton(transakceRam,text="Nákup" , variable=transakceVar, value=0).grid(row=0,column=0)
Radiobutton(transakceRam,text="Prodej", variable=transakceVar, value=1).grid(row=0,column=1)


meny=kurzy()

menaVar = IntVar()
menaVar.set(0)
menaRam = LabelFrame(okno, text="Měna", padx=5, pady=5)
menaRam.pack(anchor=W)

for n,item in enumerate(meny):
    Radiobutton(menaRam,text=item[0], variable=menaVar, value=n).pack(anchor=W)

kurzVar=StringVar()
kurzVar.set('')
mnozstviVar=StringVar()
mnozstviVar.set('')

kurzRam = LabelFrame(okno, text="Kurz", padx=5, pady=5)
kurzRam.pack(anchor=W)
mnozstviEdit = Entry(kurzRam, state='readonly', textvariable=mnozstviVar)
mnozstviEdit.pack(anchor=W)
kurzEdit = Entry(kurzRam, state='readonly', textvariable=kurzVar)
kurzEdit.pack(anchor=W)

vstupVar=StringVar()
vstupVar.set('')
vystupVar=StringVar()
vystupVar.set('')

vypocetRam = LabelFrame(okno, text="Výpočet", padx=5, pady=5)
vypocetRam.pack(anchor=W)

vstupEdit = Entry(vypocetRam, textvariable=vstupVar)
vstupEdit.pack(anchor=W)

vypocetButton= Button(vypocetRam,text="Výpočet",command=prepocet)
vypocetButton.pack(anchor=E)

vystupEdit = Entry(vypocetRam, state='readonly', textvariable=vystupVar)
vystupEdit.pack(anchor=W)
transakceVar.trace("w",prevody)
menaVar.trace("w",prevody)
okno.bind('<Map>', prevody)


okno.mainloop()