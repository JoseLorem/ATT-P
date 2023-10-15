import json

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def add_task(self, task):
        if task.strip() == "":
            return False
        self.tasks.append({"description": task, "completed": False})
        self.save_tasks()
        return True

    def list_tasks(self):
        if len(self.tasks) == 0:
            print("Não há tarefas na lista.")
        else:
            for i, task in enumerate(self.tasks):
                status = "X" if task["completed"] else " "
                print(f"{i+1}. [{status}] {task['description']}")

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            return False
        self.tasks[index]["completed"] = True
        self.save_tasks()
        return True

    def remove_task(self, index):
        if index < 0 or index >= len(self.tasks):
            return False
        del self.tasks[index]
        self.save_tasks()
        return True

    def save_tasks(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.tasks, f)
        except:
            print("Não foi possível salvar as tarefas.")

manager = TaskManager("tasks.json")

while True:
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Completar Tarefa")
    print("4. Remover Tarefa")
    print("5. Sair")

    choice = input("Selecione sua escolha: ")

    if choice == "1":
        task = input("Selecione a descrição da tarefa: ")
        if not manager.add_task(task):
            print("Descrição inválida.")
    elif choice == "2":
        manager.list_tasks()
    elif choice == "3":
        index = int(input("Selecione o índice da Tarefa: ")) - 1
        if not manager.complete_task(index):
            print("Índice inválido.")
    elif choice == "4":
        index = int(input("Selecione o índice da Tarefa: ")) - 1
        if not manager.remove_task(index):
            print("Índice inválido.")
    elif choice == "5":
        break
    else:
        print("Opção Inválida.")