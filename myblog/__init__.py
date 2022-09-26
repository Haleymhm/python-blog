from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Cargar las configuraciones
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

#Importar vistas 
from myblog.views.auth import auth
app.register_blueprint(auth)

db.create_all