from Paquete1.cliente import *

# Base de dato provisoria donde almacenar a los clientes
cliente_list = []

# Menu para interactuar con los módulos del cliente
def menu_cliente(BD_cliente):
    while True:

        if len(BD_cliente) == 0:
            print('\n[1] Crear cliente\n[2] Volver')

            try:
                option = int(input('Elija una opción: '))
            except ValueError:
                print('\nIngrese un valor numérico.\n')
                continue

            if option == 1:
                nombre = input('\nIngrese un nombre para el cliente: ')
                apellido = input('\nIngrese un apellido para el cliente: ')

                while (True):
                    try:
                        edad = int(input('\nIngrese una edad para el cliente: '))
                    except ValueError:
                        print('\nIngrese un valor númerico')
                        continue
                    break

                intereses = input('\nIngrese un interés para el cliente: ')
                email = input('\nIngrese un email para el cliente: ')
                cliente = Cliente(nombre, apellido, edad, intereses, email)
                BD_cliente.append(cliente)
                print(f'\nCliente {nombre} {apellido} creado.\n')

            elif option == 2:
                print('\nVolviendo al menú principal.')
                break

            else:
                print('\nOpción inválida\n')

        else:
            print('\n[1] Crear cliente\n[2] Comprar como cliente\n[3] Agregar a lista de deseados\n[4] Ver lista de deseados\n[5] Comprar lista de deseados\n[6] Limpiar lista de deseados\n[7] Volver')
            try:
                option = int(input('Elija una opción: '))
            except ValueError:
                print('\nIngrese un valor numérico.\n')
                continue

            if option == 1:
                nombre = input('\nIngrese un nombre para el cliente: ')
                apellido = input('\nIngrese un apellido para el cliente: ')
                edad = int(input('\nIngrese una edad para el cliente: '))
                intereses = input('\nIngrese un interés para el cliente: ')
                email = input('\nIngrese un email para el cliente: ')
                
                cliente = Cliente(nombre, apellido, edad, intereses, email)
                BD_cliente.append(cliente)
                print(f'\nCliente {nombre} {apellido} creado.\n')

            elif option == 2:
                # Comprar como cliente
                print('\nClientes disponibles:')
                for i, cliente in enumerate(BD_cliente, start=1):
                    print(f'[{i}] {cliente.nombre} {cliente.apellido}')
                
                try:
                    client_index = int(input('\nElija un cliente: ')) - 1
                    cliente = BD_cliente[client_index]
                except (IndexError, ValueError):
                    print('\nCliente no válido.\n')
                    continue

                producto = input('\nIngrese el nombre del producto a comprar: ')
                cantidad = int(input('\nIngrese la cantidad a comprar: '))
                tienda = input('\nIngrese el nombre de la tienda: ')
                cliente.comprar(cantidad, producto, tienda)

            elif option == 3:
                # Agregar a lista de deseados
                print('\nClientes disponibles:')
                for i, cliente in enumerate(BD_cliente, start=1):
                    print(f'[{i}] {cliente.nombre} {cliente.apellido}')
                
                try:
                    client_index = int(input('\nElija un cliente: ')) - 1
                    cliente = BD_cliente[client_index]
                except (IndexError, ValueError):
                    print('\nCliente no válido.\n')
                    continue

                producto = input('\nIngrese el producto a agregar a la lista de deseos: ')
                cliente.lista_deseados(producto)

            elif option == 4:
                # Ver lista de deseados
                print('\nClientes disponibles:')
                for i, cliente in enumerate(BD_cliente, start=1):
                    print(f'[{i}] {cliente.nombre} {cliente.apellido}')
                try:
                    client_index = int(input('\nElija un cliente: ')) - 1
                    cliente = BD_cliente[client_index]
                except (IndexError, ValueError):
                    print('\nCliente no válido.\n')
                    continue
                cliente.ver_lista_deseados()

            elif option == 5:
                # Comprar lista de deseos
                print('\nClientes disponibles:')
                for i, cliente in enumerate(BD_cliente, start=1):
                    print(f'[{i}] {cliente.nombre} {cliente.apellido}')
                try:
                    client_index = int(input('\nElija un cliente: ')) - 1
                    cliente = BD_cliente[client_index]
                except (IndexError, ValueError):
                    print('\nCliente no válido.\n')
                    continue
                tienda = input('\nIngrese el nombre de la tienda: ')
                cliente.comprar_lista_deseados(tienda)

            elif option == 6:
                # Limpiar lista de deseos
                print('\nClientes disponibles:')
                for i, cliente in enumerate(BD_cliente, start=1):
                    print(f'[{i}] {cliente.nombre} {cliente.apellido}')               
                try:
                    client_index = int(input('\nElija un cliente: ')) - 1
                    cliente = BD_cliente[client_index]
                except (IndexError, ValueError):
                    print('\nCliente no válido.\n')
                    continue
                cliente.borrar_lista_deseados()

            elif option == 7:
                print('\nVolviendo al menú principal.')
                break
            else:
                print('\nOpción inválida\n')