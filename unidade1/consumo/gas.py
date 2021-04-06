print '$ python joao.py' 
pos_inicial = float(raw_input())
litros_inicial = float(raw_input())
pos_final = float(raw_input())
litros_final = float(raw_input())
dist = pos_final - pos_inicial
delta_consumo = litros_inicial - litros_final
print 'O consumo total foi de %.1f Km/l.' % (dist / delta_consumo)
