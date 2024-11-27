from random import randint

#!fazer depois: dar um jeito disso ficar dinamico (criar uma função para gerar o numero)
numeroAleatorio = randint(0, 159)

def soma(numeroUsuario):
  resultado = numeroAleatorio + int(numeroUsuario)
  print('A soma dos numeros é: ', resultado)
  pass

def subtracao(numeroUsuario):
  resultado = numeroAleatorio - int(numeroUsuario)
  print('A subtração dos numeros é: ', resultado) 
  pass

def multiplicacao():

  pass

def divisao():

  pass


# while True:
#   print("Bem vindo a melhor calculadora do mundo, escolha sua opção:")
#   print('''Operações disponiveis:
#     [ 1 ] Soma
#     [ 2 ] Subtração
#     [ 3 ] Multiplicação
#     [ 4 ] Divisão
#     [ 0 ] Sair do programa''')
#   opcao = int(input('Escolha sua opção: '))
#   if opcao == 1:
#     numero = input('Qual numero você quer somar?')
#     soma(numero)
#   elif opcao == 2:
#     numero = input('Qual numero você quer subtrair?')
#     subtracao(numero)
#   elif opcao == 0:
#     print('Valeu, falow')
#     break
