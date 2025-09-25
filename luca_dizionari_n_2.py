numero_prodotti = int(input("Inserisci numero dei prodotti: "))
i = 0
prodotti = []
p = {}

while i < numero_prodotti:
    p = {"nome" : input("Inserisci nome dei prodotti: "),
        "quantità disponibile" : int(input("Inserisci quantità disponibile: ")),
         "prezzo unitario" : float(input("Inserisci prezzo unitario: "))
         }

    prodotti.append(p)

    i = i + 1
    p = {}

i = 0
prodotto_unitario_più_alto = 0

while i < numero_prodotti:
    if prodotti[i]["prezzo unitario"] > prodotto_unitario_più_alto:
        prodotto_unitario_più_alto = prodotti[i]["prezzo unitario"]
        nome_prodotto_più_alto = prodotti[i]["nome"]
        i = i + 1
    else:
        i = i + 1

print("Nome prodotto:",nome_prodotto_più_alto)
print("Prezzo:",prodotto_unitario_più_alto)







