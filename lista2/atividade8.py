class CalculadoraIMC:
    def calcular_imc(self, peso, altura):
        if peso <= 0 or altura <= 0:
            return None
        altura_m = altura / 100
        try:
            imc = peso / (altura_m ** 2)
        except ZeroDivisionError:
            return None
        return imc

calculadora = CalculadoraIMC()

while True:
    peso_str = input("Digite o seu peso em kg: ")
    try:
        peso = float(peso_str)
    except ValueError:
        print("Por favor, insira um valor numérico para o peso.")
        continue
    if peso <= 0:
        print("Por favor, insira um valor positivo para o peso.")
        continue
    altura_str = input("Digite a sua altura em cm: ")
    try:
        altura = float(altura_str)
    except ValueError:
        print("Por favor, insira um valor numérico para a altura.")
        continue
    if altura <= 0:
        print("Por favor, insira um valor positivo para a altura.")
        continue
    imc = calculadora.calcular_imc(peso, altura)
    if imc is None:
        print("Não foi possível calcular o IMC.")
    else:
        print(f"O seu IMC é {imc:.2f}")
        if imc < 18.5:
            print("Você está abaixo do peso.")
        elif imc < 25:
            print("Você está com o peso normal.")
        elif imc < 30:
            print("Você está acima do peso.")
        else:
            print("Você está obeso.")
    break