# coding: utf -8
# Itamar da Silva Farias 115210021
# Programação I

ano_inicial = int(raw_input())
ano_final   = int(raw_input())

faixa = ano_final - ano_inicial + 1
qtde_abaixo = 0
qtde_acima = 0
soma_abaixo = 0
soma_acima = 0

for i in range(faixa):
	salario = float(raw_input())
	if salario < 100:
		qtde_abaixo += 1
		soma_abaixo += salario	
	if salario > 100:
		qtde_acima += 1
		soma_acima += salario

if soma_abaixo == 0:
	media_acima = soma_acima / float(qtde_acima)
	print '0 ano(s) abaixo (0% dos anos)'
	print '%d ano(s) acima (100%% dos anos)' % qtde_acima
	print 'média dos anos acima: U$ %.2f' % media_acima
else:
	media_abaixo = soma_abaixo / float(qtde_abaixo)
	media_acima = soma_acima / float(qtde_acima)
	percent_abaixo = qtde_abaixo * 100 / (qtde_abaixo + qtde_acima)
	percent_acima = 100 - percent_abaixo
	print '%d ano(s) abaixo (%d%% dos anos)' % (qtde_abaixo, percent_abaixo)
	print 'média dos anos abaixo: U$ %.2f' % media_abaixo
	print '%d ano(s) acima (%d%% dos anos)' % (qtde_acima, percent_acima)
	print 'média dos anos acima: U$ %.2f' % media_acima
