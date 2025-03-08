from database import Database
from pokedex import Pokedex
from helper.writeAJson import writeAJson

# Criar banco de dados
db = Database(database="pokedex", collection="pokemons")

# Criar pokedex
pokedex = Pokedex(db)

# Buscar pokemon numero 018
pokedex.getPokemonByNum("018")

# Buscar pokemons com 2 evoluções
pokedex.getPokemonByNumNextEvolution(2)

# Buscar pokemons com mais de 75 doces
pokedex.getPokemonByCandy(75)

# Buscar pokemons com Eevee como evolução anterior
pokedex.getPokemonByPrevEvolution("Eevee")

# Buscar pokemons com inicial L
pokedex.getPokemonByInitial('L')