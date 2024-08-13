anoatual = 2024


def voto(year):
    idade = anoatual - year
    print(f'Com {idade} anos: ', end="")
    if idade < 16:
        return 'NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL.'
    else:
        return 'VOTO OBRIGATÓRIO.'


ano = int(input("Digite o ano de nascimento: "))
print(voto(ano))