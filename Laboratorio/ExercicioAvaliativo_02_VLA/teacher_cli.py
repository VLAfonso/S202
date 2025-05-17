class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("\nEntre com um comando: ")
            if command == "Sair":
                print("Fim!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")

class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_crud):
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("Criar", self.create_teacher)
        self.add_command("Ler", self.read_teacher)
        self.add_command("Atualizar", self.update_teacher)
        self.add_command("Deletar", self.delete_teacher)
    
    def create_teacher(self):
        name = input("Entre com o nome: ")
        ano_nasc = int(input("Entre com o ano de nascimento: "))
        cpf = input("Entre com o CPF: ")
        self.teacher_crud.create(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Entre com o nome: ")
        teacher = self.teacher_crud.read(name)
        if teacher:
            print(f"    Ano de Nascimento: {teacher[0][0]}    CPF: {teacher[0][1]}")

    def update_teacher(self):
        name = input("Entre com o nome: ")
        newCpf = input("Entre com o nome CPF: ")
        self.teacher_crud.update(name, newCpf)

    def delete_teacher(self):
        name = input("Entre com o nome: ")
        self.teacher_crud.delete(name)
        
    def run(self):
        print("Bem-vindo ao CLI do Teacher!")
        print("Comandos disponíveis: Criar, Ler, Atualizar, Deletar, Sair")
        super().run()