print("ingrese numero de respuestas correctas: ")
RC =int(input())
print("ingrese numero de respuestas incorrectas: ")
RI= int(input())
print("ingrese numero de respuestas en blanco: ")
RD= int(input())
PCR= RC*3
PRI= RI*-1
PRB= RD*0
PF= PCR+PRI+PRB
print("El puntaje total es:", PF)