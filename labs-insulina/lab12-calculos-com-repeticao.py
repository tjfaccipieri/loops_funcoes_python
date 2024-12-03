'''
  Script desenvolvido na maior boa vontade por: Thiago Faccipieri
  Utilizado para as aulas de Paitu do bootcamp Generation AWS Re/Start
  Novembro-2024 :)

  Utilização desse script: Executar os calculos de insulina humana usando lists/for/while (Aba 12)
'''

# Assim como no lab anterior, o acesso nos valores separados por arquivos da Insulina serão necessários, então, copia e cola do exercicio anterior e ja era
#Recuperar o conteudo do arquivo insulina-filtrada.txt
with open('labs-insulina/insulina-filtrada.txt', 'r') as arquivo:
  conteudo = arquivo.read()
  pass

#Definir as variaveis de insulina
#insulinaA
with open('labs-insulina/aInsulin.txt', 'r') as arquivo:
  insulinaA = arquivo.read()
  pass

#insulinaB
try:
    with open('labs-insulina/bInsulin.txt', 'r') as arquivo:
        insulinaB = arquivo.read()
except FileNotFoundError:
    print("bInsulin.txt file not found")
    insulinaB = ""
    
#insulinaC
with open('labs-insulina/cInsulin.txt', 'r') as arquivo:
  insulinaC = arquivo.read()
  pass

#insulinaLS
with open('labs-insulina/lsInsulin.txt', 'r') as arquivo:
  insulinaLS = arquivo.read()
  pass

insulinaAB = insulinaA + insulinaB

#exibir os dados sobre a insulina humana no terminal
print(f'Código completo da insulina humana: {conteudo}')
print(f'Insulina A: {insulinaA}')
print(f'Insulina B: {insulinaB}')
print(f'Insulina C: {insulinaC}')
print(f'Insulina LS: {insulinaLS}')
print(f'Insulina AB: {insulinaAB}')

# criação do dict que o lab pede:
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

float(insulinaAB.count('y'))

seqCount = ({x: float(insulinaAB.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']})

pH = 0

netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))

print('{0:.2f}'.format(pH), netCharge)
pH += 1