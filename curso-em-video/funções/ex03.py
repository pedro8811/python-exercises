from time import sleep
def contador(i, f, p):
    if p < 0:
        p = p * p
    if p == 0:
        p = 1
    print('-='*30)
    s = i
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i < f:
        while s <= f:
            print(s, end=" ")
            sleep(1)
            s += p
        print("FIM!")
    elif i > f:
        while s >= f:
            print(s, end=" ")
            sleep(1)
            s -= p
        print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)