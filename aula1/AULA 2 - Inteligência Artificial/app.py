# biblioteca para aleatoridade

import random

# numero = random.randint(1,10)
# print(numero)

print('JOGO DA ALEATORIDADE ...')
print('GANHE ATE R$ 5K ')
print('ESCOLHA UM NUMERO DE 1 A 20')
numero_maquina = random.randint(1,20)

chances = 3

for x in range(3):
    print (' VOCE TEM', chances, 'chances')
    numero_usuario = int (input('escolha o seu numero'))
    chances = chances - 1
   
    if numero_maquina == numero_usuario:
       print('VOCE FANHOU 5K!!')
else:
       print('VOCE ERROU FEIO!!!') 
       if chances == 0:
          print('A MAQUINA ESCOLHEU',numero_maquina)   
        