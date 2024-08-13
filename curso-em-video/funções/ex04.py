def maior(*values):
    maior = 0
    tam = len(values)
    for pos, x in enumerate(values):
        if pos == 0:
            maior = values[pos]
        if maior < values[pos]:
            maior = values[pos]
    print(values)
    print(f"Dos {tam} valores informados, o maior é {maior}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
