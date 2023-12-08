#importar librerias
from flask import Flask, render_template, request, url_for
import utils.server_date as server_date
import utils.database as db


#crearmos nuestra aplicación 
app = Flask(__name__)

@app.route('/')
def index ():
    return render_template(
        'index.html',
        date = server_date.year()
    )

@app.route('/home')
def home ():
    return render_template(
        'home.html',
        user = 'Luis',
    )

@app.route('/signup', methods = ['GET', 'POST'])
def signup ():
    msg = None
    mode = None    
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        msg, mode = db.createUser(name, email, password)
    
    return render_template(
        'auth/auth.html',
        type = 'signup',
        msg = msg,
        mode = mode
    )

@app.route('/login', methods = ['GET', 'POST'])
def login ():
    
    msg = None
    mode = None    
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        msg, mode = db.verifyUser(email, password)
    
    return render_template(
        'auth/auth.html', 
        type = 'login',
        msg = msg,
        mode = mode
    )   
    
    
#correr aplicación
if __name__ == '__main__':
    app.run(debug=True, port=3000)