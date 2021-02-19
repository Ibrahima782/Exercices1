def chaine_caractere (ch ="alpha", ch2="mamadou"):
    m =[]
    for i in ch:
        for j in ch2:
            if i == j:
                if i not in m:
                    m.append(i)
    print(m)
    return m
chaine_caractere()

def chaine_caractere(ch = "klbc", ch2 ="kaba"):
    ibrahima = []
    for i in ch :
        for j in ch2 :
            if i == j:
                if i not in ibrahima:
                    ibrahima.append(i)
    print(ibrahima)
    return ibrahima
chaine_caractere()