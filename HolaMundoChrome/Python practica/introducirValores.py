print("cual es tu nombre: ")
nom=input()
print("Cual es tu apellido: ")
ap=input()
print("Que edad tienes?")
edad=input()
edad= int(edad)
print("Tu nombre es " + nom+ " "+ap+ " y tienes la edad de "+ str(edad) );


if edad>=18:
    a = " ya eres mayor de edad "
else:
    a =" aun tas chikito y debes esperar para comprar guaro "


print("tu nombre es {} {} y tienes {} entonces {}".format(nom, ap, edad, a))
