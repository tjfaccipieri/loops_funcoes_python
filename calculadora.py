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

def multiplicacao(numero1, numero2):
  resultado = numero1 * numero2
  print('A multiplicação dos numeros é: ', resultado)
  pass

# opções de validar a divisão por zero
# if numerodigitado == 0:
  # print('não divida por zero, por favor')

  # fazer com tratativa de erro
  # try/catch => sempre vou tentar executar a função do try (try/except)
  # porem, se o códgo do try der erro, eu consigo pegar esse erro e tratar

def divisao(numeroUsuario):
  # try:
  #   resultado = numeroAleatorio / int(numeroUsuario) 
  #   # 150/0 => cannot divide by zero
  #   print('A divisão dos numeros é: ', resultado)
  # except ZeroDivisionError:
  #   print('Não é possivel dividir por zero')
  #   pass

  # pass
  if (int(numeroUsuario) == 0):
    print('ai não neh')
  else:
    resultado = numeroAleatorio / int(numeroUsuario)
    print('A divisão dos numeros é: ', resultado)
    
  pass

continuar = True
while continuar == True:
  print("Bem vindo a melhor calculadora do mundo, escolha sua opção:")
  print('''Operações disponiveis:
    [ 1 ] Soma
    [ 2 ] Subtração
    [ 3 ] Multiplicação
    [ 4 ] Divisão
    [ 0 ] Sair do programa''')
  opcao = int(input('Escolha sua opção: '))
  if opcao == 1:
    numero = input('Qual numero você quer somar?')
    soma(numero)
  elif opcao == 2:
    numero = input('Qual numero você quer subtrair?')
    subtracao(numero)
  elif opcao == 3:
    numero1 = int(input('Qual numero você quer multiplicar? '))
    numero2 = int(input('Por qual numero você quer multiplicar? '))
    multiplicacao(numero1, numero2)
  elif opcao == 4:
    numero = input('Qual numero você quer dividir?')
    divisao(numero)
  elif opcao == 0:
    print('Valeu, falow')
    continuar = False
