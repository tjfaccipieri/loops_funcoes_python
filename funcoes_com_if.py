#definindo funções básicas

def divisao(number):
    resposta = number / 2
    print(resposta)
    pass

def qlquercoisa():
    print('Oi')


qlquercoisa()
divisao(8)
divisao(18)
divisao(15)
qlquercoisa()

##################################Função riada em aula####################################
def darOi():
    #recebe o nome do usuário pelo terminal
    nome = input("Digite o seu nome, por favor, ó grande usuário: ")
    
    #if básico para verificar o nome
    # if (nome == 'Willian' or nome =='Andrew'):
    #     print('Oi ' + nome + ' não me hackeie')
    # else:
    #     print("Oi " + nome)
    
    #If para verificar o nome com base em uma lista
    if nome in ('Willian', 'Andrew', 'Thiago', 'Rodolfo'):
        print('Oi ' + nome + ' não me hackeie')
    elif nome in ('Lari', 'Nic', 'Jacque', 'Demetryus'):
        print('Oi ' + nome + ' larga o java, pls')
    else:
        print("Oi " + nome)

#chamar a função
darOi()