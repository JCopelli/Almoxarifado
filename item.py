class Item:
    def __init__(self, nome, estoque, un_medida, preco_un):
        self.__nome = nome
        self.__estoque = estoque
        self.__un_medida = un_medida
        self.__preco_un = preco_un
        self.__valor_estoque = self.__preco_un * self.__estoque

    def mostrar_informacoes(self):
        print(f"Produto: {self.__nome}")
        print(f"Quantidade em estoque: {self.__estoque}")
        print(f"Unidade de medida: {self.__un_medida}")
        print(f"Valor unitário: {self.__preco_un} $ por {self.__un_medida}")
        print(f"Valor em estoque: {self.__valor_estoque}")
        print("")

    def entrada_de_estoque(self, quantidade):
        self.__estoque += quantidade
        self.atualizar_estoque()
        return self.__estoque

    def saida_de_estoque(self, quantidade):
        if quantidade > self.__estoque:
            print("Não é possível retirar a quantidade desejada, pois não há disponível em estoque")
        else:
            self.__estoque -= quantidade
            self.atualizar_estoque()
            return self.__estoque

    @property
    def alterar_valor(self):
        return self.__preco_un

    @alterar_valor.setter
    def alterar_valor(self, valor):
        if valor < 0:
            print("O valor do produto não pode ser negativo")
        else:
            self.__preco_un = valor
            self.atualizar_estoque()
            return self.__preco_un

    def atualizar_estoque(self):
        self._valor_estoque = self.estoque * self._preco_un
        return self.__valor_estoque