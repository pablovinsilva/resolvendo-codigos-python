# Solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Escolha da operação
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero."
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("Resultado:", resultado)

