#importar librerias
from flask import Flask, render_template, request, url_for
from datetime import date

today = date.today() 

#crearmos nuestra aplicación 
app = Flask(__name__)

@app.route('/')
def index ():
    return render_template(
        'index.html',
        date = today.year
    )

@app.route('/home')
def home ():
    return render_template(
        'home.html',
        user = 'Luis',
    )

#correr aplicación
if __name__ == '__main__':
    app.run(debug=True, port=3000)