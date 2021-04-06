# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

cc = raw_input()
soma_impar = 0
soma_par = 0
for x in range(len(cc)):
	if x % 2 == 0:
		soma_impar += int(cc[x])
	else:
		soma_par += int(cc[x])

produto = soma_impar * soma_par

if produto % 11 == 10:
	print "%s-X" % cc
else:
	print "%s-%d" % (cc, produto % 11)
