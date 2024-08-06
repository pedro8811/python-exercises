def escreva(txt, num):
    print('~'*num)
    print(f"{txt:^{num}s}")
    print('~'*num)

escreva('Olá, Mundo!',  25)
escreva("Curso de Python no YouTube", 30)
escreva("Cev", 8)