try:
    n = int(input("dammi un naturale: "))
    assert n > 0
except ValueError:
    print("Il valore inserito non è intero")
except AssertionError:
    print("Il valore inserito non è positivo")