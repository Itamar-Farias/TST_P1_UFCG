# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

num_1 = int(raw_input())
num_2 = int(raw_input())
num_3 = int(raw_input())

if num_1 == 13:
	print "0"

elif num_2 == 13:
	soma = num_1 
	if soma == 13:
		print "0"
	else:
		print soma
	
elif num_3 == 13:
	soma = num_1 + num_2
	if soma == 13:
		print "0"
	else:
		print soma

else:
	soma = num_1 + num_2 + num_3
	if soma == 13:
		print "0"
	else:
		print soma
