# web-python

Sitio web de agendadigital.com.py.

Si tenés alguna sugerencia relacionada con este proyecto, podes crear un ticket [aquí](https://github.com/agendadigitalpy/web-python/issues/new).

# Requisitos

- [Python 3](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/)

# Requisitos (Python)

- [Flask](http://flask.pocoo.org/)
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

```bash
$ pip install -r requirements.txt
```

# Desarrollo

Antes de utilizar la aplicación, crear una base de datos en MongoDB, llamada "agendadigitalpy".

## Entorno virtual

```bash
$ python3 -m venv venv
```

```bash
$ ./venv/bin/activate
```

## Ejecución

```bash
$ cd src
$ flask run
```

## Guía de instalación para macos o linux

```bash
$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt

$ cd app

$ export FLASK_APP=main.py
# ejecutar flask en debug mode
$ export FLASK_ENV=development

$ flask run
```

en **macos** al correr `flask run` es muy común el error

```bash
ModuleNotFoundError: No module named 'bs4'
```

el fix es:

```bash
# salir del virtualenv
deactivate
# instalar manualmente
python3 -m pip install bs4
```

# Comunidad

Para discutir sobre temas de desarrollo podes ingresar al Telegram de desarrollo en [este enlace](https://t.me/agendadigitalpydev).

Para temas generales relacionados a la agenda digital, [este es el canal oficial](https://t.me/agendadigitalpy).
