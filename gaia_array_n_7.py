s =(input("inserire stringhe"))
l_a =s.split()

def modifica_array(l_a):
    nuovo_array = []
    vocali = "aeiouAEIOU"
    for s in l_a:
        if len(s) % 2 == 0:
            nuova_stringa = "".join(reversed(s))
        else:
            nuova_stringa = s
            if len(s) % 2 == 1:

                for v in vocali:
                    nuova_stringa = nuova_stringa.replace(v,"*")
        nuovo_array.append(nuova_stringa)
    return nuovo_array

print (modifica_array(l_a))
