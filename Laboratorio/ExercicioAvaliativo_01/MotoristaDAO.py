from pymongo import MongoClient
from bson.objectid import ObjectId
from Motorista import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista: Motorista):
        dados_corridas = []
        for corrida in motorista.corridas:
            dados_passageiro = {'nome': corrida.passageiro.nome, 'documento': corrida.passageiro.documento}
            dados_corridas.append({'nota': corrida.nota, 'distancia': corrida.distancia, 'valor': corrida.valor, 'passageiro': dados_passageiro})

        try:
            res = self.db.collection.insert_one({"nota": motorista.nota, "corridas": dados_corridas})
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro na criação do motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro na leitura do motorista: {e}")
            return None

    def update_motorista(self, id: str, motorista: Motorista):
        dados_corridas = []
        for corrida in motorista.corridas:
            dados_passageiro = {'nome': corrida.passageiro.nome, 'documento': corrida.passageiro.documento}
            dados_corridas.append({'nota': corrida.nota, 'distancia': corrida.distancia, 'valor': corrida.valor, 'passageiro': dados_passageiro})

        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": motorista.nota, "corridas": dados_corridas}})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro na atualização do motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletedo: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro na deleção do motorista: {e}")
            return None