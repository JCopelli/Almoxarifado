class Item:
    def __init__(self, nome, estoque, un_medida, preco_un):
        try:
            self.__nome = nome
            self.__estoque = float(estoque)
            self.__un_medida = un_medida
            self.__preco_un = float(preco_un)
            self.__valor_estoque = float(self.__estoque * self.__preco_un)
        except ValueError as e:
            raise ValueError(f"Erro ao inicializar o item: {e}")

    def mostrar_informacoes(self):
        try:
            print(f"Produto: {self.__nome}")
            print(f"Quantidade em estoque: {self.__estoque}")
            print(f"Unidade de medida: {self.__un_medida}")
            print(f"Valor unitário: R$ {self.__preco_un:.2f} por {self.__un_medida}")
            print(f"Valor em estoque: R$ {self.__valor_estoque:.2f}\n")
        except Exception as e:
            print(f"Erro ao mostrar informações do item: {e}")

    def entrada_de_estoque(self, usuario, quantidade):
        try:
            quantidade = float(quantidade)
            self.__estoque += quantidade
            self.atualizar_estoque()
            log = f"O item {self.__nome} foi incrementado em {quantidade} {self.__un_medida} pelo usuário {usuario.nome}"
            return log
        except ValueError as e:
            return f"Erro ao adicionar ao estoque: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"
        finally:
            print(f"Operação de entrada de estoque finalizada para o item: {self.__nome}")

    def saida_de_estoque(self, usuario, quantidade):
        try:
            quantidade = float(quantidade)
            if quantidade > self.__estoque:
                return f"Erro: quantidade solicitada ({quantidade}) maior que o estoque disponível ({self.__estoque})"
            self.__estoque -= quantidade
            self.atualizar_estoque()
            log = f"O item {self.__nome} foi retirado em {quantidade} {self.__un_medida} pelo usuário {usuario.nome}"
            return log
        except ValueError as e:
            return f"Erro ao retirar do estoque: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"
        finally:
            print(f"Operação de saída de estoque finalizada para o item: {self.__nome}")

    @property
    def valor_estoque(self):
        return self.__valor_estoque

    @property
    def altera_preco(self):
        return self.__preco_un

    @altera_preco.setter
    def alterar_preco(self, valor):
        try:
            valor = float(valor)
            if valor < 0:
                raise ValueError("O valor do produto não pode ser negativo")
            self.__preco_un = valor
            self.atualizar_estoque()
            return self.__preco_un
        except ValueError as e:
            print(f"Erro ao alterar o preço: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        finally:
            print(f"Operação de alteração de preço finalizada para o item: {self.__nome}")

    def atualizar_estoque(self):
        try:
            self.__valor_estoque = self.__estoque * self.__preco_un
            return self.__valor_estoque
        except Exception as e:
            print(f"Erro ao atualizar valor do estoque: {e}")

    @property
    def nome(self):
        return self.__nome

    @property
    def estoque(self):
        return self.__estoque

    @property
    def un_medida(self):
        return self.__un_medida

    @property
    def preco_un(self):
        return self.__preco_un

    @property
    def valor_estoque(self):
        return self.__valor_estoque
