from math import hypot

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

print('Hipotenusa: {:.2f}'.format(hypot(co, ca)))
