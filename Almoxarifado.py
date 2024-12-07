import Item

class Almoxarifado:
    def __init__(self, nome):
        self.__nome = nome
        self.__estoque = {}
        self.__valor = 0

    @property
    def estoque(self):
        return self.__estoque
   
    def adicionar_item(self, usuario):                                    #Pede os dados do Item a ser cadastrado, atribui a variáveis temporárias 
        if usuario == None:
           print("O usuário não autenticado. Efetue o login para ter acesso a essa função!")
           log = f"Usuario não autenticado tentou adicionar um item"
           return log
        else:
            nome = input("Nome: ")                          #e utiliza essas variáveis para criar um objeto Item antes de sair do escopo da função
            estoque = float(input("Estoque: "))
            un_medida = str(input("Unidade de Medida: "))
            preco_un = float(input("Preço Unitário: "))
            valor_estoque = estoque * preco_un
            self.__estoque[nome] = Item.Item(nome, estoque, un_medida, preco_un) #composição com Item aqui
            print(f"{nome} adicionado ao sistema!")
            log = f"Item {nome} adicionado por {usuario.nome}"       #cria uma string com os dados da operação realizada e retorna para fora da função
            return log
            

    def remover_item(self, usuario):
        if usuario == None:
            print("O usuário não autenticado. Efetue o login para ter acesso a essa função!")
            log = f"Usuario não autenticado tentou remover um item"
            return log
        else:
            item = input("Qual item deseja remover? ")
            if item in self.__estoque:        
                del self.__estoque[item]
                print("Item removido!")
                log = f"Item {item} removido por {usuario.nome}"
                return log                                              #cria uma string com os dados da operação realizada e retorna para fora da função
            else:
                print("Item não encontrado!")
                log = f"{usuario.nome} tentou buscar {item}, item não encontrado"
            
