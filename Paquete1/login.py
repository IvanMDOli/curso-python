import json

# Función para cargar los datos desde un archivo JSON

def cargar_datos():
    try:
        with open('usuariosJson.json', 'r') as archivo:
            data = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data

# Función para guardar los datos en un archivo JSON

def guardar_datos(data):
    with open('usuarios.json', 'w') as archivo:
        json.dump(data, archivo, indent=4)

user_list = cargar_datos()

#Registro

def register(BD):
    print('\nIngrese sus datos para registrarse.\n')

    while(True):

        user_register = input('Ingrese un usuario: ')
        password_register = input('Ingrese una contraseña: ')
        password_confirm = input('Confirme la contraseña: ')

        if any(user["username"] == user_register for user in BD):
            print('El usuario ya existe.')
        else:  
            if password_register == password_confirm:
                new_user = {
                    "username": user_register,
                    "password": password_register,
                    "id": len(BD),
                    "login": False
                }
                BD.append(new_user)
                guardar_datos(BD)
                print('\nUsuario Creado\n')
                return menu(BD)
            else:
                print('\nLas contraseñas no coinciden.\n')

#Login

def login(BD):
    print('\nIngrese sus datos para loguearse.\n')

    while(True):

        user_login = input('Ingrese un Usuario: ')
        password_login = input('Ingrese una contraseña: ')

        for user in BD:
            if user["username"] == user_login and user["password"] == password_login:
                user["login"] = True
                guardar_datos(BD)
                print(f"\nBienvenido {user_login}! Te has logueado correctamente.\n")
                return menu(BD)
        else:
            print('\nEl usuario o la contraseña son incorrecntos, intente de nuevo.\n')

#Logout

def logout(BD, id):
    for user in BD:
        if user["id"] == id:
            user["login"] = False
            print(f'\nChau {user["username"]}, se ha cerrado la sesión correctamente.\n')
    return menu(BD)

#Mostrar información del usuario

def mostrar_usuario(BD, id):
    print(f'\nInformación del usuario:\n')

    for user in BD:
        if user["id"] == id:
            print(f'\nUser[{user["id"]}]: {user["username"]} - {user["password"]} - {user["login"]}\n')
    return menu(BD)

#Leer e imprimir base de datos

def bd_info(BD):
    print(f'\nLa información almacenada en la base de datos es:\n')

    with open('informacion_bd.txt', 'w') as archivo:
        archivo.write('Información almacenada en la base de datos:\n\n')
        
        for user in BD:
            info_usuario = f'User[{user["id"]}]: {user["username"]} - {user["password"]} - {user["login"]}\n'
            print(info_usuario)
            archivo.write(info_usuario)

    print("Información de la base de datos escrita en 'informacion_bd.txt'.")
    return menu(BD)

#Menu

def menu(BD):
    
    while(True):

        for user in BD:
            if user["login"] == True:
                print('[1]Mostrar usuario\n[2]Logout\n[3]Mostrar base de datos\n')
                try:
                    option = int(input('Elija una opción: '))
                except ValueError:
                    print('\nIngrese un valor númerico.\n')
                    continue
                if option == 1:
                    return mostrar_usuario(BD, user["id"])
                elif option == 2:
                    return logout(BD, user["id"])
                elif option == 3:
                    return bd_info(BD)
                else:
                    print('\nOpción inválida\n')
        else:
            print('[1]Login\n[2]Registro\n')
            try:
                option = int(input('Elija una opción: '))
            except ValueError:
                print('\nIngrese un valor númerico.\n')
                continue
            if option == 1:
                return login(BD)
            elif option == 2:
                return register(BD)
            else:
                print('\nOpción inválida\n')