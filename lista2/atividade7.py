import random
import json

class Jogodasorte:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, "r") as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = None

    def play(self):
        number = random.randint(1, 100)
        attempts = 0
        while True:
            try:
                guess = int(input("Adivinhe o número!(1-100): "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue
            attempts += 1
            if guess < number:
                print("Muito baixo. Advinhe novamente.")
            elif guess > number:
                print("Muito alto. Advinhe novamente.")
            else:
                print(f"Parabéns! Você acertou o número em {attempts} tentativas.")
                if self.high_score is None or attempts < self.high_score:
                    self.high_score = attempts
                    print("Nova maior pontuação!")
                    try:
                        with open(self.filename, "w") as f:
                            json.dump(self.high_score, f)
                    except:
                        print("Não foi possível salvar a maior pontuação.")
                break

    def show_high_score(self):
        if self.high_score is None:
            print("Sem maior pontuação até o momento.")
        else:
            print(f"A maior pontuação atual é de {self.high_score} tentativas.")

game = Jogodasorte("high_score.json")

while True:
    print("1. Jogar")
    print("2. Mostrar Ranking")
    print("3. Sair")
    choice = input("Selecione sua escolha: ")
    if choice == "1":
        game.play()
    elif choice == "2":
        game.show_high_score()
    elif choice == "3":
        break
    else:
        print("Escolha inválida.")