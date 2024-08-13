def fatorial(n,show=None):
    """
     -> Calcula o fatorial de
     :param n: O número a ser calculado.
     :param show: (opcional) mostra ou não a conta.
     :return: O valor do fatorial de um número n.
    """

    f = 0
    c = n
    tot = 1
    print(f'{c}! =', end=" ")
    if show == True:
        for x in range(n, f, -1):
            if x != 1:
                print(f'{x} x', end=" ")
            else:
                print(f'{x}', end=" ")
            tot *= x
        print("=", end=" ")
    print(f"{tot}")


print('-'*40)
# fatorial(6, True)
help(fatorial)