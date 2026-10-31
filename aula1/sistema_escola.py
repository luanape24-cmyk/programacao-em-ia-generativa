

import tkinter as tk



def calcular_media():
    nota_1 = float(nota1.get())
    nota_2 = float(nota2.get())
    nota_3 = float(nota3.get())
    media = (nota_1 + nota_2+ nota_3)/3
    resultado.config(text = media)

    nome_ = nome.get()

    if media >= 7:
        situacao.config(text = f'O aluno(a) {nome_} Passou DIRETO')
    elif media>= 5 and media <7:
        situacao.config(text = f'O aluno(a) {nome_} ESTA EM RECUPERACAO')
    else:
        situacao.config(text = f'O aluno(a) {nome_} NAO PASSOU...')

janela = tk.Tk()
janela.geometry('400x400')

titulo = tk.Label(janela, text = 'SISTEMA ESCOLA xyz')
titulo.pack()

nome_titulo = tk.Label(janela, text = 'nome:')
nome_titulo.pack()

nome = tk.Entry(janela)
nome.pack(pady = 5)


tk.Label(janela, text= 'nota1').pack()
nota1 = tk.Entry(janela, text =' Nota1')
nota1 = tk.Entry(janela, text = "Nota 1")
nota1.pack(pady = 5)

tk.Label(janela, text= 'nota2').pack()
nota2 = tk.Entry(janela, text =' Nota2')
nota2 = tk.Entry(janela, text = "Nota 2")
nota2.pack(pady = 5)



tk.Label(janela, text= 'nota3').pack()
nota3 = tk.Entry(janela, text =' Nota3')
nota3 = tk.Entry(janela, text = "Nota 3")
nota3.pack(pady = 5)

botao = tk.Button(janela, text = 'calcular', command = calcular_media)
botao.pack()

resultado= tk.Label(janela, text = ' ')
resultado.pack()


tk.Label(janela, text= 'SITUACAO').pack()
situacao = tk.Label(janela, text = '')
situacao.pack()


janela.mainloop()
