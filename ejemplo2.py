letras = ["A", "B", "C"]
print(letras)
for i in range(len(letras)):
    letras[i] = "X"
    print(letras)

['A', 'B', 'C']
['X', 'B', 'C']
['X', 'X', 'C']
['X', 'X', 'X']