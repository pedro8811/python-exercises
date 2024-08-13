def leiaInt(x):
    value = input(x)
    while True:
        if value.isnumeric():
            return value
            break
        else:
            print("\033[0;31mERRO, o valor não é númérico.\033[m")
            value = input(x)


    # integer = int(value)
    # print(integer)
    # if type(integer) == typeInt:
    #     return value
    # else:
    #     return 'erro'

print('-'*40)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
