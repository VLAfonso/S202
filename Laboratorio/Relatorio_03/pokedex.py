from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database ):
        self._database = database   
    
    # Buscar pokemon pelo número
    def getPokemonByNum(self, num: str):
        pokemon = self._database.collection.find({"num": num})
        nome = "pokemon"+num
        writeAJson(pokemon, nome)

    # Buscar pokemons pelo num de evoluções
    def getPokemonByNumNextEvolution(self, num: int):
        pokemons = self._database.collection.find({"next_evolution": {"$size": num}})
        nome = "pokemons_"+str(num)+"_evolucoes"
        writeAJson(pokemons, nome)

    # Buscar pokemons com mais de determinado num doces
    def getPokemonByCandy(self, num: int):
        pokemons = self._database.collection.find({"candy_count": {"$gt": num}})
        nome = "pokemons_mais_de_"+str(num)+"_doces"
        writeAJson(pokemons, nome)
    
    # Buscar pokemons pela evolução anterior
    def getPokemonByPrevEvolution(self, name: str):
        pokemon = self._database.collection.find({"prev_evolution.name": name})
        nome = "pokemons_anteriores_a_"+name
        writeAJson(pokemon, nome)
    
    # Buscar pokemons pela inicial
    def getPokemonByInitial(self, initial: str):
        pokemon = self._database.collection.find({"name":{"$regex":f"^{initial}"}})
        nome = "pokemons_inicial_"+initial
        writeAJson(pokemon, nome)