#dependencia de flask
from flask import Flask, render_template,url_for

#Dependencia de configuracion 
from .config import Config #El punto es para indicarle a python que los archivos estan en el mismo paquete

#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy

#dependencia de las migraciones
from flask_migrate import Migrate

#crear el objeto flask
app = Flask(__name__)

#Configuracion del objeto flask
app.config.from_object(Config)

#Importar el modulo 
from app.materiales import materiales_blueprint
from app.ordenes import ordenes_blueprint
from app.catalogo import catalogo_blueprint

#Vincular submodulos del proyecto
app.register_blueprint(materiales_blueprint)
app.register_blueprint(ordenes_blueprint)
app.register_blueprint(catalogo_blueprint)
#crear el objeto de modelos:

db=SQLAlchemy(app)
#crear el obejeto de migracion 
migrate=Migrate(app,db)





@app.route('/index')
def index():
    return render_template('index.html' )

from .models import RolUsuario,Usuario,Material,Cotizacion,OrdenServicio
