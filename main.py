print("Calculadora de IMC")

nome = input("Qual é o seu nome? ")
idade = input(f"Qual sua idade? ")
peso = str(input("Qual seu peso (em KG)? ")).replace(',', '.')
altura = str(input("Qual sua Altura? ")).replace(',', '.')

# Conversão de str para float
peso = float(peso)
altura = float(altura)

# No cálculo é usado a expressão **2 para multiplicar a variável
imc = (peso / (altura ** 2))

# É acresentado 2 casa decimais com a expessão (variável:.2f) dentro da variável
print(f"seu IMC é: {imc:.2f}")

if imc < 16:
    print(f"{nome} você está com muito abaixo do peso ideal.\n Procure um especialista.")
elif imc < 18.5:
    print(f"{nome} você está abaixo do peso ideal.\n Procure um especialista.")
elif imc < 25:
    print(f"{nome} Você está Saudável.\n")
elif imc < 30:
    print(f"{nome} você está acima do peso ideal.\n")
elif imc < 35:
    print(f"{nome} você está com Obesidade Grau I\n")
elif imc < 40:
    print(f"{nome} você está com Obesidade Grau II\n")
else:
    print(f"{nome} você está com Obesidade Grau III\n")
