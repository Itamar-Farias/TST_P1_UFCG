# coding: utf-8
# Itamar da Silva Farias	115210021
# programação I

limite = int(raw_input())
i = 1
soma = 0
while soma < limite:
	soma += i
	if soma > limite: break
	if soma < limite:
		print i
	i += i	
		

