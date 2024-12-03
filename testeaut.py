def checkValue(valueToCheck):
  assert(type(valueToCheck) is int), 'Só vale colocar numeros'
  assert(valueToCheck > 0), 'O valor tem que ser maior que zero'
  if valueToCheck > 4:
    print("O valor foi maior que 4")
  else:
    print("Valor menor ou igual a 4")

var = int(input('Por favor, coloque um numero, na moral: '))
checkValue(var)