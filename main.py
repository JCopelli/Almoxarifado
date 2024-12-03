import Almoxarifado
import pickle
import Usuario
import pwinput
import datetime

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

def main():

    usuarios = {}
    usuario_atual = None
    almoxarifado1 = ler_dados(almoxarifado_path)
    usuarios = ler_dados(usuarios_path) 
    print(type(usuarios))
    print(type(almoxarifado1))

    opcao = 0

    while True:
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
            usuario = input("Usuário: ")
            if usuario not in usuarios:
                print("Usuário não cadastrado!")
            else:
                usuarios[usuario].login()
                usuario_atual = usuarios[usuario]

        elif opcao == 2:
            pass
            
        elif opcao == 3:
            pass

        elif opcao == 4:
            inventario = ler_dados(almoxarifado_path)
            inventario = inventario.estoque
            for chave, item in inventario.items():
                item.mostrar_informacoes()
            
        elif opcao == 5:
            item_entrada = input ("Digite o item que deseja incrementar: ")
            if item_entrada in almoxarifado1.estoque:
                almoxarifado1.estoque[item_entrada].entrada_de_estoque()
                salvar_alteracoes(almoxarifado1, almoxarifado_path)
            else:
                print("O item que deseja incrementar não existe no estoque!")


        elif opcao == 6:
            item_saida = input ("Digite o item que deseja retirar: ")
            if item_saida in almoxarifado1.estoque:
                almoxarifado1.estoque[item_saida].saida_de_estoque()
                salvar_alteracoes(almoxarifado1, almoxarifado_path)
            else:
                print("O item que deseja incrementar não existe no estoque!")

        elif opcao == 7:
            log = almoxarifado1.adicionar_item(usuario_atual)
            registrar_log(log)
            salvar_alteracoes(almoxarifado1, almoxarifado_path)

        elif opcao == 8:
            log = almoxarifado1.remover_item(usuario_atual)
            registrar_log(log)
            salvar_alteracoes(almoxarifado1, almoxarifado_path)

        elif opcao == 9:
            pass

        else:
            exit()
    
if __name__ == "__main__":
    main()
