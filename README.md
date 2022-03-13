# python1_suma
 función que pueda sumar 2 números enteros

 x = int(input("Ingresa el valor de x: "))
 y = int(input("Ingresa el valor de y: "))
 suma = x + y
print("El total de la suma es: ")

# python1_suma_arreglo
import random
arreglo = []
for i in range(100):
  arreglo.append(random.randint(1,10))
print("Arreglo: ", arreglo)

suma = 0
for valor in arreglo:
      suma = suma + valor
print(f"La suma del arreglo es {suma} ")
