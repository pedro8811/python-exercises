def leiaInteiro(msg):
    while True:
        try:
            entrada = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return entrada


def leiaFloat(msg):
    while True:
        try:
            entrada = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário não digitou o valor e finalizou o programa.\033[m')
            return 0
        else:
            return entrada


def resultado(i, f):
    print(f'O valor inteiro digitado foi {i} e o real foi {f}')


n1 = leiaInteiro("Digite um inteiro: ")
n2 = leiaFloat("Digite um float: ")
resultado(n1, n2)
