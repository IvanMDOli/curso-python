from Paquete1.cliente import Cliente
from Paquete1.login import *


cliente1 = Cliente("Iván", "De oli", 25, ["Programación", "Cine", "Música"], "ivanmdeoli@hotmail.com")

print(cliente1)

cliente1.comprar(10, "Celulares", "Mercado Libre")
cliente1.lista_deseados(["Televisor", "PS5", "Laptop"])

cliente1.comprar_lista_deseados("Mercado Libre")

menu(user_list)
