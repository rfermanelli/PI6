def tris_setup():

    # impostazione della matrice del tris con None
    tris_matrix =[[None, None, None], [None, None, None], [None, None, None]]

    # scelta del giocatore iniziale e assegnamento del segno
    mossa = input("Chi inizia il gioco? Scegli: u = utente; m = macchina ---> ")
    return tris_matrix, mossa

def tris_matrix_ctrl(tris_matrix):
    pass

def tris_matrix_view(tris_matrix):
    pass

def mossa_utente(tris_matrix):
    coordinate_mossa = input("Inserisci le coordinate della mossa separate da una virgole---> ")

    s = "1,1"   ls = ['1', '1']
    tris_matrix[riga][colonna] = "X"


def mossa_macchina(tris_matrix):
    pass




tris_matrix, mossa = tris_setup()



