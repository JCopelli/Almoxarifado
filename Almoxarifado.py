import Item
from typing import Dict

class Almoxarifado:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__estoque: Dict[str, Item.Item] = {}
        self.__valor = 0

    @property
    def estoque(self) -> Dict[str, Item.Item]:
        return self.__estoque

    def adicionar_item(self, usuario, nome: str, estoque: float, un_medida: str, preco_un: float) -> str:
        try:
            # Convertendo valores usando lambda para garantir a tipagem correta
            estoque_alt = (lambda x: float(x))(estoque)
            preco_un_alt = (lambda x: float(x))(preco_un)
            
            # Calculando o valor total em estoque
            valor_estoque = (lambda x, y: x * y)(estoque_alt, preco_un_alt)
            
            # Adicionando o item ao estoque (composição com Item)
            self.__estoque[nome] = Item.Item(nome, estoque_alt, un_medida, preco_un_alt)
            
        except ValueError as e:
            return f"Erro ao adicionar o item: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"
        else:
            log = f"Item {nome} criado por {usuario.nome}"
            return log
        finally:
            print(f"O item {nome} foi adicionado ao almoxarifado!")

    def remover_item(self, usuario, nome: str) -> str:
        try:
            if nome not in self.__estoque:
                raise KeyError(f"Item '{nome}' não encontrado no estoque.")
            
            # Removendo o item do estoque
            del self.__estoque[nome]
        
        except KeyError as e:
            return f"Erro ao remover o item: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"
        else:
            log = f"Item {nome} removido por {usuario.nome}"
            return log
        finally:
            print(f"O item {nome} foi removido do almoxarifado!")