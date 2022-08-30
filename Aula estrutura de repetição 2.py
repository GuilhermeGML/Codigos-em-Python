c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

p1 = int(input('Digite o primeiro termo de uma razão: '))
r = int(input('Digite a razão da progreção: '))
x = 1
usu = False
while not usu:
    num = int(input('Qual termo deseja saber: '))
    x = p1 + (num - 1) * r
    print('O {} termo vale {}'.format(num, x))
    uzi = str(input('Deseja continuar? [S/N] ')).upper()
    if uzi == 'N':
        usu = True
print('FIM')