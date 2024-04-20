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

        for user in BD:
            if user["username"] == user_register:
                print('El usuario ya existe.')
                break
        else:  
            create_user = dict()
            create_user["username"] = user_register
            create_user["password"] = password_register
            user_list.append(create_user)
            print('Usuario Creado')
            return menu()



#Login

def login(BD):
    print('Ingrese sus datos para loguearse.')

    while(True):

        user_login = input('Ingrese un Usuario: ')
        password_login = input('Ingrese una contraseña: ')

        for user in BD:
            if user["username"] == user_login and user["password"] == password_login:
                print(f"Bienvenido {user_login}! Te has logueado correctamente.")
                return menu()
        else:
            print('El usuario o la contraseña son incorrecntos, intente de nuevo.')



#Leer base de datos

def bd_info(BD):
    print(f'La información almacenada en la base de datos es: \n{BD}')
    return menu()



#Menu

def menu():

    while(True):
        print('[1]Login\n[2]Registro\n[3]Mostrar base de datos')
        try:
            option = int(input('Elija una opción: '))
        except ValueError:
            print('Ingrese un valor númerico.')
            continue
        if option == 1:
            return login(user_list)
        elif option == 2:
            return register(user_list)
        elif option == 3:
            return bd_info(user_list)
        else:
            print('Opción inválida')
    
menu()