pessoa = {}
anoatual = 2024
anoaposentadoria = 35
anosxp = 0
idadefinal = 0
pessoa['idade'] = 0
pessoa['nome'] = str(input("Digite o nome: "))
pessoa['ano'] = int(input("Digite o ano de nascimento: "))
pessoa['carteira'] = int(input("Digite a CTPS: "))
pessoa["idade"] = anoatual - pessoa['ano']
print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos de idade.')
if pessoa['carteira'] != 0:
     pessoa['anocontratacao'] = int(input("Digite o ano de contratação: "))
     pessoa['salario'] = float(input("Digite o salário: R$"))
     anosxp = 2024 - pessoa['anocontratacao']
     anoaposentadoria -= anosxp
     idadefinal = pessoa['idade'] + anoaposentadoria
     print(f'Possui {anosxp} anos de experiência, devendo se aposentar em {anoaposentadoria} anos com {idadefinal} anos de idade.')
else:
    print(f'Não possui experiência e precisa de {anoaposentadoria} para se aposentar.')