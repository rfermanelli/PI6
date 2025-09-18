i = 0
j = 0
h = float (input("inserisci numero righe: "))
k = float (input("inserisci numero colonne: "))
M = []
m = []
while i < h:
    while j < k:
        m.append(float(input("inserisci un numero in input: ")))
        j = j + 1
    else:
        M.append(m)
        i = i + 1
        m = []
        j =  0
def matrice_simmetrica_antisimmetrica (M):
    n = len(M)
    i = 0
    j = 0
    for i in range(n):
        for j in range(n):
            if M [i][j] == M [j][i]:
                print (0)
            else:
                if M [i][j] ==  -M [j][i]:
                  print (1)


