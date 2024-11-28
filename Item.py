class Item:
    def __init__(self, nome, estoque, un_medida, preco_un, valor_estoque):
        self.__nome = nome
        self.__estoque = estoque
        self.__un_medida = un_medida
        self.__preco_un = preco_un
        self.__valor_estoque = valor_estoque
    
    def mostrar_informacoes(self):
        print(self.__nome)
        print(self.__estoque)
        print(self.__un_medida)
        print(self.__preco_un)
        print(f"{self.__valor_estoque}\n")
