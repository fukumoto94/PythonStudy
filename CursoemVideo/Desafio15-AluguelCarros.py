km = float(input('Km rodados: '))
qtdDias = int(input('Quantidade de dias Alugado: '))
price = (km*0.15) + (qtdDias*60)
print('Km rodados: {}\nQuantidade dias: {}\nValor a ser pago: {}'.format(km, qtdDias, price))