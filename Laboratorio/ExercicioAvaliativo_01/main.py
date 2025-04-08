from Database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

# Criar banco de dados
db = Database(database='ExercicioAvaliativo_01', collection='Motoristas')
#db.resetDatabase()

# Criar relação com banco de dados
motoristaDAO = MotoristaDAO(db)

# Criar e iniciar CLI
motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI .run()
