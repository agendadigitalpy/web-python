
from flask import Flask, request, render_template, send_from_directory
from flask import Response
from flask_pymongo import PyMongo, ASCENDING, DESCENDING
from bson.objectid import ObjectId
from forms import ProposalForm

from bs4 import BeautifulSoup


app = Flask(__name__,  static_url_path='')
app.secret_key = 'top secret'

app.config["MONGO_URI"] = "mongodb://localhost:27017/agendadigitalpy"
mongo = PyMongo(app)

@app.route('/assets/<path:path>')
def send_assets(path):
	return send_from_directory('assets', path)

@app.route('/')
def index():
    return render_template('principal.html')
	

@app.route("/propuestas/<_id>")
def show_proposal(_id):
    proposal = mongo.db.proposals.find_one({'_id': ObjectId(_id)})
    return render_template("propuesta.html", proposal=proposal)

@app.route('/propuestas', methods = ['POST','GET'])
def getProps():
    form = ProposalForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
                category = int(form.category.data)
                if category > 4:
                        category = 0
        except ValueError:
                category = 0

        title = form.title.data
        content = form.content.data
        p = {
                'name': form.name.data,
                'email': form.email.data,
                'category': category,
                'title': form.title.data,
                'content': form.content.data,
                'approved': True
            }
        mongo.db.proposals.insert(p)
        proposals = mongo.db.proposals.find().sort('_id', DESCENDING)
        return render_template("propuestas.html", proposals=proposals, form=form, success=True)

    proposals = mongo.db.proposals.find().sort('_id', DESCENDING)
    return render_template("propuestas.html", proposals=proposals, form=form)

# TODO: validar e-mail
"""@app.route('/propuestas', methods = ['POST'])
def createProposal():
    if form.validate():
        name = form.name.data
        email = form.email.data
        category = form.category.data
        try:
                category = int(category)
                if category > 4:
                        category = 0
        except ValueError:
                category = 0

        title = form.title.data
        content = form.content.data
        p = {
                'name': name,
                'email': email,
                'category': category,
                'title': title,
                'content': content,
                'approved': True
            }
        mongo.db.proposals.insert(p)
        proposals = mongo.db.proposals.find().sort('_id', DESCENDING)
        return render_template("propuestas.html", proposals=proposals, success=True)
"""
def remove_html(s):
        soup = BeautifulSoup(s)
        return soup.get_text()

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

cats = ['General', 'Gobierno Digital', 'Economía Digital', 'Conectividad', 'Fortalecimiento Institucional']
@app.template_filter('category_name')
def category_name(n):
        return cats[n]

@app.template_filter('proposal_date')
def proposal_date(i):
        return i.generation_time.strftime('%d/%m/%y')

@app.template_filter('content_filter')
def content_filter(s):
        s = s.replace("\n", "<br/>")
        return s

if __name__ == '__main__':
	app.run(debug = True)
