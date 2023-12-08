from io import open
import pathlib
import json 
import bcrypt 
import base64
from utils.verifyData import verfuDataUser 

#obtener ruta de nuestro json 
route = str(pathlib.Path().absolute()) + '/users.json'

#obtener infomacion de nuestro json
def getData ():
  with open(route, 'r') as file:
        data = json.load(file)
        return data

#obtener id 
def id():
  data = getData()  
  return  len(data) + 1

#verificar email
def verifyEmail (email):
    data = getData()
    emailList = []
    for user in data:
        emailList.append(user['email']) 
    if not (email in emailList):
        return True           
    else: 
        return False

#verificar contraseña
def verifyPassword (email, password):
    users = getData()
    for user in users:
        if user["email"] == email:
            currentPassword = base64.b64decode(user["password"])
            if bcrypt.checkpw(password.encode('utf-8'), currentPassword):
                return True
                
            else:
                return False
                
                    
#Crear de usuario => SignUp
def createUser(name, email, password):
    try:
        if(verfuDataUser(name, email, password)):
            
            if verifyEmail(email):
                salt = bcrypt.gensalt()
                passwordHash = bcrypt.hashpw(password.encode('utf-8'), salt)
                passwordHash = base64.b64encode(passwordHash).decode('utf-8')
                
                user_data = {
                    'id': id(),    
                    'name': name,
                    'email': email,
                    'password': passwordHash
                }
                
                data = getData()
            
                data.append(user_data)

                with open(route, 'w') as file:
                    json.dump(data, file, indent=1)
                    
                return 'Account created successfully', 'success'   
            else:
                return 'That email is in use', 'danger'
            
            
        else: return 'The information provided is invalid, check the data entered', 'danger'
            
    except:
        return 'error in the system', 'warning'

#verificacion de usuario => Login        
def verifyUser (email, password):
    try:
        if verfuDataUser('login-name', email, password):
            #se usa not porque esta funcion al no encontar un correo regresa false
            if not(verifyEmail(email)) and verifyPassword(email, password):
                return 'Successful login', 'success'
            else:
                return 'wrong password or username', 'danger'
        else:
            return 'The information provided is invalid, check the data entered', 'danger'    
    except:
        return 'error in the system', 'warning'



    




