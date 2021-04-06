#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

distancia = float(raw_input(''))
aliquota = float(raw_input(''))

valor = distancia * aliquota + 51
a_vista = valor * 0.75

seis_parcelas = valor * 0.95


print 'Valor da passagem: R$ %.2f' % valor
print
print 'Pagamento:'
print '1. À vista. R$ %.2f' % a_vista
print '2. Em 6 parcelas. Total: R$ %.2f' % seis_parcelas
print '   6 x R$ %.2f' % (seis_parcelas / 6)
print '3. Em 10 parcelas. Total: R$ %.2f' % valor
print '   10 x R$ %.2f' % (valor / 10)
