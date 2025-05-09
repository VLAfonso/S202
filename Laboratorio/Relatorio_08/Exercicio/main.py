from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.235.150.135:7687", "neo4j", "heat-rejection-fumes")
db.drop_all()

game_db = GameDatabase(db)

# Criar jogadores
game_db.create_player("Ana")
game_db.create_player("Breno")
game_db.create_player("Clara")
game_db.create_player("Denise")
game_db.create_player("Evandro")
game_db.create_player("Fernanda")

# Criar partidas
game_db.create_match([{"name": "Ana", "score": 87}, {"name": "Breno", "score": 72}])
game_db.create_match([{"name": "Breno", "score": 77}, {"name": "Denise", "score": 76}])
game_db.create_match([{"name": "Clara", "score": 89}, {"name": "Evandro", "score": 87},  {"name": "Fernanda", "score": 91}])
game_db.create_match([{"name": "Fernanda", "score": 88}, {"name": "Ana", "score": 79}])

# Mostrar todas as informações adicionadas

# Mostrar jogadores
print("All players:")
for p in game_db.get_players():
    print(p)

# Mostrar partidas
result = game_db.get_matchs()
matchs = []
for r in result:
    found = False
    for m in matchs:
        #Verificar se já a partida já foi adicionada
        if(r[0] == m["id"]):
            m["players"].append({"name": r[1], "score": r[2]})
            found = True
            break
    if not found:
        matchs.append({"id": r[0], "players": [{"name": r[1], "score": r[2]}], "winner": r[3]})

print("\nAll matchs:")
for m in matchs:
    print(f"Match {m['id']}")
    print("     Players:")
    for p in m["players"]:
        print(f"        Name: {p['name']} - Score: {p['score']}")
    print(f"     Winner: {m['winner']}")

# Mostrar informação de uma partida específica
print("\nSpecific match:")
print("Match 2:")
match = game_db.get_match(2)
print("     Players:")
for p in match:
    print(f"        Name: {p[0]} - Score: {p[1]}")
print(f"     Winner: {match[0][2]}")


# Mostrar histórico de partidas de um jogador
print("\nPlayer's match history:")
print("Breno:")
match_history = game_db.get_match_player("Breno")
for m in match_history:
    print(f"    Match - {m[0]}")
    print(f"        Score - {m[1]}")
    if m[2] == "Breno":
        print(f"        Winner - Yes")
    else:
        print(f"        Winner - No")

# Atualizar nome de um jogador
print("\nUpdate name Breno to Bruno")
game_db.update_player_name("Breno", "Bruno")

# Atualizar ganhador de uma partida
print("\nUpdate match 2 winner to Clara")
game_db.update_match_winner(2, "Clara")

# Excluir um jogador
print("\nDelete Ana")
game_db.delete_player("Ana")

# Excluir uma partida
print("\nDelete match 3")
game_db.delete_match(3)

# Mostrar informações atualizadas

# Mostrar jogadores
print("\nAll players:")
for p in game_db.get_players():
    print(p)

# Mostrar partidas
result = game_db.get_matchs()
matchs = []
for r in result:
    found = False
    for m in matchs:
        #Verificar se já a partida já foi adicionada
        if(r[0] == m["id"]):
            m["players"].append({"name": r[1], "score": r[2]})
            found = True
            break
    if not found:
        matchs.append({"id": r[0], "players": [{"name": r[1], "score": r[2]}], "winner": r[3]})

print("\nAll matchs:")
for m in matchs:
    print(f"Match {m['id']}")
    print("     Players:")
    for p in m["players"]:
        print(f"        Name: {p['name']} - Score: {p['score']}")
    print(f"     Winner: {m['winner']}")


# Fechando a conexão com o banco de dados
db.close()

