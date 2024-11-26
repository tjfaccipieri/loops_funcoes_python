#usar uma estrutura de FOR para printar valores e tipos

#criação da lista
listinha = [45, 290578, 1.02, True, "Texto bonitinho aqui.", "45"]

#criação do FOR para printar tudo
for item in listinha:
    print("{} é um dado do tipo {}".format(item, type(item)))