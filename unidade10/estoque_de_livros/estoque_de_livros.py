# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def ausentes(estoque):
	quantidade = 0
	for i in estoque:
		if estoque[i] == 0:
			quantidade += 1
	return quantidade
