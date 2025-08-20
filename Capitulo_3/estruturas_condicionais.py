MAIOR_IDADE = 18

def verificar_idade(idade):
    if idade >= MAIOR_IDADE:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."
    
# Exemplo de uso
if __name__ == "__main__":
    idade_usuario = int(input("Digite sua idade: "))
    resultado = verificar_idade(idade_usuario)
    print(resultado)

# Capítulo 3: Estruturas Condicionais
# Este código verifica se uma pessoa é maior de idade ou não, baseado na constante MAIOR_IDADE.
# Definindo a constante para maioridade
# A função verificar_idade recebe a idade e retorna uma mensagem apropriada.# 
# O bloco if __name__ == "__main__": permite que o código seja executado diretamente.
# # O usuário é solicitado a inserir sua idade, e o resultado é impresso na tela.
#    
