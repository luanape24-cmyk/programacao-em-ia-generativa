# Calculadora de imc

import random

# numero = random.randint(1,10)
# print(numero)

print('CALCULADORA IMC ...')
print('COLOQUE SEU PESO')
print('COLOQUE SEU ALTURA')
peso=float(input('peso: '))
altura=float(input('altura:'))
imc = (peso / altura **2)
print('imc',imc)

   
if (imc <= 18 ):
      print('VOCE ESTA ABAIXO DO PESO')
elif imc  <= 25:
      print('PESO NORMAL')   

if (imc >=30):
      print ('SOBREPESO')
            