from flask import Flask
#from flask_pymongo import PyMongo

#Criando o objeto de aplicativo Flask
app = Flask(__name__)

#Criando a conexão com o DB
#mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/Acoes")
#db = mongodb_client.db

@app.route('/')
def index():
    return 'index page'




if __name__ == '__main__':
    app.run(debug=True)



