import tkinter
from tkinter import *
from tkinter import ttk

# cores
cor1 = '#9c0606'  # vermelho
cor2 = '#080202'  # preto
cor3 = '#fafafa'  # branco
cor4 = '#17a2b8'  # azul


janela = Tk()
janela.title('Calculadora Corinthiana')
janela.geometry('350x450')
janela.config(bg=cor1)

# criando as 2 parte
frame_tela = Frame(janela, width=350, height=100, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=350, height=370, bg=cor2)
frame_corpo.grid(row=1, column=0)


todos_valores = ''

# criando a função


def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores+str(event)

    valor_texto.set(todos_valores)


# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=37, height=7, padx=14,
                  relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 13 '), bg=cor2, fg=cor3)
app_label.place(x=0, y=0)

# função de cálculo


def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


# função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set('')


# botões
b_1 = Button(frame_corpo, command=limpar_tela, text='C', width=20, height=3, bg=cor3,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text='%', width=7, height=3,
             bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=194, y=0)
b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text='/', width=7, height=3, bg=cor1,
             fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=270, y=0)
# 7,8,9 e *
b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text='7', width=10, height=3, bg=cor3,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=1, y=70)
b_5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text='8', width=8, height=3, bg=cor3,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=110, y=70)
b_6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text='9', width=7, height=3, bg=cor3,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=194, y=70)
b_7 = Button(frame_corpo, command=lambda: entrar_valores('*'), text='*', width=7, height=3, bg=cor1,
             fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=270, y=70)

# 4,5,6 e -
b_8 = Button(frame_corpo, command=lambda: entrar_valores('4'), text='4', width=10, height=3, bg=cor3,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=1, y=140)
b_9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text='5', width=8, height=3, bg=cor3,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=110, y=140)
b_10 = Button(frame_corpo, command=lambda: entrar_valores('6'), text='6', width=7, height=3, bg=cor3,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=194, y=140)
b_11 = Button(frame_corpo, command=lambda: entrar_valores('-'), text='-', width=7, height=3, bg=cor1,
              fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=270, y=140)

# 1,2,3 e +
b_12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text='1', width=10, height=3, bg=cor3,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=1, y=210)
b_13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text='2', width=8, height=3, bg=cor3,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=110, y=210)
b_14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text='3', width=7, height=3, bg=cor3,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=194, y=210)
b_15 = Button(frame_corpo, command=lambda: entrar_valores('+'), text='+', width=7, height=3, bg=cor1,
              fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=270, y=210)

# 0, , e =
b_16 = Button(frame_corpo, command=lambda: entrar_valores('0'), text='0', width=20, height=3, bg=cor3,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=280)
b_17 = Button(frame_corpo, command=lambda: entrar_valores(','), text=',', width=7, height=3, bg=cor3,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=194, y=280)
b_18 = Button(frame_corpo, command=calcular, text='=', width=7, height=3, bg=cor1,
              fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=270, y=280)


janela.mainloop()
