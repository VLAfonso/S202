class GameDatabase:
    def __init__(self, database):
        self.db = database
        self.id_player = 0
        self.id_match = 0
    
    # Criar jogador
    def create_player(self, name):
        query = "CREATE (:Player {id: $id, name: $name})"
        parameters = {"name": name, "id": self.id_player}
        self.id_player += 1
        self.db.execute_query(query, parameters)
    
    # Criar partida
    def create_match(self, players): #players = [{"name": name, "score": score}]
        # Verificar vencedor
        winner = max(players, key=lambda player: player["score"])

        # Criar partida
        query = "CREATE (:Match {id: $id, winner: $winner})"
        parameters = {"id": self.id_match, "winner": winner["name"]}
        self.db.execute_query(query, parameters)

        # Adicionar jogadores
        for p in players:
            query = "MATCH (p:Player {name: $player_name}), (m:Match {id: $match_id}) CREATE (p)-[:PLAYS{score: $score}]->(m)"
            parameters = {"player_name": p["name"], "match_id": self.id_match, "score": p["score"]}
            self.db.execute_query(query, parameters)

        self.id_match += 1

    # Recuperar alunos
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    # Recuperar partidas
    def get_matchs(self):
        query = "MATCH (m:Match)<-[r:PLAYS]-(p:Player) RETURN m.id AS match_id, m.winner as winner, p.name AS player_name, r.score AS score"
        results = self.db.execute_query(query)
        return [(result["match_id"], result["player_name"], result["score"], result["winner"]) for result in results]
    
    # Recuperar partida específica
    def get_match(self, match_id):
        query = "MATCH (m:Match {id: $id})<-[r:PLAYS]-(p:Player) RETURN m.winner as winner, p.name AS player_name, r.score AS score"
        parameters = {"id": match_id}
        results = self.db.execute_query(query, parameters)
        return [(result["player_name"], result["score"], result["winner"]) for result in results]
    
    # Recuperar partidas de um jogador
    def get_match_player(self, player_name):
        query = "MATCH (m:Match)<-[r:PLAYS]-(p:Player {name: $player_name}) RETURN m.id AS match_id, m.winner as winner, r.score AS score"
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return [(result["match_id"], result["score"], result["winner"]) for result in results]
    
    # Atualizar nome do jogador
    def update_player_name(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

        query = "MATCH (m:Match {winner: $old_name}) SET m.winner = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    
    # Atualizar vencedor da partida
    def update_match_winner(self, id, new_winner):
        query = "MATCH (m:Match {id: $id}) SET m.winner = $new_winner"
        parameters = {"id": id, "new_winner": new_winner}
        self.db.execute_query(query, parameters)

    # Excluir jogador
    def delete_player(self, name):
        # Apagar informações do jogador
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

        # Alterar vencedor
        query = "MATCH (m:Match {winner: $winner})<-[r:PLAYS]-(p:Player) SET m.winner = $new_winner"
        parameters = {"winner": name, "new_winner": "No winner"}
        self.db.execute_query(query, parameters)

    # Excluir partida
    def delete_match(self, id):
        query = "MATCH (m:Match {id: $id}) DETACH DELETE m"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)