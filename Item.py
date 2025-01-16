class Item:
    def __init__(self, nome, estoque, un_medida, preco_un):
        self.__nome = nome
        self.__estoque = estoque
        self.__un_medida = un_medida
        self.__preco_un = preco_un
        self.__valor_estoque = self.__estoque * self.__preco_un

    def mostrar_informacoes(self):
        print(f"Produto: {self.__nome}")
        print(f"Quantidade em estoque: {self.__estoque}")
        print(f"Unidade de medida: {self.__un_medida}")
        print(f"Valor unitário: R$ {self.__preco_un:.2f} por {self.__un_medida}")
        print(f"Valor em estoque: R$ {self.__valor_estoque:.2f}\n")

    def entrada_de_estoque(self, usuario, quantidade):
        self.__estoque = self.__estoque + float(quantidade)
        self.atualizar_estoque()
        log = f"O item {self.__nome} foi incrementado em {quantidade} {self.__un_medida} pelo usuario {usuario.nome}"
        return log

    def saida_de_estoque(self, usuario, quantidade):
        if float(quantidade) > self.__estoque:
           return False
        else:
            self.__estoque -= float(quantidade)
            self.atualizar_estoque()
            log = f"O item {self.__nome} foi retirado em {quantidade} {self.__un_medida} pelo usuario {usuario.nome}"
            return log

    @property
    def valor_estoque(self):
        return self.__valor_estoque

    @property
    def altera_preco(self):
        return self.__preco_un

    @altera_preco.setter
    def alterar_preco(self, valor):
        if valor < 0:
            print("O valor do produto não pode ser negativo")
        else:
            self.__preco_un = valor
            self.atualizar_estoque()
            return self.__preco_un

    def atualizar_estoque(self):
        self.__valor_estoque = self.__estoque * self.__preco_un
        return self.__valor_estoque
