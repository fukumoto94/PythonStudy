larg = float(input('Largura: '))
alt = float(input('Altura: '))
area = larg*alt;
qtdTinta = area/2;
print('Parede de largura: {}  e altura: {} tem área de {}m2 e precisa de {}l de tinta'
      .format(larg, alt, area, qtdTinta))