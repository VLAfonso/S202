class TeacherDatabase:
    def __init__(self, database):
        self.db = database
    
    # Buscar professor pelo nome
    def get_teacher_name(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(result["ano_nasc"], result["cpf"]) for result in results]
    
    # Buscar professor pela inicial
    def get_teacher_initial(self, inicial):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH $inicial RETURN t.name AS name, t.cpf AS cpf"
        parameters = {"inicial": inicial}
        results = self.db.execute_query(query, parameters)
        return [(result["name"], result["cpf"]) for result in results]
    
    # Buscar nome de todas as cidades
    def get_city(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        results = self.db.execute_query(query)
        return [(result["name"]) for result in results]
    
    # Buscar escola por uma faixa de valores do seu número
    def get_school(self, minimo, maximo):
        query = "MATCH (s:School) WHERE s.number >= $minimo AND s.number <= $maximo RETURN s.name AS name, s.address AS address, s.number AS number"
        parameters = {"minimo": minimo, "maximo": maximo}
        results = self.db.execute_query(query, parameters)
        return [(result["name"], result["address"], result["number"]) for result in results]
    
    # Buscar professor mais jovem e mais velho
    def get_teacher_age(self):
        query = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS jovem, MIN(t.ano_nasc) AS velho"
        results = self.db.execute_query(query)
        return (results[0]["jovem"], results[0]["velho"])

    # Buscar média dos habitantes das cidades
    def get_avg_population(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS avg_population"
        results = self.db.execute_query(query)
        return results[0]["avg_population"]

    # Buscar cidade pelo CEP e substituir "a" por "A" no nome
    def get_city_cep(self, cep):
        query = "MATCH (c:City {cep: $cep}) RETURN REPLACE(c.name, 'a', 'A') AS name"
        parameters = {"cep": cep}
        results = self.db.execute_query(query, parameters)
        return results[0]["name"]

    # Buscar 3ª letra do nome dos professores
    def get_teacher_char(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS char"
        results = self.db.execute_query(query)
        return [(result["char"]) for result in results]