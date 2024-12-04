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
        print(f"Valor unitário: {self.__preco_un} $ por {self.__un_medida}")
        print(f"Valor em estoque: {self.__valor_estoque}\n")

    def entrada_de_estoque(self, usuario):
        if usuario == None:
            print("O usuário não foi autenticado. Efetue o login para ter acesso a essa função!")
            log = f"Usuario não autenticado tentou incrementar um item."
            return log

        quantidade = input("Digite a quantidade que deseja incrementar: ")
        self.__estoque = self.__estoque + float(quantidade)
        self.atualizar_estoque()
        log = f"O item {self.__nome} foi incrementado em {quantidade} {self.__un_medida} pelo usuario {usuario.nome}"
        return log

    def saida_de_estoque(self, usuario):
        if usuario == None:
            print("O usuário não foi autenticado. Efetue o login para ter acesso a essa função!")
            log = f"Usuario não autenticado tentou retirar um item."
            return log

        quantidade = input("Digite a quantidade que deseja retirar: ")
        if float(quantidade) > self.__estoque:
            print("Não é possível retirar a quantidade desejada, pois não há disponível em estoque")
        else:
            self.__estoque -= float(quantidade)
            self.atualizar_estoque()
            log = f"O item {self.__nome} foi retirado em {quantidade} {self.__un_medida} pelo usuario {usuario.nome}"
            return log

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
        self.__valor_estoque = self.__estoque * self.__preco_un
        return self.__valor_estoque
