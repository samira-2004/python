print("ingrese numero de partidos ganados")
PG= int(input())
print("ingrese numero de partidos empatados")
PE= int(input())
print("ingrese numero de partidos perdidos")
PP= int(input())
PPG= PG*3
PPE= PE*1
PPP= PP*0
PF= PPG+ PPE+ PPP
print("\nSALIDA: ")
print("-------------")
print("Puntaje Final:", PF)