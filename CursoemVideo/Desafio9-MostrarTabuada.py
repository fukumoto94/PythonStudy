n = int(input('Digite: '))
print('A tabuade de {}:'.format(n))
print('-'*15)
for x in range(1, 11):
    print('{} x {:2} = {}'.format(n, x, n*x))
print('-'*15)