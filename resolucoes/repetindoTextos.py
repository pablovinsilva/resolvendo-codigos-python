# Solicita a entrada do usuário
texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Repete a string o número de vezes informado
resultado = " ".join([texto] * numero)

# Exibe o resultado
print("Resultado:", resultado)

