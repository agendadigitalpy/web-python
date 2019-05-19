
from flask import Flask, render_template, send_from_directory
from flask import Response
from flask_pymongo import PyMongo

app = Flask(__name__,  static_url_path='')

# Estructura de datos actual.
# p = {
#     "name" : "Matías Insaurralde",
#     "email" : "matias@insaurral.de",
#     "category" : 1,
#     "title" : "Expandir modelo de evaluación del producto 7",
#     "content" : "Hola, me parece que la forma en que se propone medir el producto 7 es poco clara.\r\n\r\nSería bueno que se revele mayor documentación sobre la implementación y se detalle la metodología del informe de progreso.\r\n\r\nSaludos",
#     "approved" : True
# }

app.config["MONGO_URI"] = "mongodb://localhost:27017/agendadigital"
mongo = PyMongo(app)

@app.route('/assets/<path:path>')
def send_assets(path):
	return send_from_directory('assets', path)

@app.route('/')
def index():
	return render_template('principal.html')
	
@app.route('/propuestas')
def getProps():
	propuestas = mongo.db.proposals.find()
	return render_template("propuestas.html", propuestas=propuestas)

@app.route('/conectividad')
def getConectividad():
	return render_template("conectividad.html")

@app.route('/documentación')
def getDocumentacion():
	return render_template("documentación.html")

@app.route('/economia-digital')
def getEconomia_Digital():
	return render_template("economia-digital.html")

@app.route('/fortalecimiento-institucional')
def getFortalecimieto_digital():
	return render_template("fortalecimiento-institucional.html")

@app.route('/gobierno-digital')
def getGobierno_digital():
	return render_template("gobierno-digital.html")

@app.route('/seguimiento')
def getSeguimiento():
	return render_template("seguimiento.html")

@app.route('/solicitudes')
def getSolicitudes():
	return render_template("solicitudes.html")



if __name__ == '__main__':
	app.run(debug = True)
