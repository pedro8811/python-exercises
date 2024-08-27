class Tree:
   def __init__(self, height):
       self._height = height


pine = Tree(20)
print(pine._height)


class Car:
    def __init__(self, model, brand):
        self.__model = model
        self.__brand = brand

argo = Car('Argo', 'Fiat')
# ERRO print(argo.__model)
