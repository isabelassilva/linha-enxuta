
import tkinter as tk

from tkinter import ttk

win = tk.Tk()

win.title("Software RK8511")

#Frame de Aquisição de Dados

interface = ttk.LabelFrame(win, text='Aquisição de Dados')

interface.grid(column=0,row=0,padx=8,pady=4)

# Labels Estáticos

refx = 0
refy = 0

ttk.Label(interface, text='Tensão (V):').grid(column=refx,row=refy,sticky='W')
ttk.Label(interface, text='Potência (W):').grid(column=refx,row=refy+1,sticky='W')
ttk.Label(interface, text='Corrente (A):').grid(column=refx+2,row=refy,sticky='W')
ttk.Label(interface, text='Resistência (ohm):').grid(column=refx+2,row=refy+1,sticky='W')

# Labels Dinâmicos

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
    child.grid_configure(padx=10,pady=6)

# Funcionalidade "Atualizar"

def hexTOint(word):
    if len(word) == 2:
        word=word[0]+'0'+word[1]
        print("word", word)
    return (int(word,16)/100)

def atualizar():
    from subprocess import Popen, PIPE
    if com.get() != ' ':
        mensagem.configure(text=' ')

        p = Popen(["./rk8511.sh", com.get()], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        if output != b'Can not open comport\n':
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
            mensagem.configure(text=" Falha de comunicaçao: Não foi possível acessar a PORTA.")
    else:
        mensagem.configure(text=" Selecione a PORTA de comunicação.")

ttk.Button(interface, text="Atualizar", command=atualizar).grid(column=1,row=refy+2, columnspan=2, padx=8,pady=12)

#Frame de Seleção da Porta

porta = ttk.LabelFrame(win, text='Porta')

porta.grid(column=1,row=0,padx=8,pady=4)

com = ttk.Combobox(porta, width=6, state='readonly')

com['values']=(' ',0,1,2)

com.grid(column=1,row=1,padx=8,pady=16)

com.current(0)

#Frame de Modos Operacionais

modo = ttk.LabelFrame(win, text='Modos Operacionais')

modo.grid(column=0,row=5, padx=8,pady=16)

modos = ["Tensão Constante",
         "Corrente Constante",
         "Potência Constante",
         "Resistência Constante"]

radVar = tk.IntVar()

radVar.set(99)

# Radiobutton callback function
def radCall():
    radSel = radVar.get()

    if radSel == 0:
        for child in entradasModo.winfo_children():
            child.configure(state='disabled', width=8)
        Vcte.configure(state='enabled')
    elif radSel == 1:
        for child in entradasModo.winfo_children():
            child.configure(state='disabled', width=8)
        Icte.configure(state='enabled')
    elif radSel == 2:
        for child in entradasModo.winfo_children():
            child.configure(state='disabled', width=8)
        Pcte.configure(state='enabled')
    elif radSel == 3:
        for child in entradasModo.winfo_children():
            child.configure(state='disabled', width=8)
        Rcte.configure(state='enabled')

    #win.configure(background=colors[radSel])

for row in range(len(modos)):
    tk.Radiobutton(modo, text=modos[row], variable=radVar, value=row, command=radCall).grid(column=refx, row=row, sticky=tk.W)

# Entradas

entradasModo = ttk.Label(modo)

entradasModo.grid(column=refx+1,row=refy, rowspan=len(modos))

Vcte = ttk.Entry(entradasModo)
Vcte.grid(column=refx+1,row=refy, sticky=tk.W)

Icte = ttk.Entry(entradasModo)
Icte.grid(column=refx+1,row=refy+1, sticky=tk.W)

Pcte = ttk.Entry(entradasModo)
Pcte.grid(column=refx+1,row=refy+2, sticky=tk.W)

Rcte = ttk.Entry(entradasModo)
Rcte.grid(column=refx+1,row=refy+3, sticky=tk.W)

for child in entradasModo.winfo_children():
    child.grid_configure(padx=10,pady=6)
    child.configure(state='disabled', width=8)

# Botão "Enviar"

def enviar():
    tipodado = radVar.get()
    if tipodado == 0:
        print("desejo enviar a tensão", Vcte.get())
    elif tipodado == 1:
        print("desejo enviar a corrente", Icte.get())
    elif tipodado == 2:
        print("desejo enviar a potência", Pcte.get())
    elif tipodado == 3:
        print("desejo enviar a resistência", Rcte.get())

ttk.Button(modo, text="Enviar", command=enviar).grid(column=0,row=refy+4, columnspan=2, padx=8,pady=12)

# StatusBar

mensagem = ttk.Label(win, text="Bem-vindo ao Software RK8511!", borderwidth=1, relief=tk.SUNKEN, anchor=tk.W)
mensagem.grid(column=0,row=9, columnspan=2, stick='WES')

win.mainloop()
