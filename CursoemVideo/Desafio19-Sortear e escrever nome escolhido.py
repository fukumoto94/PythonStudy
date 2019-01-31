import random
aluno = []

for x in range(0, 4):
    aluno.append(input('Nome do aluno: '))
nr = random.choice(aluno);


print('Alunos: {}, {}, {}, {} e o sorteado é: {}'.format(aluno[0], aluno[1], aluno[2], aluno[3], nr))