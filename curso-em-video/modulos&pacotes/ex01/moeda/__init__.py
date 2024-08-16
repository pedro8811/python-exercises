def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def aumentar(n, x, format=False):
    """
    :param n: preço a ser aumentado
    :param x: % de aumento
    :param format: formatar monetário ou não
    :return: valor aumentado
    """
    res = n * (x / 100)
    n += res
    return moeda(n) if format is True else n


def diminuir(n, x, format=False):
    """
    :param n: preço a ser reduzido
    :param x: % de redução
    :param format: formatar monetário ou não
    :return: valor reduzido
    """
    res = n * (x / 100)
    n -= res
    return moeda(n) if format else n


def dobro(n, format=False):
    """
    :param n: preço
    :param format: formatar monetário ou não
    :return: valor em dobro
    """
    return moeda(n * 2) if format else n * 2


def metade(n, format=False):
    """
    :param n: preço
    :param format: formatar monetário ou não
    :return: valor pela metade
    """
    return moeda(n / 2) if format else n / 2


def resumo(n, aumento, diminui):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(n)}.')
    print(f'Dobro do preço: {dobro(n, True)}.')
    print(f'Metade do preço: {metade(n, True)}.')
    print(f'{aumento}% de aumento: {aumentar(n, aumento, True)}')
    print(f'{diminui}% de redução: {diminuir(n, diminui, True)}')

