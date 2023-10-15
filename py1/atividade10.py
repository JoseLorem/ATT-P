print("informe seu genero, M para masculino e F para feminino")

valor = str(input("resposta: "))
valor_final = valor.upper()

if valor_final == "M":
    print("masculino")
elif valor_final == "F": 
    print("feminino")
else: 
    ("invalido")