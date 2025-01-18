import Item

class Almoxarifado:
    def __init__(self, nome):
        self.__nome = nome
        self.__estoque = {}
        self.__valor = 0

    @property
    def estoque(self):
        return self.__estoque
   
    def adicionar_item(self, usuario, nome, estoque, un_medida, preco_un):
        estoque_alt = float(estoque)
        preco_un_alt = float(preco_un)
        valor_estoque = estoque_alt * preco_un_alt
        self.__estoque[nome] = Item.Item(nome, estoque, un_medida, preco_un) #composição com Item aqui
        log = f"Item {nome} criado por {usuario.nome}"       #cria uma string com os dados da operação realizada e retorna para fora da função
        return log
            

    def remover_item(self, usuario, nome):          
        del self.__estoque[nome]
        log = f"Item {nome} removido por {usuario.nome}"
        return log                                              #cria uma string com os dados da operação realizada e retorna para fora da função