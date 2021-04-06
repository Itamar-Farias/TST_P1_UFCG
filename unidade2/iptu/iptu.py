# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

area = float(raw_input("Área construída? "))
aliquota = float(raw_input("Alíquota? "))
print "IPTU: R$ %.2f" % ((area * aliquota) + 35)
print 
print "Pagamento:"
print "1. Quota única. R$ %.2f" % (((area * aliquota) + 35) * 0.75)
print "2. Em 6 parcelas. Total: R$ %.2f" % (((area * aliquota) + 35) * 0.95)
print "   6 x R$ %.2f" % ((((area * aliquota) + 35) * 0.95) / 6)
print "3. Em 10 parcelas. Total: R$ %.2f" % ((area * aliquota) + 35)
print "   10 x R$ %.2f" % (((area * aliquota) + 35) / 10)
