from flask import Flask
from controllers.controlador import mutant_blueprint
from database.db_connection import engine
from models.dna_model import Base

app = Flask(__name__)


app.register_blueprint(mutant_blueprint)


Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)
