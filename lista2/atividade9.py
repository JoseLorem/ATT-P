class Cinema:
    def __init__(self, nome, filmes, precos):
        self.nome = nome
        self.filmes = filmes
        self.precos = precos
        self.reservas = []
        self.load_reservas()

    def mostrar_filmes(self):
        print("Filmes:")
        for i, filme in enumerate(self.filmes):
            print(f"{i+1}. {filme}")

    def mostrar_precos(self):
        print("Preços:")
        for i, preco in enumerate(self.precos):
            print(f"{i+1}. {preco:.2f} R$")

    def fazer_reserva(self, index_filme, index_preco, num_ingressos):
        filme = self.filmes[index_filme]
        preco = self.precos[index_preco]
        preco_total = preco * num_ingressos
        reserva = {"Filme": filme, "Preço": preco, "Num_Ingressos": num_ingressos, "Preço_Total": preco_total}
        self.reservas.append(reserva)
        self.save_reservas()
        print(f"Reserva feita para {num_ingressos} ingressos para {filme} por {preco:.2f} R$ cada. Preço Total: {preco_total:.2f} R$")

    def mostrar_reservas(self):
        print("Reservas:")
        for i, reserva in enumerate(self.reservas):
            print(f"{i+1}. {reserva['Filme']} - {reserva['Num_Ingressos']} ingressos - {reserva['Preço_Total']:.2f} R$")

    def save_reservas(self):
        with open("reservas.txt", "w") as f:
            for reserva in self.reservas:
                f.write(f"{reserva['Filme']},{reserva['Preço']},{reserva['Num_Ingressos']},{reserva['Preço_Total']}\n")

    def load_reservas(self):
        try:
            with open("reservas.txt", "r") as f:
                for line in f:
                    filme, preco, num_ingressos, preco_total = line.strip().split(",")
                    reserva = {"Filme": filme, "Preço": float(preco), "Num_Ingressos": int(num_ingressos), "Preço_Total": float(preco_total)}
                    self.reservas.append(reserva)
        except FileNotFoundError:
            pass

cinema = Cinema("Meu Cinema", ["Filme 1", "Filme 2", "Filme 3"], [10.0, 15.0, 20.0])

while True:
    print("1. Mostrar Filmes")
    print("2. Mostrar Preços")
    print("3. Fazer Reserva")
    print("4. Mostrar Reservas")
    print("5. Sair")
    escolha = input("Selecione uma opção: ")
    if escolha == "1":
        cinema.mostrar_filmes()
    elif escolha == "2":
        cinema.mostrar_precos()
    elif escolha == "3":
        index_filme = int(input("Selecione o índice do filme: ")) - 1
        index_preco = int(input("Selecione o índice do preço: ")) - 1
        num_ingressos = int(input("Selecione o número de ingressos: "))
        cinema.fazer_reserva(index_filme, index_preco, num_ingressos)
    elif escolha == "4":
        cinema.mostrar_reservas()
    elif escolha == "5":
        break
    else:
        print("Opção inválida.")