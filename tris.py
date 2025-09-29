from ramo_1_test import coordinate_mossa


def tris_setup():

    # impostazione della matrice del tris con None
    tris_matrix =[[None, None, None], [None, None, None], [None, None, None]]

    # scelta del giocatore iniziale e assegnamento del segno
    primo_giocatore = input("Chi inizia il gioco? Scegli: u = utente; m = macchina ---> ")
    return tris_matrix, primo_giocatore

def tris_matrix_ctrl(tris_matrix):
    pass

def tris_matrix_view(tris_matrix):
    pass

def mossa_utente(tris_matrix):
    coordinate_mossa = input("Inserisci le coordinate della mossa separate da una virgole---> ")
    riga = coordinate_mossa[0]
    colonna = coordinate_mossa[2]
    tris_matrix[riga][colonna] = "X"


def mossa_macchina(tris_matrix):
    pass




tris_matrix, mossa = tris_setup()



