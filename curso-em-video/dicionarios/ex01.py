pessoa = dict()
pessoa['Nome'] = str(input("Nome: "))
pessoa['Media'] = float(input("Media: "))
if pessoa['Media'] >= 7:
    pessoa['Situação'] = 'Aprovado'
else:
    pessoa['Situação'] = 'Recuperação'
for k, v in pessoa.items():
    print(f'{k} é igual a {v}')