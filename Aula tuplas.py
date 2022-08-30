lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3])
print(lanche[1:3])
print(lanche[1:])
print(lanche[:3])
print(lanche[-2:])
print(lanche[:-2])
for c in lanche:
    print(f'Eu vou comer {c}'),
print('Comi muito')
for c in range(0, len(lanche)):
    print(f'Comi {lanche[c]}')
for pos, c in enumerate(lanche):
    print(f'Comi {c}, na posição {pos}')
print(sorted(lanche))