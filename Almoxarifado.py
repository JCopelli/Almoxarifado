import Item

class Almoxarifado:
    def __init__(self, nome):
        self.__nome = nome
        self.__estoque = {}
        self.__valor = 0

    @property
    def estoque(self):
        return self.__estoque
   
    def adicionar_item(self, usuario, nome, estoque, un_medida, preco_un):                                    #Pede os dados do Item a ser cadastrado, atribui a variáveis temporárias 
        # if usuario == None:
        #    print("O usuário não foi autenticado. Efetue o login para ter acesso a essa função!")
        #    log = f"Usuario não autenticado tentou adicionar um item"
        #    return log
        # else:
            # nome = input("Nome: ")                          #e utiliza essas variáveis para criar um objeto Item antes de sair do escopo da função
            # estoque = float(input("Estoque: ").replace(',',"."))
            # un_medida = str(input("Unidade de Medida: "))
            # preco_un = float(input("Preço Unitário: ").replace(',',"."))
        estoque_alt = float(estoque)
        preco_un_alt = float(preco_un)
        valor_estoque = estoque_alt * preco_un_alt
        self.__estoque[nome] = Item.Item(nome, estoque, un_medida, preco_un) #composição com Item aqui
        log = f"Item {nome} criado por {usuario.nome}"       #cria uma string com os dados da operação realizada e retorna para fora da função
        return log
            

    def remover_item(self, usuario, nome):
        # if usuario == None:
        #     print("O usuário não foi autenticado. Efetue o login para ter acesso a essa função!")
        #     log = f"Usuario não autenticado tentou adicionar um item"
        #     return log
        # else:
        #     item = input("Qual item deseja remover? ")
        #     if item in self.__estoque:             
        del self.__estoque[nome]
        log = f"Item {nome} removido por {usuario.nome}"
        return log                                              #cria uma string com os dados da operação realizada e retorna para fora da função
            # else:
            #     print("Item não encontrado!")
            #     log = f"{usuario.nome} tentou buscar {item}, item não encontrado"
            
