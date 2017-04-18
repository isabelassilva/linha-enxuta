
import tkinter as tk

from tkinter import ttk

win = tk.Tk()

win.title("Software RK8511")

interface = ttk.LabelFrame(win, text='Aquisição de Dados')

interface.grid(column=0,row=0,padx=8,pady=4)

refx = 0
refy = 0

ttk.Label(interface, text='Tensão (V):').grid(column=refx,row=refy,sticky='W')
ttk.Label(interface, text='Potência (W):').grid(column=refx,row=refy+1,sticky='W')
ttk.Label(interface, text='Corrente (A):').grid(column=refx+2,row=refy,sticky='W')
ttk.Label(interface, text='Resistência (ohm):').grid(column=refx+2,row=refy+1,sticky='W')

w=10

V = ttk.Label(interface, text=' 0.00', width=w, relief='sunken', borderwidth=2)
V.grid(column=refx+1,row=refy,sticky='W')

W = ttk.Label(interface, text=' 0.00', width=w, relief='sunken', borderwidth=2)
W.grid(column=refx+1,row=refy+1,sticky='W')

I = ttk.Label(interface, text=' 0.00', width=w, relief='sunken', borderwidth=2)
I.grid(column=refx+3,row=refy,sticky='W')

R = ttk.Label(interface, text=' 0.00', width=w, relief='sunken', borderwidth=2)
R.grid(column=refx+3,row=refy+1,sticky='W')

for child in interface.winfo_children():
    child.grid_configure(padx=8,pady=4)

controle = ttk.LabelFrame(win)

controle.grid(column=0,row=1, padx=8,pady=4)

def atualizar():
    from subprocess import Popen, PIPE
    p = Popen(['./rk8511.sh'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    print("frame:", output)
    out = str(output)
    out = out.split()
    Vhex = out[7]+out[6]
    Vint = int(Vhex,16)
    Vint = Vint/1000
    Vint = str(Vint)

    Phex = out[15]+out[14]
    Pint = int(Phex,16)
    Pint = Pint/100
    Pint = str(Pint)

    Ihex = out[11]+out[10]
    Iint = int(Ihex,16)
    Iint = Iint/10000
    Iint = str(Iint)

    Rhex = out[19]+out[18]
    Rint = int(Rhex,16)
    Rint = Rint/100
    Rint = str(Rint)

    print(Vint)
    print(Pint)
    print(Iint)
    print(Rint)

    V.configure(text=Vint)
    W.configure(text=Pint)
    I.configure(text=Iint)
    R.configure(text=Rint)

ttk.Button(controle, text="Atualizar", command=atualizar).grid(column=0, row=0)

win.mainloop()
