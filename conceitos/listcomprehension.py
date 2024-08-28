import pprint

lista_precos = [500, 1500, 2000, 100, 25]

# Caso 1
nova_lista_precos = []
for x in lista_precos:
    nova_lista_precos.append(x * 2)
# print(nova_lista_precos)

# Caso 2
nova_lista_precos2 = [x * 2 for x in lista_precos]
# print(nova_lista_precos)

# Caso 3
imposto = []
for x in lista_precos:
    if x > 1000:
        imposto.append(x * 0.5)
# print(imposto)

# Caso 4
imposto2 = [x * 0.5 for x in lista_precos if x > 1000]
# print(imposto2)

# numeros pares
evens = [number for number in range(50) if number % 2 == 0]
# print(evens)

# string que começam com "a" e terminam com "y"
options = ["any", "albany", "apple", "world", "hello", ""]
valid_strings = [
    word
    for word in options
    if len(word) >= 2
    if word[0] == "a"
    if word[-1] == "y"
]
# print(valid_strings)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# print(flattened)

# for row in matrix:
#     for num in row:
#         flattened.append(num)

categories = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
# print(categories)

printer = pprint.PrettyPrinter()

lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
# for a in range(5):
#     l1 = []
#     for b in range(5):
#         l2 = []
#         for num in range(5):
#             l2.append(num)
#         l1.append(l2)
#     lst.append(l1)

printer.pprint(lst)
