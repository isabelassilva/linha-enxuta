
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

strV = tk.StringVar()
Vcte = ttk.Entry(entradasModo,  textvariable=strV)
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


def isnum(str):
    return str.replace('.','',1).isdigit()


def truncate(f,n):
    f = str(f)
    dot = f.find('.')
    return float(f[:dot+1+n])


overflow8 = 256
overflow9 = 512


def checksum(hexStr, tipo):
    if (tipo == 'V'):
        tam = len(hexStr)

    # 0a operação: tornando os bytes (do valor a ser enviado) somáveis
        while tam < 6:
            hexStr = hexStr[:2] + '0' + hexStr[2:]
            tam = len(hexStr)
        else:
            if tam > 6:
                mensagem.configure(text="Tamanho maior que quatro da representação HEX do valor a se enviado")

        int1 = int(hexStr[2] + hexStr[3], 16)
        int2 = int(hexStr[4] + hexStr[5], 16)

    # 1a operação: somando o frame byte a byte /55/aa/30/00/+int1+int2
        soma = 303 + int1 + int2

    # 2a operação: reduzindo a soma a único byte

        if soma > overflow9:
            byte = soma - overflow9

        elif soma > overflow8:
            byte = soma - overflow8

    # 3a operação: complementando o byte (negando cada um dos bits)
        byte_ = 255 - byte

    # 4a operação: somando 1
        return hex(byte_+1)


def intTOhex(num):
    num = int(num)*1
    return hex(num)


# Botão "Enviar"


def enviar():
    tipodado = radVar.get()

    if tipodado == 0:
        V = Vcte.get()

        if isnum(V):
            mensagem.configure(text=" ")

            Vfloat = truncate(float(V), 2)  # reduzindo o valor de V a duas casas decimais

            strV.set(Vfloat)

            Vint = round(Vfloat*1000,0)  # solucionando problemas de arredondamento

            if Vint > 65530:
                if Vint > 150000:
                    strV.set(150.00)
                    mensagem.configure(text=" Valor Inválido.")
                else:
                    mensagem.configure(text="Valor Representável com 3 bytes")

            else:
                Vhex = intTOhex(Vint)  # Retorna variável do tipo str
                crc = checksum(Vhex, 'V')
                mensagem.configure(text="desejo enviar a tensão, " + str(Vfloat) + " , cujo CRC é " + crc)
        else:
            mensagem.configure(text=" Valor Inválido.")

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
