
from flask import Flask, render_template
from flask import Response
from flask_pymongo import PyMongo

app = Flask(__name__)

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

@app.route('/')
def index():
    return '<html><body><h1>AgendaDigital Py</h1></body></html>'


@app.route('/propuestas')
def getProps():
    propuestas = mongo.db.proposals.find()
    
    return render_template("propuestas.html", propuestas=propuestas)

    
    
    
if __name__ == '__main__':
          app.run(debug = True)
