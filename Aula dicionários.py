pessoas = {'nome': 'Gui', 'sexo': 'M', 'idade': 18}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
for k in pessoas.keys():
    print(k)
print('-' * 30)
print(pessoas.values())
for k in pessoas.values():
    print(k)
print('-' * 30)
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
# delpessoas['sexo'] == para deletar