import Item

class Almoxarifado:
    def __init__(self, nome):
        self.__nome = nome
        self.__estoque = {}
        self.__valor = 0

    def get_estoque(self):
        return self.__estoque
        
    def adicionar_item(self):                                    #Pede os dados do Item a ser cadastrado, atribui a variáveis temporárias 
            nome = str(input("Nome: "))                          #e utiliza essas variáveis para criar um objeto Item antes de sair do escopo da função
            estoque = float(input("Estoque: "))
            un_medida = str(input("Unidade de Medida: "))
            preco_un = float(input("Preço Unitário: "))
            valor_estoque = estoque * preco_un
            self.__estoque[nome] = Item.Item(nome, estoque, un_medida, preco_un, valor_estoque) #composição com Item aqui
            print(f"{nome} adicionado ao sistema!")


    def remover_item(self):
        item = input("Qual item deseja remover?")
        if item in self.__estoque:             
            del self.__estoque[item]
            print("Item removido!")
        else:
            print("Item não encontrado!")
    
    def inventario(self):
        for item in self.__estoque:
            item.mostrar_informacoes()