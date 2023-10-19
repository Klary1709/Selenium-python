NOMBRES=["Miriam","Luna","Abby","Mich"]

cont=0
for i in NOMBRES:
    cont=cont+1
    print("Nombre " +str(cont)+ "= "+ i)


#rango del 10 la 20 de dos en dos
for x in range (10, 200,7):
    if (x>=74):
        break
    print(x)
print("------------------\n")
#excluyendo numeros exactos

for num in range(12 , 23):
    if(num==13 or num==19 or num==20):
        continue
    print(num)




alerta=""
klary=0
while(alerta!="No hay nada"):

    klary=klary+1

    if(klary==4):
        print("YA LLEGO A " + str(klary))
        continue

    elif(klary==7):
        alerta = "No hay nada"

        print(" \nFIN DE LA PRUEBA")
        continue

    print("Esta prueba es esrabdar "+ str(klary))



