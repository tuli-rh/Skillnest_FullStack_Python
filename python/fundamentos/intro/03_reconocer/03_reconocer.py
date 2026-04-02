"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random   #Importacion de libreria para procesos aleatorios


nombre = "Frida Kahlo"   #Creación de variable tipo string y se asigna un valor.
print(type(nombre))      #Type() = método de pythom para mostrar el tipo de una variable.
print(len(nombre))       #len() = devuelve el largo de una variable.


edad = 25   #Creación de variable tipo numerico(int).


if edad < 18:                    #Se establece condicion if.
   print("Eres menor de edad.")  #Imprime un mensaje.
elif edad == 18:                 #Se establece condicion elif (else - if).
   print("Tienes 18 años.")      #Imprime un mensaje.
else:                            #Cierre de condicion (si no se cumplen condiciones anteriores).
   print("Eres mayor de edad.")  #Imprime un mensaje.


frutas = ["manzana", "pera", "fresa"]  #Creacion de array (lista) con valores asignados.
print(frutas[0])                       #Mostramos la primera posicion 0 del arreglo.
frutas[0] = "banana"                   #A la posicion 0 del array se le asigna el valor de "banana".
frutas.append("uva")                   #Se le agrega "uva" al final del arreglo.
frutas.remove("pera")                  #Se remueve la palabra "pera" al arreglo.


dimensiones = (200, 50)  #Creacion de variable tipo tupla (variable inmutable).
print(dimensiones[0])    #Imprime la posicion 0 de la variable creada.


persona = {            #Variable tipo object (objeto).
   "nombre": "Carlos", #Se establece un item y su respectivo valor.
   "edad": 30          #Se establece un item y su respectivo valor.
}
print(persona["nombre"])        #Imprime el valor del item(ej: "Carlos").
persona["edad"] = 31            #Se modifica el valor del item edad a 31.
persona["ciudad"] = "Santiago"  #Se agrega un nuevo item con un valor.
del persona["ciudad"]           #Se elimina un item completo.


for i in range(5):  #for range: se crea bucle en rango desde 0 a 5.
   if i == 2:       #Se establece condicion if == 2.
       continue     #Continue ignora el proceso y continua.
   if i == 4:       #Se establece la condicion if i == 4.
       break        #Si i == 4 se rompe el bucle.
   print(i)         #Imprime valor de i en cada iteracion (hasta 4).


contador = 0         #Se crea una variable contador tipo numerico(int).
while contador < 3:  #Se crea un bucle while con una condicion.
   print(f"while contador es: {contador}")  #Imprime el contador en un mensaje concatenado con f"" string.
   contador += 1     #Incrementa el valor en i en cada iteracion.


def saludar_usuario(nombre):  #def - palabra reservada para crear una funcion.
   return f"Hola, {nombre}"   #Devuelve un valor de la funcion.


print(saludar_usuario("Francisca"))  #Se imprime "Hola Francisca" -return de la funcion.