'''
  Script desenvolvido na maior boa vontade por: Thiago Faccipieri
  Utilizado para as aulas de Paitu do bootcamp Generation AWS Re/Start
  Novembro-2024 :)

  Utilização desse script: Realizar o calculo da base da insulina humana de acordo com as regras do lab (Aba 11)
'''

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

#Criando a lista de pesos moleculares com base no lab.
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 

#Contabilizando o numero de cada aminoácido na insulina humana
aaCountInsulin = ({x: float(insulinaAB.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']}) 

#Calculando o peso molecular total da insulina humana
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())

#Exibindo o peso molecular total da insulina humana
print("O peso molecular total da insulina humana é: " + str(molecularWeightInsulin))

#Taxa de variação/erro
molecularWeightInsulinActual = 5807.63
print("A taxa de variação entre o peso molecular total da insulina humana e o peso molecular total da insulina humana é: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100) + "%")

#versão melhorada do print acima
variation_rate = ((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100
print(f"Taxa de variação do peso molecular: {variation_rate:.2f}%")
