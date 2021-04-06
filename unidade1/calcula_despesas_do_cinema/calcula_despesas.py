# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

dia =  raw_input()
orcamento =  float(raw_input())
adultos =  float(raw_input())
criancas =  float(raw_input())
pizza = float(raw_input())
refrigerante = float(raw_input())
estacionamento = float(raw_input())
cinema = float(raw_input())

gastos_alimentacao = pizza + refrigerante
gastos_cinema =  (((cinema * adultos )) + (criancas * (cinema / 2.0)) + (criancas + adultos) * 2.0)
gastos_total = gastos_cinema + gastos_alimentacao + estacionamento

print "Dia da semana? Orcamento? R$ Numero de adultos? Numero de criancas? Preco da pizza? R$ Preco do refrigerante? R$ Preco do estacionamento? R$ Preco do ingresso do cinema? R$" + " " + "========== Despesas de " + dia + " =========="
print "Despesas com alimentacao: R$ " + str(gastos_alimentacao)
print "Despesas com cimena: R$ " + str(gastos_cinema)
print "Despesas por pessoa: R$ " + str(gastos_total / (criancas + adultos))
print "Saldo disponivel: " + str(orcamento - gastos_total)
