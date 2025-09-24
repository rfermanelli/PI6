def conta_isole(matrice):
    n = len(matrice)

    def dfs(i, j):
        # Controlla se siamo fuori dai limiti o se la cella non è terra
        if i < 0 or i >= n or j < 0 or j >= n or matrice[i][j] != 1:
            return
        # Marca la cella come visitata
        matrice[i][j] = -1

        # Esplora le 4 direzioni (su, giù, sinistra, destra)
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    isole = 0
    for i in range(n):
        for j in range(n):
            if matrice[i][j] == 1:
                dfs(i, j)
                isole += 1

    return isole


# Esempio di utilizzo
matrice = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 1, 0, 0]
]

print("Numero di isole:", conta_isole(matrice))
