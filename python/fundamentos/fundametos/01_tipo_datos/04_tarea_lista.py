"""
Gestor de inventario
"""

""" 1.- Creación : Cear lista llamada inventario que contenga los siguientes articulos:
    "laptop", "ratón", "monitor", "cable hdmi".
"""
inventario = ["laptop", "ratón", "monitor", "cable hdmi"]
"""
2.- Expansón: utiliza el metodo correspondiente para agregar: 
    "impresora" y "teclado" al final de la lista.
"""
inventario.append("impresora")
inventario.append("teclado")
print(inventario)
"""
3.- Conteo: utiliza la funcion integrada para mostrar cuantos elementos totales hay en la lista. 
"""
print(len(inventario))
"""
4.- Acceso y modificacion: Modifica "teclado" por "teclado mecanico".
"""
inventario[5] = "teclado mecanico"
print(inventario)
"""
5.- slicing: crea una nueva lista llamada "promocion", debe contener
    solo los 3 primeros elementos de la lista "inventario".
"""
promocion = inventario[:3]
print(promocion)
"""
6.- Mostrar la lista de inventario ordenado alfabeticamente.
"""
inventario.sort()
print(inventario)
"""
7.- elimina el ultimo elemento de la lista inventario mostrando el elemento eliminado y la lista final. 
"""
elemento_eliminado = inventario.pop()
print(inventario)
print(elemento_eliminado)



