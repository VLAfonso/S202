from database import Database
from helper.writeAJson import writeAJson
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
# db.resetDatabase()

# Criar analisador de produtos
product_analyzer = ProductAnalyzer(db)

# Total de vendas por dia
product_analyzer.totalVendas()

# Produto mais vendido por compra
product_analyzer.maisVendido()

# Cliente mais gastou em uma única compra
product_analyzer.clienteMaisGastou()

# Produtos vendidos em mais de 1 quantidade
product_analyzer.produtosMaisDeUm()