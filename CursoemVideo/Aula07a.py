n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 + n2;
m = n1 * n2;
d = n1 / n2;
di = n1 // n2;
e = n1 ** n2;
print('Soma: {} \nMultiplicação: {} \nDivisão: {:.3f}'.format(s, m, d), end=" ")
print('Div inteira: {} Exp: {}'.format(di, e))