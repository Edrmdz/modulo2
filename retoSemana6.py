# Reto de la semana 6
# ingresar una contraseña, el primer digito sea un numero, al tercer intento fallido se cierra el programa

psw1 = input("¿Cual es tu contraseña: ")

while psw1[0].isalpha():                                        #compara 1er digito
    print("Error, el primercaracter debe de ser un número.")    #advertencia de colocar numero
    psw1 = input("Ingrese una contraseña: ")                    #reingresa el valor de la nueva entrada a psw1

for i in range(3):

    psw2 = input("Repite la contreña ")                         #ingresa contraseña 2
    if psw1 == psw2 :                                             # compara contraseñas
        print("Contraseña correcta. ")
        break
    else:
        print("No coinciden.")
        print("van ", i+1, " intentos ")
        
print("Fin del programa.")