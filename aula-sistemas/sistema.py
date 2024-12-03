import os
import subprocess

def new_user():
  confirm = 'N'
  while confirm != 'Y':
    username = input('Insira o nome do novo usuário: ')
    print('Usar o nome de usuário "' + username + '"? (Y/N)')
    confirm = input().upper()
  os.system('sudo adduser ' + username)
  print('Usuario ' + username + ' criado com sucesso')


# versão com subprocess:
def new_user_subprocess():
  confirm = 'N'
  while confirm != 'Y':
    username = input('Insira o nome do novo usuário: ')
    print(f'Usar o nome de usuário "{username}"? (Y/N)')
    confirm = input().upper()
  
  try:
    # Executa o comando 'sudo adduser' com subprocess
    subprocess.run(['sudo', 'adduser', username], check=True)
    print(f'Usuário "{username}" criado com sucesso.')
  except subprocess.CalledProcessError as e:
    print(f'Erro ao criar o usuário "{username}": {e}')
  except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}')

def update_clean_system():
  escolha = ''
  while escolha != 'A' and escolha != "L":
    print('O que você deseja executar? A - Atualização / L - Limpeza')
    escolha = input().upper()
  
  if(escolha == "A"):
    #os.system('sudo yum update && sudo yum upgrade -y')
    subprocess.run(['sudo','yum','update'])
    subprocess.run(['sudo','yum','upgrade','-y'])
    #metodo "gambiarra" não indicado, maaaas, funciona
    #subprocess.run('sudo yum update && sudo yum upgrade -y', shell=True)
    print('Seu sistema está atualizado')
  elif(escolha == 'L'):
    #os.system('sudo yum autoremove && sudo yum clean all')
    subprocess.run(['sudo','yum','autoremove'])
    subprocess.run(['sudo','yum','clean','all'])
    print('Seu sistema está limpinho')