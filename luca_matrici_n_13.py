tris_matrix = [[None, None, None], [None, None, None], [None, None, None]]

def tris_setup():

    # impostazione della matrice del tris con None
    tris_matrix =[[None, None, None], [None, None, None], [None, None, None]]

    # scelta del giocatore iniziale e assegnamento del segno
    primo_giocatore = input("Chi inizia il gioco? Scegli: u = utente; m = macchina ---> ")
    if primo_giocatore == "u":
        secondo_giocatore = "m"
    else:
        secondo_giocatore = "u"

    segno_primo_giocatore = input("Scegli segno: X o O ---> ")
    if segno_primo_giocatore == "X":
        segno_secondo_giocatore = "O"
    else:
        segno_secondo_giocatore = "X"

    return tris_matrix, primo_giocatore, segno_primo_giocatore, secondo_giocatore, segno_secondo_giocatore

def mossa_utente(tris_matrix, segno):
    #risultato_tris_setup = tris_setup()
    coordinate_mossa = input("Inserisci le coordinate della mossa separate da una virgola ---> ")
    c_mossa = coordinate_mossa.split(",")
    i = int(c_mossa[0])
    j = int(c_mossa[1])

    if i in (0, 1, 2) and j in (0, 1, 2):
        tris_matrix[i][j] = segno
    else:
        coordinate_mossa = input("Errore: inserisci la coordinata corretta ---> ")

    return coordinate_mossa

tris_matrix, primo_giocatore, segno_primo_giocatore, secondo_giocatore, segno_secondo_giocatore = tris_setup()

print(mossa_utente(tris_matrix, segno_primo_giocatore))










#print(mossa_utente(tris_matrix))
#risultato_tris_setup = tris_setup()
#print(risultato_tris_setup[2])