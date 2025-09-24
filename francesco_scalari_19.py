n = int(input("Inserisci un numero intero positivo diverso da 1: "))
z = n
i = 0


def collatz_sequence(n):
    """
    Genera la sequenza di Collatz per un dato numero intero positivo.

    Args:
        n (int): Il numero intero positivo di partenza.

    Returns:
        list: Una lista di numeri che rappresenta la sequenza di Collatz.
    """

while n < 0 or n == 0:
    while True:
        if n != 0 or n == 0:
            print("Errore: Inserisci un numero intero positivo.")
            n = int(input("prova di nuovo "))
            z = n
            break
sequence = [n]
while n != 1:
    if n % 2 == 0:  # n % 2 == 0 verifica se il numero è pari
        n = n // 2  # Usiamo // per la divisione intera
    else:
        n = 3 * n + 1
    sequence.append(n)
i = len(sequence)
i = i-1
print("La sequenza di collatz di", z, "è --> ", *sequence, sep="\n")
print("ed è lunga--> ", i)