# coding: utf-8
s = float(raw_input("Quanto é o seu salário? "))
p = float(raw_input("Qual é o percentual de aumento salarial (%)? "))
i = float(raw_input("Qual é a sua contribuição previdenciária (%)? "))
print "Dados do novo salário"
print "==="
print "Salário: R$ %.2f " % (s*(p/100)+s)
x = (((i*(s*(p/100)+s))/100))
y = ((s*(p/100)+s)-x)
print "Contribuição previdenciária: R$ %.2f (%.1f%s)" % (x, i, "%")
print "Salário líquido: R$ %.2f " % y
