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

    def gerar_pdf_estoque(self, nome_arquivo: str):
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        c = canvas.Canvas(nome_arquivo, pagesize=letter)
        c.setFont("Helvetica", 12)

        # Cabeçalho
        c.drawString(100, 750, f"Relatório de Estoque - {self.__nome}")
        c.drawString(100, 735, "----------------------------------------------------------")

        # Títulos das colunas
        c.drawString(100, 715, "Produto")
        c.drawString(250, 715, "Quantidade")
        c.drawString(350, 715, "Unidade de Medida")
        c.drawString(500, 715, "Preço Unitário")
        c.drawString(650, 715, "Valor em Estoque")
        c.drawString(100, 705, "----------------------------------------------------------")

        y_position = 690
        for item in self.__estoque.values():
            c.drawString(100, y_position, item.get_nome())
            c.drawString(250, y_position, str(item.get_estoque()))
            c.drawString(350, y_position, item.get_un_medida())
            c.drawString(500, y_position, f"R$ {item.get_preco_un():.2f}")
            c.drawString(650, y_position, f"R$ {item.get_valor_estoque():.2f}")
            y_position -= 20  # Move para a próxima linha

            if y_position < 50:  # Se a página estiver cheia, cria uma nova página
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = 750

        c.save()