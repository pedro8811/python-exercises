def area(b, a):
    total = b * a
    print(f'A área de um terreno {b:.1f}x{a:.1f} é igual a {total:.1f}m².')

base = float(input("Digite a base do terreno (m): "))
altura = float(input("Digite a altura do terreno (m): "))
area(base, altura)