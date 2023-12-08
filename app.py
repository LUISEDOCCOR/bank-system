#importar librerias
from flask import Flask, render_template, request, url_for, session, redirect
import utils.server_date as server_date
import utils.database as db
import json


def createSession (id, name, email, template):
    user = {
        'id': id,
        'name': name,
        'email': email
    }
    user = json.dumps(user)
    session["user"] = user
    return redirect(url_for(template))

def verifySession ():
    user = json.loads(session['user'])
    print(user)
    return redirect(url_for('home'))
    
#crearmos nuestra aplicación 
app = Flask(__name__)

app.secret_key = '12345'

@app.route('/')
def index ():
    return render_template(
        'index.html',
        date = server_date.year()
    )

@app.route('/home')
def home ():
    mode = None
    msg = None
    
    #Si no existe el usuario regresamos a signup
    
    if not ('user' in session):
        return redirect('signup')
    
    return render_template(
        'home.html',
        user = session["user"],
    )

@app.route('/signup', methods = ['GET', 'POST'])
def signup ():
    
    if 'user' in session:
        return verifySession() 
    
    msg = None
    mode = None    
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        msg, mode = db.createUser(name, email, password)
        if mode == 'success':
            return createSession(1, name, email, 'home')
    
    return render_template(
        'auth/auth.html',
        type = 'signup',
        msg = msg,
        mode = mode
    )

@app.route('/login', methods = ['GET', 'POST'])
def login ():
    
    if 'user' in session:
        return verifySession() 
    
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