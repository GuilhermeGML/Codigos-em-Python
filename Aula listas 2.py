test = list()
test.append('Gustavo')
test.append(40)
galera = list()
galera.append(test[:])
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])
print(test)
print(galera)

turma = [['João', 19], ['Maria', 22], ['Gui', 17], ['Julia', 14]]
for p in turma:
    print(p)
    print(p[0])
    print(p[1])

galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
print(galera)