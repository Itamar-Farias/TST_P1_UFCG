# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

custo_ent = float(raw_input())
disp = float(raw_input()) * custo_ent / 100
lucro = float(raw_input()) * custo_ent / 100
impostos = float(raw_input())  
comissao = float(raw_input())  
descontos = float(raw_input()) 
encargos = float(raw_input())

preco = (custo_ent + disp + lucro) * (100 / (100 - impostos - comissao - descontos -encargos))
print "Preço de venda é R$ %.2f (R$ %.2f + R$ %.2f)" % (preco, (preco - (float(preco) - int(preco))), (float(preco) - int(preco)))
