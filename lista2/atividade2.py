import csv

class Agenda:
    def __init__(self, filename):
        self.filename = filename
        self.contatos = []
        self.carregar_contatos()

    def adicionar_contato(self, nome, telefone):
        contato = {"nome": nome, "telefone": telefone}
        self.contatos.append(contato)
        self.salvar_contatos()
        print(f"Contato {nome} adicionado com sucesso.")

    def listar_contatos(self):
        print("Lista de contatos:")
        for i, contato in enumerate(self.contatos):
            print(f"{i+1}. {contato['nome']} - {contato['telefone']}")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato["nome"] == nome:
                print(f"Contato encontrado: {contato['nome']} - {contato['telefone']}")
                return
        print("Contato não encontrado.")

    def remover_contato(self, nome):
        for i, contato in enumerate(self.contatos):
            if contato["nome"] == nome:
                del self.contatos[i]
                self.salvar_contatos()
                print(f"Contato {nome} removido com sucesso.")
                return
        print("Contato não encontrado.")

    def carregar_contatos(self):
        try:
            with open(self.filename, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    nome, telefone = row
                    contato = {"nome": nome, "telefone": telefone}
                    self.contatos.append(contato)
        except FileNotFoundError:
            pass

    def salvar_contatos(self):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            for contato in self.contatos:
                writer.writerow([contato["nome"], contato["telefone"]])

agenda = Agenda("contatos.csv")

while True:
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato")
    print("4. Remover contato")
    print("5. Sair")

    escolha = input("Digite a opção desejada: ")
    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda.adicionar_contato(nome, telefone)

    elif escolha == "2":
        agenda.listar_contatos()
        
    elif escolha == "3":
        nome = input("Digite o nome do contato: ")
        agenda.buscar_contato(nome)
        
    elif escolha == "4":
        nome = input("Digite o nome do contato: ")
        agenda.remover_contato(nome)

    elif escolha == "5":
        break
    
    else:
        print("Opção inválida.")