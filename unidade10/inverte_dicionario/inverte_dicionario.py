#coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def inverte_dicionario(dicionario):
	novo_dic = {}
	for i in dicionario:
		if novo_dic.has_key(dicionario[i]):
			novo_dic[dicionario[i]].append(i)
			ordena = novo_dic[dicionario[i]]
			for k in range(len(ordena)-1):
				for j in range(len(ordena)-1-k):
					if ordena[j] > ordena[j+1]:
						ordena[j],ordena[j+1] = ordena[j+1],ordena[j]
		else:
			novo_dic[dicionario[i]] = [i]
	return novo_dic
	
m = {"a": None, "b": 3, "c": 2}
print inverte_dicionario(m)
