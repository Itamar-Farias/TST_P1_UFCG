# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def letra_magica(fila, letra):
    fila1,fila2 = [],[]
    for i in fila:
        if i[0] == letra.upper() or i[0] == letra.lower():
            fila1.append(i)
        else:
            fila2.append(i)
    compara = fila1 + fila2
    for i in range(len(compara)):
        fila[i] = compara[i]
