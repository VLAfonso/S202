from database import Database
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database: Database ):
        self._database = database

    # Total de vendas por dia
    def totalVendas(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {"$sum": "$produtos.quantidade"}}},    
            {"$sort": {"_id": 1}}
        ])

        writeAJson(result, "Total de vendas por dia")

    # Produto mais vendido por compra
    def maisVendido(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            # definir cada compra por meio do cliente e da data
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra", "produto": "$produtos.descricao"}, "quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"_id.cliente": 1,"_id.data": 1, "quantidade": -1}},
            {"$group": {"_id": {"data": "$_id.data", "cliente": "$_id.cliente"},"produto": {"$first": "$_id.produto"}}}
        ])

        writeAJson(result, "Produto mais vendido por compra")

    # Cliente mais gastou em uma única compra
    def clienteMaisGastou(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            # definir cada compra por meio do cliente e da data
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},    
            {"$sort": {"total": -1}},
            {"$limit": 1},
            {"$group": {"_id": "$_id.cliente"}}
        ])

        writeAJson(result, "Cliente mais gastou em única compra")
    
    # Produtos vendidos em mais de 1 quantidade
    def produtosMaisDeUm(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade": {"$sum": "$produtos.quantidade"}}},
            # filtrar quantidade acima de 1
            {"$match": {"quantidade": {"$gt": 1}}},
            {"$sort": {"_id": 1}}
        ])

        writeAJson(result, "Produtos acima de 1 unidade vendida")

