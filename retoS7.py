from optparse import Option


lista = []
alumnos = 0
while alumnos <=10:
    opcion = input("Agregar alumno (1) o Terminar (2): ")
    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno: ').capitalize()
        calif1 = int(input(f'Ingrese la primer calificación de {nombre}:'))
        calif2 = int(input(f'Ingrese la segunda calificación de {nombre}:'))
        calif3 = int(input(f'Ingrese la tercer calificación de {nombre}:'))
        cal = [int(calif1), int(calif2),int(calif3)]
        promCal = sum(cal)/float(len(cal))
        alumno = [nombre, promCal]
        lista.append(alumno)
        alumnos += 1
    elif opcion == '2':
        print(f'Se creo una lista con {alumnos} alumnos ')
        break
    else:
        print('Opción inválida')
        continue 
print('Esta es la lista de promedios por alumno: ')
for i in lista:
    print(i, end='')