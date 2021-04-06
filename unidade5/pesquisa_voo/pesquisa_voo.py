# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

total_de_registros = int(raw_input())
registros = []

for i in range(total_de_registros):
	registro = raw_input().split(",")
	registros.append(registro)

while True:
	melhores_voos = []
	voo_escolhido = ""
	melhor_opcao = raw_input()
	
	if melhor_opcao == "fim":
		break
	
	elif melhor_opcao == "valor":
		melhor_voo = ""
		melhor_preco = float(registros[0][0])
		
		for j in range(len(registros)):
			if float(registros[j][0]) < melhor_preco:
				melhor_preco = float(registros[j][0])
				melhor_voo = registros[j][-1]
		
		for m in range(len(registros)):
			if melhor_preco == float(registros[m][0]):
				melhores_voos.append(registros[m][-1])
		
		if melhores_voos == []:
			print melhor_voo
		
		else:	
			print melhores_voos[0]
	
	elif melhor_opcao == "conexões":
		melhor_voo = ""
		melhor_conexao = float(registros[0][1])
	
		for k in range(len(registros)):
			if float(registros[k][1]) < melhor_conexao:
				melhor_conexao = float(registros[k][1])
				melhor_voo = registros[k][-1]
		
		for o in range(len(registros)):
			if melhor_conexao == float(registros[o][1]):
				melhores_voos.append(registros[o][-1])
		
		
		if melhores_voos == []:
			print melhor_voo
		
		else:
			print melhores_voos[0]
				
	else:
		melhor_tempo = float(registros[0][2])
		melhor_voo = ""
		
		for l in range(len(registros)):
			if float(registros[l][2]) < melhor_tempo:
				melhor_tempo = float(registros[l][2])
				melhor_voo = registros[l][-1]
				
		for q in range(len(registros)):
			if melhor_tempo == float(registros[q][2]):
				melhores_voos.append(registros[q][-1])
		
		
		if melhores_voos == []:
			print melhor_voo
		
		else:
			print melhores_voos[0]
