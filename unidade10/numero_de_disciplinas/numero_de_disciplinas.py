# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def numero_disciplinas(m1,m2, pagas):
	disciplinas = 0
	horarios = []
	for chave in m1:
		achou = True
		for i in m1[chave]:
			if i not in pagas:
				achou = False
				break
		if achou and chave not in pagas and m2[chave] not in horarios:
			horarios.append(m2[chave])
			disciplinas += 1
		
	return disciplinas
