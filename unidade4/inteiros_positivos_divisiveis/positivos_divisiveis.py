# coding: utf -8
# Itamar da Silva Farias
# Programação I

a = int(raw_input())
b = int(raw_input())
k = int(raw_input())
lista = []
for n in range(1, k + 1):
	if n % a == 0 and n % b == 0 and n <= k:
		lista.append(n)

for x in lista:
	print x		
		
