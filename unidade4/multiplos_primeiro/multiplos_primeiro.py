# coding: utf-8
# Itamar da Silva Farias 115210021	
# Programação I

primeiro = int(raw_input())
z = []
soma = 0

for n in range(10):
	numero = int(raw_input())
	if numero % primeiro == 0:
		z = z + [numero]
		
for x in z:
	soma = soma + x

print  soma
