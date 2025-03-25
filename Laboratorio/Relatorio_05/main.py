from database import Database
from writeAJson import writeAJson
from bookModel import BookModel
from cli import BookCLI

db = Database(database="relatorio_05", collection="Livros")
bookModel = BookModel(database=db)
#db.resetDatabase()

bookCLI = BookCLI(bookModel)
bookCLI.run()