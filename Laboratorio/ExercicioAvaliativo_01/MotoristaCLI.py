from Corrida import Corrida
from Passageiro import Passageiro
from Motorista import Motorista

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("\nEntre com um comando: ")
            if command == "sair":
                print("Fim!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command("criar", self.create_motorista)
        self.add_command("ler", self.read_motorista)
        self.add_command("atualizar", self.update_motorista)
        self.add_command("deletar", self.delete_motorista)

    def create_motorista(self):
        # Verificar se serão adicionadas corridas
        haCorridas = True
        while True:
            status = input('\nAdicionar uma corrida? (sim/não) ')
            if status in ['sim', 'não']:
                break
            else:
                print("Comando inválido. Tente novamente.")
        if status == 'não':
            haCorridas = False

        # Criar corridas
        corridas = []
        while haCorridas:
            # Criar passageiro
            print('\nInformações do passageiro da corrida: ')
            p_nome = input('Entre com o nome: ')
            p_documento = input('Entre com o documento: ')
            passageiro = Passageiro(p_nome, p_documento)

            # Criar corrida
            print('\nInformações da corrida: ')
            c_nota = int(input('Entre com a nota: '))
            c_distancia = float(input('Entre com a distância: '))
            c_valor = float(input('Entre com o valor: '))
            corridas.append(Corrida(c_nota, c_distancia, c_valor, passageiro))

            # Verificar se há mais corridas
            while True:
                status = input('\nAdicionar mais uma corrida? (sim/não) ')
                if status in ['sim', 'não']:
                    break
                else:
                    print("Comando inválido. Tente novamente.")
            if status == 'não':
                break

        # Criar motorista
        print('\nInformações do motorista: ')
        m_nota = int(input('Entre com a nota: '))
        self.motoristaDAO.create_motorista(Motorista(m_nota, corridas))

    def read_motorista(self):
        id = input("\nEntre com o id: ")
        motorista = self.motoristaDAO.read_motorista_by_id(id)
        if motorista:
            print(f"Nota: {motorista['nota']}")
            if len(motorista['corridas']) > 0:
                print("Corridas:")
                for i in range(len(motorista['corridas'])):
                    corrida = motorista['corridas'][i]
                    print(f"Corrida {i+1}:")
                    print(f"    Nota: {corrida['nota']}")
                    print(f"    Distância: {corrida['distancia']}")
                    print(f"    Valor: {corrida['valor']}")
                    print("    Passageiro:")
                    print(f"        Nome: {corrida['passageiro']['nome']}")
                    print(f"        Documento: {corrida['passageiro']['documento']}")
            else:
                print('Não há corridas.')
            

    def update_motorista(self):
        id = input("\nEntre com o id: ")

        # Verificar se serão adicionadas corridas
        haCorridas = True
        while True:
            status = input('\nAdicionar uma nova corrida? (sim/não) ')
            if status in ['sim', 'não']:
                break
            else:
                print("Comando inválido. Tente novamente.")
        if status == 'não':
            haCorridas = False
        else:
            print('Entre com as novas corridas: ')
            
        # Criar corridas
        corridas = []
        while haCorridas:
            # Criar passageiro
            print('\nNovas informações do passageiro da corrida: ')
            p_nome = input('Entre com o novo nome: ')
            p_documento = input('Entre com o novo documento: ')
            passageiro = Passageiro(p_nome, p_documento)

            # Criar corrida
            print('\nNovas informações da corrida: ')
            c_nota = int(input('Entre com a nova nota: '))
            c_distancia = float(input('Entre com a nova distância: '))
            c_valor = float(input('Entre com o novo valor: '))
            corridas.append(Corrida(c_nota, c_distancia, c_valor, passageiro))

            # Verificar se há mais corridas
            while True:
                status = input('\nAdicionar mais uma nova corrida? (sim/não) ')
                if status in ['sim', 'não']:
                    break
                else:
                    print("Comando inválido. Tente novamente.")
            if status == 'não':
                break

        # Criar motorista
        print('\nNovas informações do motorista: ')
        m_nota = int(input('Entre com a nova nota: '))

        self.motoristaDAO.update_motorista(id, Motorista(m_nota, corridas))

    def delete_motorista(self):
        id = input("\nEntre com o id: ")
        self.motoristaDAO.delete_motorista(id)
        
    def run(self):
        print("Bem-vindo ao CLI do motorista!")
        print("Comandos disponíveis: criar, ler, atualizar, deletar, sair")
        super().run()
        