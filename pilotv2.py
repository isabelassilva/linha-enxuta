
#region :: Configurações da Janela Principal

import tkinter as tk

from tkinter import ttk

win = tk.Tk()

win.title("Software RK8511")

win.attributes('-zoomed', True)

#endregion

#region :: Configuraçao de Fontes

fontsize = 30
f = ("Times News Roman", fontsize)
g = ("Times News Roman", fontsize-10)

#endregion

#region :: Style Configuring

style = ttk.Style()
style.theme_use('alt')

#endregion

#region Frame Top

top = ttk.Frame(win)
top.pack(fill='both', expand=1)

#region Frame Left

left = ttk.Frame(top)
left.pack(side=tk.LEFT, fill='both', expand=1)

#region Frame de Abas

ControleDeAbas = ttk.Notebook(left)

aba1 = ttk.Frame(ControleDeAbas)

ControleDeAbas.add(aba1, text="Modos Operacionais  ")

ControleDeAbas.pack(fill="both", expand=1)

aba2 = ttk.Frame(ControleDeAbas)

ControleDeAbas.add(aba2, text="Teste Automático    ")

#endregion

#region Parte Comum :: Aquisição de Dados

# Frame de Aquisição de Dados

interface = ttk.LabelFrame(left, text='Aquisição de Dados')

interface.pack(side=tk.BOTTOM, expand=1)

# Labels Estáticos

refx = 0
refy = 0

ttk.Label(interface, text='Tensão (V):', font=f).grid(column=refx,row=refy,sticky='W')
ttk.Label(interface, text='Potência (W):', font=f).grid(column=refx,row=refy+1,sticky='W')
ttk.Label(interface, text='Corrente (A):', font=f).grid(column=refx+2,row=refy,sticky='W')
ttk.Label(interface, text='Resistência (ohm):', font=f).grid(column=refx+2,row=refy+1,sticky='W')

# Labels Dinâmicos

w=8

V = ttk.Label(interface, text=' 0.00', width=w, relief='sunken', borderwidth=2, font=f)
V.grid(column=refx+1,row=refy,sticky='W')

W = ttk.Label(interface, text=' 0.00', width=w, relief='sunken', borderwidth=2, font=f)
W.grid(column=refx+1,row=refy+1,sticky='W')

I = ttk.Label(interface, text=' 0.00', width=w, relief='sunken', borderwidth=2, font=f)
I.grid(column=refx+3,row=refy,sticky='W')

R = ttk.Label(interface, text=' 0.00', width=w, relief='sunken', borderwidth=2, font=f)
R.grid(column=refx+3,row=refy+1,sticky='W')

for child in interface.winfo_children():
    child.grid_configure(padx=10,pady=6)

# Funcionalidade "Atualizar"


def hexTOint(word):
    if len(word) == 2:
        word=word[0]+'0'+word[1]
        print("word", word)
    return (int(word,16)/100)


from subprocess import Popen, PIPE


