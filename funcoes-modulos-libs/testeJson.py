import json

dados = {
  "nome": "Thiago",
  "idade": 38,
  "habilidades": ["Somas de 2 digitos", "Subtracao com 1 digito", "Tabuada do 5"]
}	

with open('funcoes-modulos-libs\dados.json', 'w') as arquivo:
  ## dump é para escrever o arquivo
  ## indent=4 é para deixar o arquivo mais legível, indentando ele, e é um valor opcional
  json.dump(dados, arquivo, indent=4)
  print('Arquivo JSON criado com sucesso!')

with open('funcoes-modulos-libs\dados.json', 'r') as arquivo:
  ## load é para ler o arquivo
  dados_carregados = json.load(arquivo)
  print(dados_carregados)