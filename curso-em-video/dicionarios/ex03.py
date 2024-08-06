pessoa = dict()
anoatual = 2024
anoaposentadoria = 35
anosxp = 0
idadefinal = 0
pessoa['nome'] = str(input("Digite o nome: "))
pessoa['idade'] = 0
ano = int(input("Digite o ano de nascimento: "))
pessoa['ctps'] = int(input("Digite a CTPS: "))
pessoa["idade"] = anoatual - ano

if pessoa['ctps'] != 0:
     pessoa['anocontratacao'] = int(input("Digite o ano de contratação: "))
     pessoa['salario'] = float(input("Digite o salário: R$"))
     pessoa["anosxp"] = 2024 - pessoa['anocontratacao']
     anoaposentadoria -= pessoa["anosxp"]
     idadefinal = pessoa['idade'] + anoaposentadoria
     print('=-'*15, end="")
     print('-='*15)
     print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos de idade.')
     print(f'Possui {pessoa["anosxp"]} anos de experiência, salário de R${pessoa["salario"]} devendo se aposentar em {anoaposentadoria} anos com {idadefinal} anos de idade.')
else:
     print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos de idade.')
     print(f'Não possui experiência e precisa de {anoaposentadoria} para se aposentar.')

# for k, v in pessoa.items():
#      print(f'- {k} tem o valor {v}')