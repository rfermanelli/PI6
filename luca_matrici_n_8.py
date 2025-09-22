i = 0
j = 0
n = int(input("Inserisci dimensione quadrata matrice: "))
matrice = []
m = []
while i < n:
    while j < n:
        m.append(int(input("Inserisci numero: ")))
        j = j + 1
    else:
        matrice.append(m)
        m = []
        i = i + 1
        j = 0

def matrice_trasposta(matrice):
   i = 0
   j = 0
   trasposta = []
   riga_trasposta = []
   while j < n:
       while i < n:
           riga_trasposta.append(matrice[i][j])
           i = i + 1
       else:
           j = j + 1
           i = 0
           trasposta.append(riga_trasposta)
           riga_trasposta = []
   return trasposta
matrice_trasposta = matrice_trasposta(matrice)

i = 0
j = 0
if matrice_trasposta == matrice:
    print(0)
else:
    while j < n:
        while i < n:
            while matrice[i][j] + matrice_trasposta[i][j] == 0:
                i = i + 1
            else:
                print("Error")
                break
        else:
            j = j + 1
    print(1)






