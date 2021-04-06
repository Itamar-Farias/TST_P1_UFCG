# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

quantidade_numeros = int(raw_input())

lista = []

for i in range(quantidade_numeros):
	numero = int(raw_input())
	if i == 0:
		lista.append(numero)
		menor = numero
		maior = numero

	else:
		lista.append(numero)
		if numero < menor:
			menor = numero
		if numero > maior:
			maior = numero

media = (menor + maior) / 2.0
abaixo = 0
acima = 0

for numero in lista:
	if numero < media:
		abaixo += 1
	if numero > media:
		acima += 1

print 'Menor número: %d' % menor
print 'Maior número: %d' % maior
print 'Média dos extremos: %.2f' % media
print '%d número(s) abaixo da média' % abaixo
print '%d número(s) acima da média' % acima
