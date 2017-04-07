import tkinter as tk

from tkinter import ttk

win = tk.Tk()

win.title("RK8511 - Teste Automático")

#win.resizable(0,0)

#ttk.Label(win, text="A Label").grid(column=0, row=0)

# Coluna PASSOS

PASSOS = 10
colPw=6 # largura da coluna PASSO
colP=1
titleRow=0 #linha dos títulos
ttk.Label(win, text='PASSO', relief='raised',width=colPw).grid(column=colP, row=titleRow)

for n in range(1, PASSOS+1):
    ttk.Label(win, text=n,relief='raised', width=colPw).grid(column=colP, row=titleRow+n)

# Coluna TIPO DE TESTE (MODO)

colMw=17 # largura da coluna MODO
colM=colP+1
ttk.Label(win, text='MODO', relief='raised', width=colMw+2).grid(column=colM, row=titleRow)

#mode = tk.StringVar()

for n in range(1, PASSOS+1):
    modeOptions = 'modeOptions'+str(n)   #eventualmente comentar
    modeOptions = ttk.Combobox(win, width=colMw, state='readonly')#, textvariable=mode[n])

    modeOptions.grid(column=colM,row=titleRow+n)

    modeOptions['values'] = ('Tensão Constante',
                             'Corrente Constante',
                             'Potencia Constante',
                             'Resistencia Constante',
                             'Aberto',
                             'Curto-Circuito')

    modeOptions.current(0)

# Coluna VALOR
colVw=8 # largura da coluna VALOR
colV=colM+1
ttk.Label(win, text='VALOR', relief='raised', width=colVw).grid(column=colV, row=titleRow)

for n in range(1, PASSOS+1):
    name = tk.StringVar()
    nameEntered = ttk.Entry(win, width=colVw, textvariable=name)
    nameEntered.grid(column=colV, row=titleRow+n)
    nameEntered.focus()

# Coluna TEMPO
colTw=8 # largura da coluna TEMPO
colT=colV+1
ttk.Label(win, text='TEMPO', relief='raised', width=colTw).grid(column=colT, row=titleRow)

for n in range(1, PASSOS+1):
    name = tk.StringVar()
    nameEntered = ttk.Entry(win, width=colTw, textvariable=name)
    nameEntered.grid(column=colT, row=titleRow+n)
    nameEntered.focus()

# Coluna TIPO DE COMPARAÇÃO
colCw=12 # largura da coluna
colC=colT+1
ttk.Label(win, text='COMPARAÇÃO', relief='raised', width=colCw+2).grid(column=colC, row=titleRow)

#mode = tk.StringVar()

for n in range(1, PASSOS+1):
    testOptions = 'testOptions'+str(n)   #eventualmente comentar
    testOptions = ttk.Combobox(win, width=colCw, state='readonly')#, textvariable=mode[n])

    testOptions.grid(column=colC,row=titleRow+n)

    testOptions['values'] = ('Tensão',
                             'Corrente',
                             'Potencia',
                             'Resistencia')

    testOptions.current(0)

# Coluna VALOR MÍNIMO
colVMINw=12 # largura da coluna VALOR
colVMIN=colC+1
ttk.Label(win, text='VALOR MÍNIMO', relief='raised', width=colVMINw).grid(column=colVMIN, row=titleRow)

for n in range(1, PASSOS+1):
    name = tk.StringVar()
    nameEntered = ttk.Entry(win, width=colVMINw, textvariable=name)
    nameEntered.grid(column=colVMIN, row=titleRow+n)
    nameEntered.focus()

# Coluna VALOR MÁXIMO
colVMAXw=12 # largura da coluna VALOR
colVMAX=colVMIN+1
ttk.Label(win, text='VALOR MÁXIMO', relief='raised', width=colVMAXw).grid(column=colVMAX, row=titleRow)

for n in range(1, PASSOS+1):
    name = tk.StringVar()
    nameEntered = ttk.Entry(win, width=colVMAXw, textvariable=name)
    nameEntered.grid(column=colVMAX, row=titleRow+n)
    nameEntered.focus()


#Button Click Event Callback Function

def clickMe():
    action.configure(text=modeOptions.get())

    #aLabel.configure(foreground='red')
    #aLabel.configure(text="A Red Label")


#Adding a Button

action = ttk.Button(win, text="Click me!", command=clickMe)

#action.configure(state='disabled')

#action.grid(column=3,row=3)

win.mainloop()



