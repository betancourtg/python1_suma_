# python2_suma_arreglo
import random
arreglo = []
for i in range(100):
  arreglo.append(random.randint(1,10))
print("Arreglo: ", arreglo)

suma = 0
for valor in arreglo:
      suma = suma + valor
print(f"La suma del arreglo es {suma} ")