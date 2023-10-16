class CaixaEletronico:

    def __init__(self):

        self.saldo = 0



    def consultar_saldo(self):

        return self.saldo



    def sacar_dinheiro(self, valor):

        if valor > 0 and valor <= self.saldo:

            self.saldo -= valor

            return f"Saque de R${valor:.2f} realizado com sucesso."

        else:

            return "Saldo insuficiente ou valor de saque inválido."



    def depositar_dinheiro(self, valor):

        if valor > 0:

            self.saldo += valor

            return f"Depósito de R${valor:.2f} realizado com sucesso."

        else:

            return "Valor de depósito inválido."



def main():

    caixa = CaixaEletronico()



    while True:

        print("1. Consultar saldo")

        print("2. Sacar dinheiro")

        print("3. Depositar dinheiro")

        print("4. Sair")



        opcao = input("Escolha uma opção: ")



        if opcao == "1":

            saldo = caixa.consultar_saldo()

            print(f"Saldo disponível: R${saldo:.2f}")

        elif opcao == "2":

            valor = float(input("Digite o valor do saque: "))

            resultado = caixa.sacar_dinheiro(valor)

            print(resultado)
        elif opcao == "3":

            valor = float(input("Digite o valor do depósito: "))

            resultado = caixa.depositar_dinheiro(valor)

            print(resultado)

        elif opcao == "4":

            print("Obrigado por usar o caixa eletrônico. Volte sempre!")

            break

        else:

            print("Opção inválida. Por favor, escolha uma opção válida.")



if __name__ == "__main__":

    main()
