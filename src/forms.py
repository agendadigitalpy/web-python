from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms import validators, ValidationError

class ProposalForm(Form):
	name = TextField('Nombre',[validators.Required("Por favor ingresa tu nombre")], description="Nombre")
	email = EmailField("Email",[validators.Required("Por ingresa una direccion de correo valida."), validators.Email("Ingresa tu correo")], description="Correo Electrónico")
	category = SelectField('Seleccioná un componente', choices = [('0', 'General / Sin componente específico'),
		('1', 'Gobierno Digital'),
		('2', 'Economía Digital'),
		('3', 'Conectividad'),
		('4', 'Fortalecimiento Institucional')]
	)
	title = TextField('Título', [validators.Required("Por favor ingresa un título")], description="Título de tu propuesta, ejemplo: Sugerencia para el producto 15")
	content = TextAreaField('Descripción', [validators.Required("Por favor ingresa descripción de tu propuesta.")], description="Escribí aquí tu propuesta")
	submit = SubmitField('Enviar')
	