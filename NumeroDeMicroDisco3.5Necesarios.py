import math
print("ingrese GB: ")
GB= float(input())
MG= GB*1024
MD= MG / 1.44
print("\nSALIDA")
print("-------------")
print(MD)
print("Numero de Disco necesarios:", math.ceil(MD))