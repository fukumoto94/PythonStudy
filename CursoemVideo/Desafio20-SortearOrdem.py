import random

listaAlunos = []
numRands = []
for x in range(0, 4):
    listaAlunos.append(input('Nome aluno:'))
random.shuffle(listaAlunos)
print(listaAlunos)


