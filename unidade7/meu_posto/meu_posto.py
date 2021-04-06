# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

num_cpfs = []
nomes = []
postos = []
saldos = []
def cadastro(cpf,nome,posto):
	num_cpfs.append(cpf)
	nomes.append(nome)
	postos.append(posto)
	saldos.append(300.0)
	print "Usuário cadastrado com sucesso."

def procura_usuario(cpf,nome,posto):
	achou = False
	for i in num_cpfs:
		if cpf == i:
			print "Usuário já existente."
			achou = True
			break
	if not achou:
		cadastro(cpf,nome,posto)
		
def consulta(cpf):
	achou = False
	for i in range(len(num_cpfs)):
		if num_cpfs[i] == cpf:
			print "Nome: %s" % nomes[i]
			print "CPF: %s" % num_cpfs[i]
			print "Saldo: %.2f" % saldos[i]
			achou = True
	if not achou:
		print "Usuário inexistente."

def atualiza(cpf,posto):
	achou = False
	indice = 0
	if len(num_cpfs) > 0:
		for i in range(len(num_cpfs)):
			if cpf == num_cpfs[i]:
				indice = i
				achou = True
				break
	else:
		print "Usuário inexistente."
		return
	if achou == True:
		if postos[indice] == posto:
			saldos[indice] = (saldos[indice] + 300)
		else:
			saldos[indice] = (saldos[indice] + 100)
		print "Usuário atualizado com sucesso."
	if not achou:
		print "Usuário inexistente."
		
while True:
	dado = raw_input()
	if dado == "finalizar": break
	if dado == "cadastrar":
		cpf = raw_input()
		nome = raw_input()
		posto = raw_input()
		procura_usuario(cpf,nome,posto)
	elif dado == "atualizar":
		cpf = raw_input()
		posto = raw_input()
		atualiza(cpf,posto)
	elif dado == "consultar":
		cpf = raw_input()
		consulta(cpf)
