
#escola

#cadastro
acesso =input('Deseja acesssar o sistema? s/n --')
while True:

        print('SISTEMA ESCOLA xyz')

        nome = input('Nome Aluno>>')

        nota_1 = float(input('nota 1>> ✔'))
        nota_2 = float(input('nota 2>> ✔'))
        nota_3 = float(input('nota 3>> ✔'))



        # media
        lista =[]
        lista.append(nota_1)
        lista.append(nota_2)
        lista.append(nota_3)

        media = sum(lista)/len(lista)

        print('o aluno(a)', nome, 'possui a media', media)

        if media >= 7:
            print(f"0 {nome} Passou de Ano 😎")
        elif media >= 5 and media <=6:
            print (f'o {nome}Esta de recuperação 😒')
        else:
            print(f'o{nome}não passou de ano.....😢')
        acesso = input( 'Deseja acessar o continuar? s/n >> ')


print('ate logo...😎')
input('clique enter para sair...')

