# Creación de la clase

class Cliente():
    def __init__(self, nombre, apellido, edad, intereses, email):
        
        self.nombre = nombre
        self.apellido = apellido
        self.__edad = edad
        self.intereses = intereses
        self.email = email
        self.deseados = []

    def __str__(self):
        return f'Se ha creado un nuevo cliente.\nCliente: {self.nombre} {self.apellido}\nEdad: {self.__edad} años.\nIntereses: {self.intereses}'
    
    def comprar(self, cantidad, producto, tienda): # Método de compra
        print(f'El cliente {self.nombre} {self.apellido} ha comprado {cantidad} {producto} en la tienda {tienda}.')
        return print(f'Se ha enviado un correo con su factura a {self.email}.')
    
    def lista_deseados(self, producto): # Método para agregar a lista de deseados
        if isinstance(producto, list):
            self.deseados.extend(producto)
            producto = ', '.join(producto)
        else:
            self.deseados.append(producto)
        return print(f'\n{self.nombre} {self.apellido} ha agregado {producto} a la lista de deseados.\n')
    
    def ver_lista_deseados(self): # Método para ver la lista de deseados

        if self.deseados:
            print(f'\nLa lista de deseados de {self.nombre} {self.apellido} es: \n')
            lista = '\n'.join(self.deseados)
            return print(lista)
        else:
            return print('\nLa lista está vacía.\n')
    
    def borrar_lista_deseados(self): # Método para borrar la lista de deseados
        self.deseados = []
        return print('\nSe ha borrado la lista de deseados.\n')
    
    def comprar_lista_deseados(self, tienda):
        lista = ', '.join(self.deseados)
        print(f'\nEl cliente {self.nombre} {self.apellido} ha comprado {lista} en {tienda}.\n')
        return print(f'\nSe ha enviado un correo con su factura a {self.email}.\n')