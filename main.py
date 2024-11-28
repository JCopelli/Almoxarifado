import Almoxarifado
import pickle

almoxarifado_path = "C:/Users/joaop/OneDrive/Documentos/Almoxarifado/almoxarifado.pkl"

def salvar_alteracoes(almoxarifado):
    try:
        with open(almoxarifado_path,"wb") as f:   #grava o o objeto almoxarifado no arquivo .pkl
            pickle.dump(almoxarifado, f)
            print("Atualizações Salvas")

    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")

def ler_almoxarifado():
    try:
        with open(almoxarifado_path, "rb") as f:
            estoque = pickle.load(f)
            print("Lendo Arquivos\n")
            return estoque
        
    except Exception as e:
        print(f"Erro ao ler o estoque: {e}")
    
def main():

    almoxarifado1 = ler_almoxarifado()
    print(type(almoxarifado1))
    
    opcao = 0

    while True:
        print("---------Menu---------")
        print("\n-> (1) Adicionar Item")
        print("-> (2) Remover Item")
        print("-> (3) Inventário \n")
        print("-> (0) Encerrar")
        print("----------------------------------------")
        opcao = int(input("O que deseja fazer?\n"))

        if opcao == 1:
            almoxarifado1.adicionar_item()
            salvar_alteracoes(almoxarifado1)

        elif opcao == 2:
            almoxarifado1.remover_item()
            salvar_alteracoes(almoxarifado1)

        elif opcao == 3:
            inventario = ler_almoxarifado()
            inventario = inventario.get_estoque()
            for chave, item in inventario.items():
                item.mostrar_informacoes()
        else:
            exit()
    
if __name__ == "__main__":
    main()