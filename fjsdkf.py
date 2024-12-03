
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Encontrar números primos entre 1 e 250
prime_numbers = find_primes(1, 250)

# Salvar resultados em arquivo
with open('resultados.txt', 'w') as file:
    file.write("Números primos entre 1 e 250:\n")
    for prime in prime_numbers:
        file.write(str(prime) + "\n")

# Imprimir números primos na tela
print("Números primos entre 1 e 250:")
for prime in prime_numbers:
    print(prime)

print("\nOs resultados foram salvos em results.txt")
