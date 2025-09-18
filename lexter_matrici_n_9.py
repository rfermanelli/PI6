M1 = []
M2 = []
M3 = []
V = []

lm = int(input("dimensione matrice quadrata: "))

i = 0
j = 0

while i <= lm - 1:
    while j <= lm - 1:
        V.append(int(input("inserisci variabile vettore di M1: ")))
        j = j + 1
    else:
        i = i + 1
        j = 0
        M1.append(V)
        V = []
else:
    V = []

i = 0
j = 0

while i <= lm - 1:
    while j <= lm - 1:
        V.append(int(input("inserisci variabile vettore di M2: ")))
        j = j + 1
    else:
        i = i + 1
        j = 0
        M2.append(V)
        V = []
else:
    V = []

i = 0
j = 0

while i <= lm - 1:
    while j <= lm - 1:
        V.append(M1[i][j] * M2[i][j])
        j = j + 1
    else:
        i = i + 1
        j = 0
        M3.append(V)
        V = []
else:
    print(M3)

