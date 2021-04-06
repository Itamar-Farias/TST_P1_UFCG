# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

media = 0
contador = 1
soma = 0
lista_valor = []
while True:
	valor = float(raw_input())
	lista_valor.append(valor)
	soma += valor
	media = soma / contador
	if valor < media:
		break
	contador += 1

print "Saldo total do FIS: R$%.2f." % (soma - lista_valor[-1])
print "Média das contribuições: R$%.2f." % ((soma - lista_valor[-1]) / (contador - 1))
