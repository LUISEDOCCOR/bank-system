from io import open
import pathlib
import json  

route = str(pathlib.Path().absolute()) + '/data.json'


def getData ():
  with open(route, 'r') as file:
        data = json.load(file)
        return data


def verifyEmail (email):
    data = getData()
    emailList = []
    for user in data:
        emailList.append(user['email']) 
    if not (email in emailList):
        return True           
    else: 
        return False

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
        
    



    




