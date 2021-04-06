# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

valor_meta = float(raw_input())
venda_total = 0
lista_funcionario = []
numero_meta_alc = 0
for x in range(6):
	venda_funcionario = float(raw_input())
	venda_total += venda_funcionario
	lista_funcionario.append(venda_funcionario)
	if venda_funcionario >= valor_meta / 6:
		numero_meta_alc += 1 

func = 1
	
if venda_total >= valor_meta and numero_meta_alc == 6:
	print "Total de vendas: R$ %.2f (meta atingida)" % venda_total
	print "----"
	print "Bonificação:"
	for z in range(len(lista_funcionario)):
		print "Funcionário %d: R$ %.2f" % (func, (lista_funcionario[z] * 0.01))
		func += 1
else:
	print "Total de vendas: R$ %.2f (meta não foi atingida)" % venda_total
	print "----"
