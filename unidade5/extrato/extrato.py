# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

limite_saque = int(raw_input())
saldo = float(raw_input())
total_saque = 0
while True:
	operacao = raw_input().split()
	if operacao[0] != "saque" and float(operacao[1]) > 1000.0:
		print "Operação inválida: %s %.2f." % (operacao[0], float(operacao[1]))
		break
	elif operacao[0] != "saque":
		saldo += float(operacao[1])	
	elif operacao[0] == "saque":
		saldo -= float(operacao[1])
		total_saque += 1
		if saldo < 0: 
			print "Operação inválida: %s %.2f." % (operacao[0], float(operacao[1]))
			saldo += float(operacao[1])
			break
		if total_saque > limite_saque:
			print "Operação inválida: %s %.2f." % (operacao[0], float(operacao[1]))
			saldo += float(operacao[1])
			break

print "Seu saldo é R$ %.2f." % saldo
