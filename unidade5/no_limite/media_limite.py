# coding: utf-8
# Itamar da Silva Farias	115210021	
# Programação I

i = 1
lista_numero = []
lista_numero_media = []
soma = 0

while True:
	numero = raw_input()
	if numero == "-":
		valor_limite = float(raw_input())
		break
	soma += float(numero)
	lista_numero.append(float(numero))
	media_instantanea = soma / i
	lista_numero_media.append(media_instantanea)
	i += 1

lista = []
j = 1

for x in range(len(lista_numero_media)):
	if lista_numero_media[x] > valor_limite:
		lista.append(lista_numero_media[x])
		break
	j += 1
		
if lista == []:
	print "limite não alcançado" 
	
else:
	print "media = %.1f" % lista[0]
	print "num = %d" % j
	


			
