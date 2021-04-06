matricula = raw_input()
nova_matricula = ""

for x in range(len(matricula)):
	if x == 0:
		nova_matricula += "1"
	elif x == 5:
		nova_matricula += matricula[5] + "0"
	else:
		nova_matricula += matricula[x]

print nova_matricula
