from random import randint

def jogoAdivinhacao():
    print("Bem-vindo(a) ao jogo de Adivinhação!")
    print("Tente adivinha o número secreto entre 1 e 100.")

    numero_aleatorio = randint(1, 100)
    tentativas = 0

    while True:
        try:
            numero = int(input("Digite um número entre 1 e 100: "))
            tentativas += 1
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue
    
        if numero < numero_aleatorio:
            print("O numero aleatorio é maior.")
        elif numero > numero_aleatorio:
            print("O número aleatorio é menor.")
        else:
            print(f"Você ganhou o número aleatorio é: {numero_aleatorio}")
            print(f"Tentativas usadas: {tentativas}")
            break

jogoAdivinhacao()
