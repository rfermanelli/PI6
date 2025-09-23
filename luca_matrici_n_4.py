i = 0
j = 0
h = int(input("Inserisci numero righe: "))
k = int(input("Inserisci numero colonne: "))
m = []
m2 = []
while i < h:
    while j < k:
        m2.append(int(input("Inserisci un numero in input: ")))
        j = j + 1
    else:
        m.append(m2)
        i = i + 1
        m2 = []
        j = 0

def m_ruotata(m):
    i = h - 1
    j = 0
    ruotata = []
    riga_ruotata = []
    while j < k:
        while i >= 0:
            riga_ruotata.append(m[i][j])
            i = i - 1
        else:
            j = j + 1
            i = h - 1
            ruotata.append(riga_ruotata)
            riga_ruotata = []
    return ruotata
m_ruotata = m_ruotata(m)
print(m_ruotata)