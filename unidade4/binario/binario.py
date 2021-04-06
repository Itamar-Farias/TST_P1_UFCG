# coding: utf-8
# Itamar da Silva Farias	115210021	
# Programação I

binario = raw_input()
e = len(binario) - 1
produto = 0
soma = 0
for x in range(len(binario)):
	produto = int(binario[x]) * (2 ** e)
	print "%s * %d = %d" % (binario[x], (2 ** e), produto)
	e += -1
	soma += produto

print "%s(2) = %d(10)" % (binario, soma)
