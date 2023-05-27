# Projeto desenvolvido no curso de Python - CursoemVídeo
import random
from time import sleep

print('\033[31mDesafio 058\033[m')
print('-=' * 20)
print('\033[35mJogo da Adivinhação v2.0\033[m')
print('-=' * 20)

sorte = random.randint(0, 10)
num = -1
cont = 0
# print('-=' * 30)
print('Vamos jogar!')
print('-=' * 30)
print('Regras: \n- Vou escolher 1 número de 0 a 10 e você tem quantas chances quiser para acertar!')
print('---' * 10)
print('Pensando...')
for i in range(1, 4):
    print('.')
    sleep(1)
print('Tente acertar!\n')
while sorte != num:
    num = int(input('Palpite: '))
    cont += 1
    if sorte > num:
        print('Mais... Tente novamente.')
    elif sorte < num:
        print('Menos... Tente novamente.')
print('Acertou!\n')
print('O número que escolhi foi {}.'.format(sorte))
if sorte == num:
    print('Aff, você ganhou!')
print('Foram {} tentativas para você acertar.'.format(cont))
