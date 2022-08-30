tempo = int(input('Quantos anos seu carro tem? '))
if tempo<=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('---FIM---')

idade = int(input('Qual é a sua idade? '))
if idade<=18:
    print('Vc é de menor')
else:
    print('Vc é de maior')


n1 = float(input("Digite nota 1: "))
n2 = float(input('Digite nota 2: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m>=6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

