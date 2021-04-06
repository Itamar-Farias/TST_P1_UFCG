# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

salario = float(raw_input("Valor atual? "))
novo_salario = float(raw_input("Novo valor? "))
print "Reajuste de %.1f%%" % ((100 * (novo_salario - salario)) / salario)
