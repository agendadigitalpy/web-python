FROM tiangolo/meinheld-gunicorn-flask:python3.7
COPY ./app /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
