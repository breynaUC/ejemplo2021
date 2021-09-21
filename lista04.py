x = int(input("n: "))
cursos=[]
notas=[]
ph = 40
print(x)
for i in range(x):
    w = input("Curso: ")
    q = float(input("Nota: "))    
    cursos.append(w)
    notas.append(q)
for i in range(0,x):
    print(cursos[i],notas[i])
