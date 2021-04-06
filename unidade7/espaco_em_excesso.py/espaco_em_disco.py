# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def fun(): 
	nomes = []
	espacos = []
	soma = 0.0
	while True:
		login = raw_input().split()
		if login[0] == "fim":
			break
		nomes.append(login[0])
		espacos.append((float(login[1]) / 1024) / 1024)
		soma += (((float(login[1]) / 1024) / 1024))
	
	print "SPLab - Espaço utilizado pelos usuários"
	print "---------------------------------------------"
	print "Nr., Usuário, Espaço Utilizado, %s do uso\n" % ("%")
	
	total = 0
	
	for i in range(len(espacos)):
		print "%d, %s, %.2f MB, %.2f%%" % (i + 1, nomes[i], espacos[i], ((espacos[i] / soma) * 100))
		total += espacos[i]
	
	print "\nEspaço total ocupado: %.2f MB" % total
	print "Espaço médio ocupado: %.2f MB" % (total / len(espacos))

fun()
