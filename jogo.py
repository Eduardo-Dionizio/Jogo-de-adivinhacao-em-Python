# Importa a biblioteca
import random

# Criar função
def jogo_adivinhacao():
  # variavel que escolhe um número aleátorio entre 1 e 20
  numero_secreto = random.randint(1, 20)

  # 5 Tentativas
  tentativas = 5
  
  print("Adivinhe qual é o número secreto entre 1 e 20. Você tem 5 tentativas")

  # Loop criado enquanto as tentativas forem maior que 0
  while tentativas > 0:
    print(f"Você tem {tentativas} tentavisa(s) restante(s)!!")

    # Inserir palpite para adivinhar o número secreto
    palpite = int(input("Adivinhe o número secreto!!"))

     # Caso acerte o número, o programa é encerrado imediatamente.
    if palpite == numero_secreto:
      print(f"Parabéns!! Você acertou o número secreto: {numero_secreto}!!!")
      break
      # Caso o palpite for menor que o número secreto, dizer que é está baixo
    elif palpite < numero_secreto:
      print("Muito baixo.")
      # Caso o palpite for maior que o número secreto, dizer que está alto
    else:
      print("Muito alto.")
      
    # Número reduzido de tentativas a cada palpite errado
    tentativas -= 1

    # Este else é contraditorio ao while, quando o número de tentativas chegar a 0.
  else:
    print(f"\nSeu número de tentavivas acabou. O número secreto era: {numero_secreto}")

# Chamar a função
jogo_adivinhacao()