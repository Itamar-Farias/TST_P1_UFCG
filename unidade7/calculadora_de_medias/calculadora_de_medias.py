# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def medias():

	while True:
		
		media = raw_input().split()
				
		if media[0] == "Q":
			break
		
		numeros = raw_input().split()
		
		for x in range(len(media)):
			if media[x] == "MA":
				soma = 0.0
				for i in range(len(numeros)):
					soma += float(numeros[i])
				print "Média Aritmética: %.4f" % (soma / len(numeros))
			
			elif media[x] == "MG":
				produto = 1.0
				for j in range(len(numeros)):
					produto *= float(numeros[j])
				print "Média Geométrica: %.4f" % (produto ** (1.0 / len(numeros)))
				
			else:
				somatorio = 0.0
				for k in range(len(numeros)):
					somatorio += (1.0 / float(numeros[k]))
				print "Média Harmônica: %.4f" % (len(numeros) / somatorio)
				
		print "----"
	
medias()	
			
	
