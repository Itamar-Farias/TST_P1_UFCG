# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def troca_chave(dic):
	novo_dic = {}
	for i in dic:
		novo_dic[dic[i]] = i
	
	return novo_dic

assert troca_chave({1:2}) == {2:1}
assert troca_chave({1:2, 2:3, 3:4}) == {2:1, 3:2, 4:3}
assert troca_chave({ '@':'V','a':'v', 'n':'o'}) == { 'V':'@','v':'a', 'o':'n'}
