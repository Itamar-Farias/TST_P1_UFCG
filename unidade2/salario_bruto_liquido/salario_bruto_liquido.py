# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

nome = raw_input()
quant_hora_extra = float(raw_input())
salario = float(raw_input())
valor_hora_extra = float(raw_input())
salario_bruto = 4 * salario + (quant_hora_extra * valor_hora_extra)
desconto_inss = salario_bruto * 0.12
desconto_inposto_de_renda = salario_bruto * 0.2
salario_liquido = salario_bruto - desconto_inss - desconto_inposto_de_renda
print "O Salário Bruto de %s é de R$ %.2f" % (nome, salario_bruto)
print "O Salário Líquido de %s é de R$ %.2f" % (nome, salario_liquido)
