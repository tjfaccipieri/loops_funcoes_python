'''
  Script desenvolvido na maior boa vontade por: Thiago Faccipieri
  Utilizado para as aulas de Paitu do bootcamp Generation AWS Re/Start
  Novembro-2024 :)

  Utilização desse script: Preparar os arquivos necessários para o calculo da base da insulina humana com base no código completo
'''

#importando a lib para trabalhar com Regex
import re
#importanto a lib do time, pra dar uns pauses nos processos
import time

#abrindo o arquivo com a insulina original do site
with open('labs-insulina/insulina-completa.txt', 'r') as arquivoOriginal:
  try:
      linhas = arquivoOriginal.readlines()
      # print(linhas)
  except IOError as e:
      print(f"Erro ao encontrar o arquivo: {e}")

#deletando a primeira e a ultima linha do array, o que vai tirar as linhas de ORIGIN e //
del linhas[0]
del linhas[-1]

#agora, para as linhas que sobraram, remover todos os numeros e espaços em branco que existam nelas
#  modelo sem o uso do FOR, passando linha a linha manualmente
# linhas[0] = re.sub(r'[\d\s]', '', linhas[0])
# linhas[1] = re.sub(r'[\d\s]', '', linhas[1])

#feat: utilizando um laço FOR, pra caso precise filtrar um arquivo maior que esse
for item in range(len(linhas)):
  linhas[item] = re.sub(r'[\d\s]', '', linhas[item])

# outra opção que funciona com o FOR, mas que eu acho pior de entender de primeira, pq faz tudo em um unico
#? linhas = [re.sub(r'[\d\s]', '', linha) for linha in linhas]

#salvar essas linhas modificadas em um novo arquivo
with open('labs-insulina/insulina-filtrada.txt', 'w') as regexFile:
  regexFile.writelines(linhas)
  pass

#abrir o arquivo que tem a insulina ja filtrada, mas aqui ele vai abrir como um array, com o código inteiro no index[0]
with open('labs-insulina/insulina-filtrada.txt') as filtros:
  textoCompleto = filtros.readlines()
  # print(textoCompleto)
  pass

#com esse esqueminha do .join, o texto completo da insulina fica disponivel fora do array que foi criado ali em cima 
conteudo = ''.join(textoCompleto)
# print(conteudo)

'''separando as partes necessárias de acordo com o guia do Laboratório, sendo:
  - primeira parte: do inicio até o caractere 24,
  - segunda parte: do caractere 25 até o 54,
  - terceira parte: do caractere 55 até o 89,
  - quarta parte: do caractere 90 até o fim.
'''
primeiraParte = conteudo[:24]
segundaParte = conteudo[24:54]
terceiraParte = conteudo[54:89]
quartaParte = conteudo[89:110]
# salvar cada uma das partes separadas acima, em um arquivo diferente, para consultas futuras:
with open('labs-insulina/lsInsulin.txt', 'w') as primeiroFiltro:
  primeiroFiltro.write(primeiraParte)
  pass
print('Sequenciando primeira cadeia de caracteres, um momento')
time.sleep(2)
print('******************************************************')

with open('labs-insulina/bInsulin.txt', 'w') as segundoFiltro:
  segundoFiltro.write(segundaParte)
  pass
print('Sequenciando segunda cadeia de caracteres, um momento')
time.sleep(2)
print('******************************************************')

with open('labs-insulina/cInsulin.txt', 'w') as terceiroFiltro:
  terceiroFiltro.write(terceiraParte)
  pass
print('Sequenciando terceira cadeia de caracteres, um momento')
time.sleep(2)
print('******************************************************')

with open('labs-insulina/aInsulin.txt', 'w') as quartoFiltro:
  quartoFiltro.write(quartaParte)
  pass
print('Sequenciando quarta cadeia de caracteres, um momento')
time.sleep(2)
print('******************************************************')
print("Sequenciamento completo, agradecemos a utilização.")