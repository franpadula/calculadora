print("Bienvenido a la francalculadora")

num1 = int(input("2)"))
num2 = int(input("4"))

print("Elige entre estas opciones")
print("1\. Suma")
print("2\. Resta")
print("3\. Multiplicación")
print("4.\ División")

operacion = int(input("¿Que operación desea realizar? Introduzca el número (1, 2, 3, o 4)"))

if operacion == 1:
   Resultado = num1 + num2
    print (f"El resultado de x operacion es: {Resultado}")
elif operacion == 2:
    Resultado = num1 - num2
    print (f"El resultado de x operacion es: {Resultado}")
elif operacion == 3:
    Resultado = num1 * num2
    print (f"El resultado de x operacion es: {Resultado}")
elif operacion == 4:
    Resultado = num1 / num2
    print (f"El resultado de x operacion es: {Resultado}")
else:
  #El usuario no ha introducido una opcion valida