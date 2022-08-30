nome =input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {}'.format(s))
print('A multiplicação vale {}'.format(m))
print('A divisão vale {:.3f}'.format(d))
print('A divisão com resto vale {}'.format(di))
print('A exponenciação vale {}'.format(e))
print('Comando utilizado para não quebrar a linha', end=' ')
print('A linha não foi quebrada')



