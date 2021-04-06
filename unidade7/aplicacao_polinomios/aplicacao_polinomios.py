# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def polinomio(lista,numero):
    soma = 0
    for i in range(len(lista)):
        soma += (numero**int(i)) * int(lista[i])
    return soma

x = True
novo = ""
while x == True:
    if novo != '':
        atualiza = novo
        novo = novo.split()
        novo = novo[1:]
        poli = raw_input()
        if poli == "fim": break
        print polinomio(novo,int(poli))
        novo = atualiza
    else:
        poli = raw_input()
        if poli == "fim": break
        if poli[0] == "p":
            print "novo polinomio"
            while True:
                entrada = raw_input()
                if entrada == "fim":
                    x = False
                    break
                if entrada[0] != "p":
                    atualiza = poli
                    poli = poli.split()
                    poli = poli[1:]
                    print polinomio(poli,int(entrada))
                    poli = atualiza
                else:
                    novo = entrada
                    print "novo polinomio"
                    break
                    
