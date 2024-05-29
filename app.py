#Jogo de adivinha o número
import random

#configurações do jogo
NUM_INICIAL = 1
NUM_FINAL = 10
NUM_TENTATIVAS = 5

jogar = True

while jogar:
    numero_secreto = random.randint(NUM_INICIAL, NUM_FINAL)
    print ('>>>>>>>>>> JOGO DA ADIVINHAÇÃO <<<<<<<<<<')
    print('TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO!')
    print('Estou pensando em um número entre ' + str (NUM_INICIAL) +  ' e ' + str (NUM_FINAL) + '.')
    print('Você tem ' + str(NUM_TENTATIVAS) + ' tentativas. BOA SORTE!')
    print('======================================================')
    print()
    

    for tentativa in range (1, NUM_TENTATIVAS +1):
        print('Tentativa número:' + str(tentativa))
        print('Digite um Número:')
        numero = int(input())
        print()

        if numero < numero_secreto:
            print('ESTÁ ABAIXO DO NÚMERO SECRETO')
        elif numero > numero_secreto:
            print('ESTÁ ACIMA DO NÚMERO SECRETO')
        else:
            break
    if numero == numero_secreto:
        print('>>>>> Parabéns Você Acertou!!! <<<<<')
    else:
        print('>>>>>Não Foi Dessa Vez!<<<<<')  
        print()
    print('QUER JOGAR NOVAMENTE? (Digite s para sim, n para não)')
    jogar = True if input().lower() == 's' else False
print()
print('Até a Logo ')

