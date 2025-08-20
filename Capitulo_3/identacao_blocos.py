def sacar(valor, saldo):
    if valor > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= valor
        print(f"Saque de {valor} realizado com sucesso")
    return saldo

def depositar(valor, saldo):
    saldo += valor
    print(f"Depósito de {valor} realizado com sucesso")
    return saldo


saldo = 1000
print(f"Saldo inicial: {saldo}")
# Testando a função
saldo = sacar(150, saldo)
saldo = sacar(2000, saldo)

# pegar o retorno do saldo da função
saldo = sacar(300, saldo)
print(f"Saldo atualizado: {saldo}")

saldo = depositar(500, saldo)
print(f"Saldo final: {saldo}")

saldo = depositar(500, saldo)
print(f"Saldo final: {saldo}")




