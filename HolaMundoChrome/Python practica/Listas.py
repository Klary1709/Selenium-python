#notas
# setear un tipo es variable=tipoASetear(variable)
#numero=int(numero)
#PARA pasar a stram es str(variable)
# para ingregar en panralla es el input ,variable = input(variable)
# podemos ingresa un variable en consula y luego setearle un tipo



lenguajes = ["php", "Java","python","Javascript"]

lenguajes.append("KLARYLU")
lenguajes.remove("php")

CONT=1
print("lENGUAJES DISPONIBLES")
for i in lenguajes:
    print(str(CONT)+"- "+i)
    CONT=CONT+1

print("\nSELECCIONE UN LEGUAJE :")
selec=input()
selec=int(selec)
print(lenguajes[selec-1])

if (selec==2 or selec==3 and lenguajes[selec-1]=="Java" or lenguajes[selec-1]=="python" ):
    print("el numero es 2 y lenguaje Java")
else:
    print("Numero distinto a 2 o No se esta tomando la variable ")




