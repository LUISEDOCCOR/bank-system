from io import open
import pathlib
import json  

#obtener ruta de nuestro json 
route = str(pathlib.Path().absolute()) + '/data.json'


#obtener infomacion de nuestro json
def getData ():
  with open(route, 'r') as file:
        data = json.load(file)
        return data

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
    print(getData())
    for user in users:
        if user["email"] == email:
            if user["password"] == password:
                return True
                
            else:
                return False
                
                    
#Crear de usuario => SignUp
def createUser(name, email, password):
    try:
        if verifyEmail(email):
            
            user_data = {
            'name': name,
            'email': email,
            'password': password
            }
            
            data = getData()
        
            data.append(user_data)

            with open(route, 'w') as file:
                json.dump(data, file, indent=1)
                
            return 'Account created successfully', 'success'   
        
        else: return 'That email is in use', 'danger'
            
    except:
        return 'error in the system', 'warning'

#verificacion de usuario => Login        
def verifyUser (email, password):
    print(verifyPassword(email, password))
    try:
        if not(verifyEmail(email)) and verifyPassword(email, password):
            return 'Successful login', 'success'
        else:
            return 'wrong password or username', 'danger'
    except:
        return 'error in the system', 'warning'



    




