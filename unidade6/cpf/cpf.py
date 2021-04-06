# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I


def calcula_digitos_verificacao(digit):
    
    invertida = []
    soma = 0
    soma2 = 0
    for i in range(len(digit)-1,-1,-1):
        invertida.append(digit[i])    
    
    for j in range(len(invertida)):
        d = int(j) + 2
        soma += d * int(invertida[j])
    digito_verificador1 = (soma * 10) % 11
    if digito_verificador1 == 10:
        digito_verificador1 = 0

    soma2 += digito_verificador1 * 2
    for k in range(len(invertida)):
        d1 = int(k) + 3
        soma2 += d1 * int(invertida[k])
    digito_verificador2 = (soma2 * 10) % 11
    if digito_verificador1 == 10:
        digito_verificador1 = 0
    digito = "%d%d" % (digito_verificador1, digito_verificador2)
    return digito
