def maior(*values):
    maior = 0
    for pos, x in enumerate(values):
        if pos == 0:
            maior = values[pos]
        if maior < values[pos]:
            maior = values[pos]
    print(f"Dos valores {values}, o maior é {maior}")


maior(1, 2, 8, 5, 7, 6, 4)