#Reto de la semana 5
#Solcitando 2 valores
dato1 = int(input("Introduce el año actual: "))
dato2 = int(input("Introduce otro año para calcular:: "))
if dato1 > dato2 :
    print("Han pasado ", (dato1 - dato2), "años desde el año que has introducido")

elif dato1 < dato2 :
    print("Faltan ", dato2 - dato1, "años para llegar al año que has introducido")

else:
    print("Los numeros ingresados son iguales")
