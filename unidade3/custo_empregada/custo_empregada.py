# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

salario_base = float(raw_input())
dias_trabalhado = int(raw_input())
custo_diario_transporte = float(raw_input())

print "O salário base é R$ %.2f" % salario_base

FGTS = 0.08 * salario_base
gasto_do_empregado = salario_base + FGTS

salario_liquido = salario_base
custo_total_transporte = dias_trabalhado * custo_diario_transporte

if custo_total_transporte > 0.06 * salario_base:
	salario_liquido -= 0.06 * salario_base
	gasto_do_empregado += custo_total_transporte - (0.06 * salario_base)
	
if salario_base <= 1317.07:
	INSS = 0.08 * salario_base
elif salario_base > 1317.08  and salario_base <= 2195.12:
	INSS = 0.09 * salario_base
else:
	INSS = 0.11 * salario_base

gasto_do_empregado += 0.12 * salario_base
salario_liquido -= INSS

print "O custo mensal para o empregador é de R$ %.2f" % gasto_do_empregado 
print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liquido
