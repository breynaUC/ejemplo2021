

lista1 =[]#Trabajadores
lista2 =[]#Horas
lista3 =[]#Sueldo
x = int(input("N°: "))
pagohora = 40
for i in range(x):
    nombre = input("Nombre: ");
    lista1.append(nombre)
    horasT = int(input("Horas: "))
    lista2.append(horasT)
    sueldo = pagohora*horasT
    lista3.append(sueldo)
print("Trabajadores\tHoras\tSueldo")
for y in range(0,x):
    print(lista1[y],"\t\t",lista2[y],"\t",lista3[y])
