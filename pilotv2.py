
import tkinter as tk

from tkinter import ttk

win = tk.Tk()

win.title("Software RK8511")

#Frame de Aquisição de Dados

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

def hexTOint(word):
    if len(word) == 2:
        word=word[0]+'0'+word[1]
        print("word", word)
    return (int(word,16)/100)

def atualizar():
    from subprocess import Popen, PIPE
    if com.get() != ' ':
        p = Popen(["./rk8511.sh", com.get()], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        print("frame:", output)
        out = str(output)
        out = out.split()

        Vint = str(hexTOint(out[7]+out[6])/10)

        Pint = str(hexTOint(out[15]+out[14]))

        Iint = str(hexTOint(out[11]+out[10])/100)

        Rint = str(hexTOint(out[19]+out[18]))

        V.configure(text=Vint)
        W.configure(text=Pint)
        I.configure(text=Iint)
        R.configure(text=Rint)
    else:
        return "Selecione a PORTA de comunicação"
    
ttk.Button(controle, text="Atualizar", command=atualizar).grid(column=0, row=0)

#Frame de Seleção da Porta

porta = ttk.LabelFrame(win, text='Porta')

porta.grid(column=1,row=0,padx=8,pady=4)

com = ttk.Combobox(porta, width=6, state='readonly')

com['values']=(' ',0,1,2)

com.grid(column=1,row=1,padx=8,pady=16)

com.current(0)

win.mainloop()
