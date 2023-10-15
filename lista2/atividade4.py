class CaixaEletronico:
    def __init__(self):
        self.saldo = 0
        self.notas = {
            100: 10,
            50: 10,
            20: 10,
            10: 10
        }

    def consultar_saldo(self):
        return self.saldo

    def sacar_dinheiro(self, valor):
        notas_sacadas = {}
        for nota in sorted(self.notas.keys(), reverse=True):
            if valor >= nota and self.notas[nota] > 0:
                qtd_notas = min(valor // nota, self.notas[nota])
                notas_sacadas[nota] = qtd_notas
                valor -= nota * qtd_notas
                self.notas[nota] -= qtd_notas
        if valor == 0:
            self.saldo -= sum(notas_sacadas.keys()) * sum(notas_sacadas.values())
            return notas_sacadas
        else:
            return None

    def depositar_dinheiro(self, valor):
        self.saldo += valor

caixa = CaixaEletronico()

while True:
    print("1 - Consultar saldo")
    print("2 - Sacar dinheiro")
    print("3 - Depositar dinheiro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        saldo = caixa.consultar_saldo()
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "2":
        valor = int(input("Digite o valor a ser sacado: "))
        notas_sacadas = caixa.sacar_dinheiro(valor)
        if notas_sacadas is not None:
            print("Notas sacadas:")
            for nota, qtd in notas_sacadas.items():
                print(f"{qtd} nota(s) de R${nota}")
        else:
            print("Não foi possível sacar o valor desejado.")

    elif opcao == "3":
        valor = int(input("Digite o valor a ser depositado: "))
        caixa.depositar_dinheiro(valor)
        print("Depósito realizado com sucesso.")

    elif opcao == "4":
        print("Obrigado por utilizar o caixa eletrônico.")
        break

    else:
        print("Opção inválida.")