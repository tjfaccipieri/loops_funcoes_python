import os

arquivos = os.listdir('c:/')

# print(arquivos)

arquivo = open('arquivo.txt', 'w')
arquivo.write('Texto bonito pro teste')
arquivo.close()

os.system('dir c:')

os.mkdir('teste')
