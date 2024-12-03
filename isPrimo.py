def eh_primo(numero):
    """Verifica se um número é primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def salvar_primos_em_arquivo(limite, nome_arquivo):
    """Gera números primos até um limite e salva em um arquivo."""
    primos = [numero for numero in range(1, limite + 1) if eh_primo(numero)]
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("\n".join(map(str, primos)))
    print(f"Lista de números primos salva em '{nome_arquivo}'.")

if __name__ == "__main__":
    limite = 250
    nome_arquivo = "results.txt"
    salvar_primos_em_arquivo(limite, nome_arquivo)