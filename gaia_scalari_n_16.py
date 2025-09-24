a = int (input(" inserire numero:"))
b = int (input(" inserire numero:"))

def divisione (a, b):
 if b == 0:
     print ("ERRORE: divisione per zero")
     return True
 else:
     return False


quoziente = 0
resto = a

while resto >= b:
    if divisione(a, b):
        break
    else:
        resto = resto - b
        quoziente = quoziente + 1

print (quoziente, resto)






