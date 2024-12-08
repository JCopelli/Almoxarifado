import Almoxarifado
import pickle
import Usuario
import pwinput
import datetime
import os

almoxarifado_path = "C:/Users/TEMP.CCE.140/Documents/Almoxarifado/almoxarifado.pkl"

usuarios_path = "C:/Users/TEMP.CCE.140/Documents/Almoxarifado/usuarios.pkl"

log_path = "C:/Users/TEMP.CCE.140/Documents/Almoxarifado/log.txt"

def salvar_alteracoes(dado, caminho):
    try:
        with open(caminho,"wb") as f:   #grava o o objeto almoxarifado no arquivo .pkl
            pickle.dump(dado, f)
            print("Atualizações Salvas")

    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")

def registrar_log(log):
    with open(log_path, "a") as registros:  #grava os logs em um arquivo .txt
        registros.write(f"{log} às {datetime.datetime.now()}\n")

def ler_dados(caminho):
    try:
        with open(caminho, "rb") as f:
            leitura = pickle.load(f)
            print("Lendo Arquivos\n")
            return leitura
        
    except Exception as e:
        print(f"Erro ao ler o banco de dados: {e}")

def cadastro_usuario(usuarios):
    nome = input("Digite o nome do novo usuario: ")
    senha = pwinput.pwinput(prompt = "Digite a senha do novo usuario: ", mask = "*")
    usuarios[nome] = Usuario.Usuario(nome, senha)
    salvar_alteracoes(usuarios, usuarios_path)
    log = f"Usuario {nome} criado"
    return log

def continuar_acao():
    input("Pressione enter para continuar")

def main():

    usuarios = {}
    usuario_atual = None
    almoxarifado1 = ler_dados(almoxarifado_path)
    usuarios = ler_dados(usuarios_path) 
    print(type(usuarios))
    print(type(almoxarifado1))

    opcao = 0

    while True:
        os.system("cls")
        print("---------Menu---------")
        print("\n-> (1) Login") 
        print("-> (2) Alterar senha") #Requer Autenticação
        print("-> (3) Cadastrar Usuario\n")
        print("-> (4) Consultar Estoque") # FINALIZADO
        print("-> (5) Entrada no estoque")#Requer Autenticação
        print("-> (6) Saída do estoque")#Requer Autenticação
        print("-> (7) Cadastrar Item") #Requer Autenticação
        print("-> (8) Remover Item\n") #Requer Autenticação
        print("-> (9) Logout ")   #Requer Autenticação
        print("-> (0) Encerrar")
        print("----------------------------------------")
        opcao = int(input("O que deseja fazer?\n"))

        if opcao == 1:
            os.system("cls")
            print("---------Login---------\n")
            usuario = input("Usuário: ")
            if usuario not in usuarios:
                print("Usuário não cadastrado!")
                continuar_acao()
            else:
                usuarios[usuario].login()
                usuario_atual = usuarios[usuario]
                continuar_acao()

        elif opcao == 2:
            pass
            
        elif opcao == 3:
            pass

        elif opcao == 4:
            os.system("cls")
            print("---------Estoque---------\n")
            inventario = ler_dados(almoxarifado_path)
            inventario = inventario.estoque
            for chave, item in inventario.items():
                item.mostrar_informacoes()
            continuar_acao()
            
        elif opcao == 5:
            os.system("cls")
            print("---------Entrade de estoque---------\n")
            item_entrada = input ("Digite o item que deseja incrementar: ")
            if item_entrada in almoxarifado1.estoque:
                log = almoxarifado1.estoque[item_entrada].entrada_de_estoque(usuario_atual)
                registrar_log(log)
                salvar_alteracoes(almoxarifado1, almoxarifado_path)
                continuar_acao()
            else:
                print("O item que deseja incrementar não existe no estoque!")
                continuar_acao()


        elif opcao == 6:
            os.system("cls")
            print("---------Saída de estoque---------\n")
            item_saida = input ("Digite o item que deseja retirar: ")
            if item_saida in almoxarifado1.estoque:
                log = almoxarifado1.estoque[item_saida].saida_de_estoque(usuario_atual)
                registrar_log(log)
                salvar_alteracoes(almoxarifado1, almoxarifado_path)
                continuar_acao()
            else:
                print("O item que deseja incrementar não existe no estoque!")
                continuar_acao()

        elif opcao == 7:
            os.system("cls")
            print("---------Cadastro de item---------\n")
            log = almoxarifado1.adicionar_item(usuario_atual)
            registrar_log(log)
            salvar_alteracoes(almoxarifado1, almoxarifado_path)
            continuar_acao()

        elif opcao == 8:
            os.system("cls")
            print("---------Remoção de item---------\n")
            log = almoxarifado1.remover_item(usuario_atual)
            registrar_log(log)
            salvar_alteracoes(almoxarifado1, almoxarifado_path)
            continuar_acao()

        elif opcao == 9:
            pass

        else:
            os.system("cls")
            exit()
    
if __name__ == "__main__":
    main()
