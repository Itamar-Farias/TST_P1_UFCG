# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def is_substring_expr(str1,str2):
	str_separada = [""]
	indice = 0
	for letra in str2:
		if not letra == "*":
			str_separada[indice] = str_separada[indice]+letra
		else:
			str_separada.append("")
			indice += 1
			
	for i in range(len(str_separada[0])):
		if str_separada[0][i] == str1[i]:
			pass
		else:
			return False
	
	for i in range(-1, -len(str_separada[1])-1, -1):
		if str_separada[1][i] == str1[i]:
			pass
		else:
			return False
	return True