def atualizar():

    if com.get() != ' ':
        status.configure(text=' ')

        p = Popen(["./rk8511.sh", com.get(), "RX"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
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
            status.configure(text=" Falha de comunicaçao: Não foi possível acessar a PORTA.")
    else:
        status.configure(text=" Selecione a PORTA de comunicação.")

tk.Button(interface, text="Atualizar", command=atualizar).grid(column=1,row=refy+2, columnspan=2, padx=8,pady=12)

#endregion

#endregion

#region Frame de Botoes Comuns aos Modos e ao Teste Automático

comum = tk.Label(top, relief='flat', bd=1)
comum.pack(side=tk.RIGHT, fill='both')

#region Frame de Seleção da Porta

porta = ttk.LabelFrame(comum, text='Porta')

porta.grid(column=refx,row=refy,padx=38,pady=34)

com = ttk.Combobox(porta, width=6, state='readonly')

com['values']=(' ',0,1,2)

com.grid(column=refx,row=refy,padx=8,pady=16)

com.current(0)

#endregion

#region Seção "Em qual Aba estou"
l = ttk.Label(comum, text="a Aba que estou é")
l.grid(column=refx, row=refy+2)

def func():
    aba = ControleDeAbas.index(ControleDeAbas.select())
    l.configure(text=aba)

ttk.Button(comum, text="Detector de Abas", command=func).grid(column=refx, row=refy+1, padx=8, pady=12)

#endregion

#end region

#endregion

#endregion

#region Aba1 :: Modos Operacionais

modo = ttk.Frame(aba1)

modo.pack(side=tk.BOTTOM, expand=1)

#region RadioButtons

modos = ["Tensão Constante",
         "Corrente Constante",
         "Potência Constante",
         "Resistência Constante"]

radVar = tk.IntVar()
radVar.set(99)

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


for row in range(len(modos)):
    tk.Radiobutton(modo, text=modos[row], variable=radVar, value=row, command=radCall, font=f).grid(column=refx, row=row, sticky=tk.W)

#endregion

#region Frame de entradas

entradasModo = ttk.Label(modo)

entradasModo.grid(column=refx+1,row=refy, rowspan=len(modos))

strV = tk.StringVar()
Vcte = ttk.Entry(entradasModo,  textvariable=strV, font=f)
Vcte.grid(column=refx+1,row=refy, sticky=tk.W)

strI = tk.StringVar()
Icte = ttk.Entry(entradasModo, textvariable=strI, font=f)
Icte.grid(column=refx+1,row=refy+1, sticky=tk.W)

strP = tk.StringVar()
Pcte = ttk.Entry(entradasModo, textvariable=strP, font=f)
Pcte.grid(column=refx+1,row=refy+2, sticky=tk.W)

strR = tk.StringVar()
Rcte = ttk.Entry(entradasModo, textvariable=strR, font=f)
Rcte.grid(column=refx+1,row=refy+3, sticky=tk.W)

for child in entradasModo.winfo_children():
    child.grid_configure(padx=10,pady=6)
    child.configure(state='disabled', width=8)

#endregion

#endregion

#region Funcionalidade do Botão "Enviar"


def isnum(str):
    return str.replace('.','',1).isdigit()


def truncate(f,n):
    f = str(f)
    dot = f.find('.')
    return float(f[:dot+1+n])


def fillin(str, n):
    tam = len(str)

    while tam < n:
        str = str[:2] + '0' + str[2:]
        tam = len(str)
    else:
        if tam > n:
            return 1
    return str


overflow8 = 256
overflow9 = 512
overflow10 = 1024
overflow11 = 2048


def checksum(hexStr, s, tipo):

# 0a operação: tornando os bytes (do valor a ser enviado) somáveis
    if tipo != 'TA':
        int1 = int(hexStr[2] + hexStr[3], 16)
        int2 = int(hexStr[4] + hexStr[5], 16)

        if tipo == 0:    # 1a operação: somando o frame byte a byte /55/aa/30/00/+s+int1+int2
            soma = 303 + int1 + int2 + int(s)
        if tipo == 1:    # 1a operação: somando o frame byte a byte /55/aa/30/03/+s+int1+int2
            soma = 306 + int1 + int2 + int(s)
        if tipo == 2:  # 1a operação: somando o frame byte a byte /55/aa/30/07/+s+int1+int2
            soma = 310 + int1 + int2 + int(s)
        if tipo == 3:  # 1a operação: somando o frame byte a byte /55/aa/30/09/+s+int1+int2
            soma = 312 + int1 + int2 + int(s, 16)

    else:   # 1a operação: somando o frame byte a byte /55/aa/30/10/+s+int1+int2
        soma = 319 + s

# 2a operação: reduzindo a soma a único byte

    if soma > overflow9:
        byte = soma - overflow9

        if byte > overflow8:
            byte = byte - overflow8

    elif soma > overflow8:
        byte = soma - overflow8

# 3a operação: complementando o byte (negando cada um dos bits)
    byte_ = 255 - byte

# 4a operação: somando 1
    return hex(byte_+1)


def intTOhex(num):
    num = int(num)*1
    return hex(num)


def particiona(hexstr):
    if len(hexstr) < 7:
        byte_2 = fillin(hexstr, 6)
        s = '0'
    elif len(hexstr) > 7:
        s = hexstr[2] + hexstr[3]
        byte_2 = hexstr[0:2] + hexstr[4:]
    else:
        s = hexstr[2]
        byte_2 = hexstr[0:2] + hexstr[3:]
    return byte_2, s


#region Variáveis Auxiliares da Função sendX()

Xcte = [Vcte, Icte, Pcte, Rcte]

code = ['00', '03', '07', '09']

decimal_size = [2, 3, 2, 2]

strX = [strV, strI, strP, strR]

weight = [1000, 10000, 100, 100]

upper_bound = [150000, 300000, 15000, 9999999]

#endregion


def sendX(x):    # vai entar 0, 1, 2 ou 3
    X = Xcte[x].get()

    if isnum(X):
        status.configure(text=" ")

        Xfloat = truncate(float(X), decimal_size[x])

        strX[x].set(Xfloat)

        Xint = round(Xfloat*weight[x], 0)  # solucionando problemas de arredondamento

        if Xint > upper_bound[x]:
            strX[x].set(upper_bound[x]/weight[x])

            status.configure(text=" Valor Inválido.")

        else:
            Xhex = intTOhex(Xint)  # Retorna variável do tipo str

            Xhex, s = particiona(Xhex)

            crc = checksum(Xhex, s, x)

            status.configure(text="desejo enviar o valor, " + str(Xfloat) + " , cujo HEX é " + Xhex + ", cujo CRC é " + crc + " e s =" + s)

            Popen(["./rk8511.sh", com.get(), "TX", code[x], s, Xhex, '0', crc], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    else:
        status.configure(text=" Valor Inválido.")


def getValue(x, p):
    if x in [0,1,2,3]:
        X = value[p].get()

        if isnum(X):
            status.configure(text=" ")

            Xfloat = truncate(float(X), decimal_size[x])

            valor[p].set(Xfloat)

            Xint = round(Xfloat*weight[x], 0)  # solucionando problemas de arredondamento

            if Xint > upper_bound[x]:
                valor[p].set(upper_bound[x]/weight[x])

                status.configure(text=" Valor Inválido.")

                return 0
            else:
                Xhex = intTOhex(Xint)  # Retorna variável do tipo str

                Xhex = fillin(Xhex, 8)

                return Xhex
        else:
            status.configure(text=" Valor Inválido.")

            return 0
    else:
        return '0x000000'


def isint(num):
    r = True if num == int(num) else False
    return r


maxTime = 255


def getTime(p):
    sec = time[p].get()

    if isnum(sec):
        status.configure(text=" ")
        sec = float(sec)

        if isint(sec):
            if sec > maxTime:
                tempo[p].set(maxTime)
                status.configure(text=" Valor Inválido: O tempo deve ser no máximo 255 segundos")
                return 0

            else:
                Xhex = intTOhex(sec)
                return Xhex
        else:
            status.configure(text=" Valor Inválido: O tempo deve ser inteiro.")
            return 0
    else:
        status.configure(text=" Valor Inválido.")
        return 0


def minGetValue(x, p):
    X = minValue[p].get()

    if isnum(X):
        status.configure(text=" ")

        Xfloat = truncate(float(X), decimal_size[x])

        valorMin[p].set(Xfloat)

        Xint = round(Xfloat*weight[x], 0)  # solucionando problemas de arredondamento

        if Xint > upper_bound[x]:
            valorMin[p].set(upper_bound[x]/weight[x])

            status.configure(text=" Valor Inválido.")

            return 0
        else:
            Xhex = intTOhex(Xint)  # Retorna variável do tipo str

            Xhex = fillin(Xhex, 8)

            return Xhex
    else:
        status.configure(text=" Valor Inválido.")

        return 0


def maxGetValue(x, p):
    X = maxValue[p].get()

    if isnum(X):
        status.configure(text=" ")

        Xfloat = truncate(float(X), decimal_size[x])

        valorMax[p].set(Xfloat)

        Xint = round(Xfloat*weight[x], 0)  # solucionando problemas de arredondamento

        if Xint > upper_bound[x]:
            valorMax[p].set(upper_bound[x]/weight[x])

            status.configure(text=" Valor Inválido.")

            return 0
        else:
            Xhex = intTOhex(Xint)  # Retorna variável do tipo str

            Xhex = fillin(Xhex, 8)

            return Xhex
    else:
        status.configure(text=" Valor Inválido.")

        return 0


def checksum2(parcela):
# 1a operação: somando o frame byte a byte /55/aa/30/10/+parcela

    soma = 319 + parcela

# 2a operação: reduzindo a soma a único byte

    if soma > overflow11:
        byte = soma - overflow11
    else:
        byte = soma

    if byte > overflow10:
        byte = byte - overflow10

    if byte > overflow9:
        byte = byte - overflow9

    if byte > overflow8:
        byte = byte - overflow8

# 3a operação: complementando o byte (negando cada um dos bits)
    byte_ = 255 - byte

# 4a operação: somando 1
    return hex(byte_+1)


def enviar():
    aba = ControleDeAbas.index(ControleDeAbas.select())

    if aba == 0:
        sendX(radVar.get())

    else:

    #region Obteção dos parâmetros referentes ao FRAME0
        p = int(passos.get())

        m = modo_saida.get()
        m = 0 if m == 'Pulso' else 1

        t = modo_trigger.get()
        if t == 'Desabilitado':
            t = 0
        elif t == 'Teste Aprovado':
            t = 1
        else:
            t = 2

        crc = checksum(0, (p-1)+m+t, 'TA')

        status.configure(text='Desejo enviar ' + str(p) + ' passos, modo de saída = ' + str(m) + ', trigger = ' + str(t) + ' e CRC = ' + crc)

        Popen(["./rk8511.sh", com.get(), "TX", "10", str(t), str(m), str(p-1), crc], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    #endregion

    # region Obteção dos parâmetros referentes ao FRAMEn
        for n in range(0, PASSOS):
            p = n + 1
            p = hex(p)

            m = mode[n].current()

            x = getValue(m, n)

            t = getTime(n)

            c = test[n].current()

            xmin = minGetValue(c, n)

            xmax = maxGetValue(c, n)

            # cálculo do CRC

            parteInt = (n+1) + m + c + int(t, 16)

            parteHex = int(x[2:4], 16) + int(x[4:6], 16) + int(x[6:8], 16) + \
                       int(xmin[2:4], 16) + int(xmin[4:6], 16) + int(xmin[6:8], 16) + \
                       int(xmax[2:4], 16) + int(xmax[4:6], 16) + int(xmax[6:8], 16)

            parcela = parteInt + parteHex

            crc = checksum2(parcela)

            if (x != 0) and (t != 0) and (xmin != 0) and (xmax != 0):
                print("Passo: " + p[2:] +
                      '\tMODO: ' + str(m) +
                      '\tVALOR: ' + x +
                      '\tTEMPO: ' + t[2:] +
                      '\tCOMPAR.: ' + str(c) +
                      '\tVal.MIN: ' + xmin +
                      '\tVal.MAX: ' + xmax +
                      ' e CRC: ' + crc[2:])

                Popen(["./rk8511_.sh", com.get(), p[2:], str(m), x, t[2:], str(c), xmin, xmax, crc[2:]], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            else:
                print('Falha no passo ' + p)
                break

        print()
    #endregion


tk.Button(comum, text="ENVIAR VALORES", command=enviar, font=g, relief='raised', bd=2).grid(column=0, row=refy+4, columnspan=2, padx=8,pady=12)

#endregion

#region Parte Comum :: StatusBar

status = ttk.Label(win, text="Bem-vindo ao Software RK8511!", borderwidth=1, relief=tk.SUNKEN, anchor=tk.W)

status.pack(side=tk.BOTTOM, fill=tk.X)

#endregion

#region Aba2 :: Teste Automático

#region Frame de Configuração de Valores

conf_valores = ttk.Frame(aba2)
conf_valores.pack(expand=1)

#region Coluna PASSOS

PASSOS = 7
colPw = 6       # largura da coluna PASSO
colP = 1
titleRow = 0      # linha dos títulos
tk.Label(conf_valores, text='PASSO', relief='raised', width=colPw, anchor=tk.CENTER, font=g, borderwidth=2, height=2).grid(column=colP, row=titleRow)

for n in range(1, PASSOS+1):
    tk.Label(conf_valores, text=n, relief='raised', width=colPw, anchor=tk.CENTER, font=g, borderwidth=2).grid(column=colP, row=titleRow+n)

#endregion

#region Coluna TIPO DE TESTE (MODO)
def valueTypeDefiner(none):
    p = int(passos.get())

    for n in range(0, p):
        if (mode[n].current() == 4) or (mode[n].current() == 5):
            valor[n].set('----')
            value[n].configure(state='disabled')

            test[n].configure(state='disabled')

            if mode[n].current() == 4:
                test[n].current(0)
            else:
                test[n].current(1)

        elif not isnum(valor[n].get()):
            valor[n].set('0.000')
            value[n].configure(state='enabled')

            test[n].configure(state='enabled')


colMw = 11      # largura da coluna MODO
colM = colP+1
tk.Label(conf_valores, text='MODO', relief='raised', width=colMw+1, anchor=tk.CENTER, font=g, borderwidth=2, height=2).grid(column=colM, row=titleRow)

mode = []

for n in range(1, PASSOS+1):
    modeOptions = ttk.Combobox(conf_valores, width=colMw, state='readonly', font=g)
    modeOptions.grid(column=colM, row=titleRow+n)

    modeOptions.bind("<<ComboboxSelected>>", valueTypeDefiner)

    modeOptions['values'] = ('V Constante',
                             'I Constante',
                             'P Constante',
                             'R Constante',
                             'Aberto',
                             'Curto-Circuito')

    modeOptions.current(0)

    mode.append(modeOptions)

#endregion

#region Coluna VALOR
colVw = 7       # largura da coluna VALOR
colV = colM+1
tk.Label(conf_valores, text='VALOR', relief='raised', width=colVw, anchor=tk.CENTER, font=g, borderwidth=2, height=2).grid(column=colV, row=titleRow)

value = []
valor = []

for n in range(1, PASSOS+1):
    e = tk.StringVar()

    ent = ttk.Entry(conf_valores, width=colVw, font=g, textvariable=e, justify='center')
    ent.grid(column=colV, row=titleRow+n)

    value.append(ent)
    e.set('0.000')
    valor.append(e)

#endregion

#region Coluna TEMPO
colTw = 7       # largura da coluna TEMPO
colT = colV+1
tk.Label(conf_valores, text='TEMPO', relief='raised', width=colTw, anchor=tk.CENTER, font=g, borderwidth=2, height=2).grid(column=colT, row=titleRow)

time = []
tempo = []

for n in range(1, PASSOS+1):
    e = tk.StringVar()

    ent = ttk.Entry(conf_valores, width=colTw, font=g, textvariable=e, justify='center')
    ent.grid(column=colT, row=titleRow+n)

    time.append(ent)
    e.set('0')
    tempo.append(e)

#endregion

#region Coluna TIPO DE COMPARAÇÃO
colCw = 11      # largura da coluna
colC = colT+1
tk.Label(conf_valores, text='COMPARAÇÃO', relief='raised', width=colCw+1, anchor=tk.CENTER, font=g, borderwidth=2, height=2).grid(column=colC, row=titleRow)

test = []

for n in range(1, PASSOS+1):
    testOptions = ttk.Combobox(conf_valores, width=colCw, state='readonly', font=g)

    testOptions.grid(column=colC, row=titleRow+n)

    testOptions['values'] = ('Tensão',
                             'Corrente',
                             'Potencia',
                             'Resistencia')

    testOptions.current(0)

    test.append(testOptions)

#endregion

#region Coluna VALOR MÍNIMO
colVMINw = 7        # largura da coluna
colVMIN = colC+1
tk.Label(conf_valores, text='VALOR MÍNIMO', relief='raised', width=colVMINw, anchor=tk.CENTER, wraplength=110, font=g, borderwidth=2, justify=tk.CENTER).grid(column=colVMIN, row=titleRow)

minValue = []
valorMin = []

for n in range(1, PASSOS+1):
    e = tk.StringVar()

    ent = ttk.Entry(conf_valores, width=colVMINw, font=g, textvariable=e, justify='center')
    ent.grid(column=colVMIN, row=titleRow+n)

    minValue.append(ent)
    e.set('0.000')
    valorMin.append(e)

#endregion

#region Coluna VALOR MÁXIMO
colVMAXw = 7        # largura da coluna
colVMAX = colVMIN+1
tk.Label(conf_valores, text='VALOR MÁXIMO', relief='raised', width=colVMAXw, anchor=tk.CENTER, wraplength=120, font=g, borderwidth=2, justify=tk.CENTER).grid(column=colVMAX, row=titleRow)

maxValue = []
valorMax = []

for n in range(1, PASSOS+1):
    e = tk.StringVar()

    ent = ttk.Entry(conf_valores, width=colVMAXw, font=g, textvariable=e, justify='center')
    ent.grid(column=colVMAX, row=titleRow+n)

    maxValue.append(ent)
    e.set('0.000')
    valorMax.append(e)

#endregion

#endregion

#region Frame de Configuração de Parâmetros

conf_parametros = ttk.Frame(aba2)
conf_parametros.pack(expand=1)

#region Seleção de Passos


def selectstep(none):
    p = int(passos.get())
    for n in range(0, p):
        value[n].configure(state='enabled')
        mode[n]['state'] = 'readonly'
        time[n].configure(state='enabled')
        test[n]['state'] = 'readonly'
        minValue[n].configure(state='enabled')
        maxValue[n].configure(state='enabled')
    for n in range(p, PASSOS):
        value[n].configure(state='disabled')
        mode[n]['state'] = 'disabled'
        time[n].configure(state='disabled')
        test[n]['state'] = 'disabled'
        minValue[n].configure(state='disabled')
        maxValue[n].configure(state='disabled')

ttk.Label(conf_parametros, text='PASSOS:', font=g).grid(column=refx, row=refy)

passos = ttk.Combobox(conf_parametros, width=3, state='readonly', font=g)
passos.grid(column=refx+1, row=refy)

passos.bind("<<ComboboxSelected>>", selectstep)

strDePassos = ""

for n in range(1, PASSOS+1):
    strDePassos += ' ' + str(n)

passos['values'] = strDePassos

passos.current(PASSOS-1)

#endregion

#region Seleção do Modo de Saída

ttk.Label(conf_parametros, text='MODO DE SAÍDA:', font=g).grid(column=refx+2, row=refy)

modo_saida = ttk.Combobox(conf_parametros, width=6, state='readonly', font=g)
modo_saida.grid(column=refx+3, row=refy)

modo_saida['values'] = ('Pulso',
                        'Nível')

modo_saida.current(0)

#endregion

#region Seleção do Modo do Trigger

ttk.Label(conf_parametros, text='MODO DO TRIGGER:', font=g).grid(column=refx+4, row=refy)

modo_trigger = ttk.Combobox(conf_parametros, width=14, state='readonly', font=g)
modo_trigger.grid(column=refx+5, row=refy)

modo_trigger['values'] = ('Desabilitado',
                        'Teste Aprovado',
                        'Teste Reprovado')

modo_trigger.current(0)

#endregion

for child in conf_parametros.winfo_children():
    child.grid_configure(padx=10)

#endregion

#endregion

win.mainloop()
