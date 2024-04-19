#Base de datos

user_list = [
    {
        "username" : 'asd',
        "password" : '123'
    }
]


#Registro

def register(BD):
    print('Ingrese sus datos para registrarse.')

    while(True):

        user_register = input('Ingrese un Usuario: ')
        password_register = input('Ingrese una contraseña: ')

        for u in BD:
            if u["username"] == user_register:
                print('El usuario ya existe.')
                break
        else:  
            user = dict()
            user["username"] = user_register
            user["password"] = password_register
            user_list.append(user)
            return print('Usuario Creado')

register(user_list)


#Login

def login(BD):
    print('Ingrese sus datos para loguearse.')

    while(True):

        user_login = input('Ingrese un Usuario: ')
        password_login = input('Ingrese una contraseña: ')

        for u in BD:
            if u["username"] == user_login and u["password"] == password_login:
                return print(f"Bienvenido {user_login}! Te has logueado correctamente.")
        else:
            print('El usuario o la contraseña son incorrecntos, intente de nuevo.')

login(user_list)


#Leer base de datos

def bd_info(BD):
    print(f'La información almacenada en la base de datos es: \n{BD}')

bd_info(user_list)