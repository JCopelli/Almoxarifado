import Almoxarifado 
import pickle
import Usuario
import Item
import pwinput
import datetime
import os


dir = os.getcwd()
def inicializa_pkl(objetos):

    db_path = os.path.join(dir, f"{objetos}.pkl")

    if not os.path.exists(db_path):
        with open(db_path, "wb") as db:
            print(f"--- Banco {objetos} criado ---")
            return db_path
    else:
        return db_path

def inicializa_txt(objetos):

    db_path = os.path.join(dir, f"{objetos}.txt")

    if not os.path.exists(db_path):
        with open(db_path, "w") as db:
            db.write("")
            print(f"--- Banco {objetos} criado ---")
            return db_path
    else:
        return db_path

almoxarifado_path = inicializa_pkl("almoxarifado")

usuarios_path = inicializa_pkl("usuarios")

log_path = inicializa_txt("log")

def salvar_alteracoes(dado, caminho):
    try:
        with open(caminho,"wb") as f:   #grava o o objeto almoxarifado no arquivo .pkl
            pickle.dump(dado, f)

    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")

def registrar_log(log):
    with open(log_path, "a") as registros:  # Grava os logs em um arquivo .txt
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")  # Formata o timestamp para incluir apenas horas e minutos
        registros.write(f"{log} às {timestamp}\n")

def ler_dados(caminho):
    try:
        with open(caminho, "rb") as f:
            leitura = pickle.load(f)
            return leitura
        
    except Exception as e:
        print(f"Erro ao ler o banco de dados: {e}")

def cadastro_usuario(usuarios, nome, senha):
    usuarios[nome] = Usuario.Usuario(nome, senha)
    salvar_alteracoes(usuarios, usuarios_path)
    log = f"Usuario {nome} criado"
    return log

def continuar_acao():
    input("Pressione enter para continuar")

def main():

    usuarios = ler_dados(usuarios_path)
    if usuarios == None:
        usuarios = {}
        usuarios["admin"] = Usuario.Usuario("admin", "admin")
        salvar_alteracoes(usuarios, usuarios_path)
    
    usuario_atual = None


    almoxarifado1 = ler_dados(almoxarifado_path)
    if almoxarifado1 == None:
        almoxarifado1 = Almoxarifado.Almoxarifado(input("Digite um nome para o novo almoxarifado: "))
        salvar_alteracoes(almoxarifado1, almoxarifado_path)

    opcao = 0

    while True:
        #os.system("cls") #limpa o ternminal
        print("---------Menu---------")
        print("\n-> (1) Login") 
        print("-> (2) Alterar senha") #Requer Autenticação
        print("-> (3) Cadastrar Usuario\n")
        print("-> (4) Consultar Estoque") 
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
                log = usuarios[usuario].login()
                registrar_log(log)
                usuario_atual = usuarios[usuario]
                continuar_acao()

        elif opcao == 2:
            if usuario_atual == None: 
                print("você não está conectado!")
                log = "Usuario não autenticado tentou modificar senha."
                registrar_log(log)
                continuar_acao()
            else:
                log = usuario_atual.alterar_senha(usuario_atual)
                registrar_log(log)
                salvar_alteracoes(usuarios, usuarios_path)
                continuar_acao()
            
        elif opcao == 3:
            nome = input("Digite o nome do novo usuario: ")
            senha = pwinput.pwinput(prompt = "Digite a senha do novo usuario: ", mask = "*")
            salvar_alteracoes(usuarios, usuarios_path)
            log = cadastro_usuario(usuarios, nome, senha)
            registrar_log(log)
            continuar_acao()

        elif opcao == 4:
            os.system("cls")
            print("---------Estoque---------\n")
            almoxarifado1 = ler_dados(almoxarifado_path)
            if not almoxarifado1.estoque:
                print("Almoxarifado Vazio")
            else:
                estoque = almoxarifado1.estoque
                total = 0
                for chave, item in estoque.items():
                    item.mostrar_informacoes()
                    total += item.valor_estoque
                print(f"-----------Valor Total em Estoque------------- \nR$ {total:.2f}\n")
            continuar_acao()
            
        elif opcao == 5:
            os.system("cls")
            print("---------Entrada de estoque---------\n")
            item_entrada = input ("Digite o item que deseja incrementar: ")
            if item_entrada in almoxarifado1.estoque:
                log = almoxarifado1.estoque[item_entrada].entrada_de_estoque(usuario_atual)
                registrar_log(log)
                salvar_alteracoes(almoxarifado1, almoxarifado_path)
                continuar_acao()
            else:
                print("\nEsse item não existe no estoque!")
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
                print("\nEsse item não existe no estoque!")
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
            if usuario_atual == None:
                print("Você não está conectado!")
                log = f"Usuario não autenticado tentou se desconectar."
                return log
            else:
                log = usuario_atual.logout(usuario_atual)
                registrar_log(log)
                salvar_alteracoes(usuarios, usuarios_path)
                usuario_atual = None
                continuar_acao()

        else:
            os.system("cls")
            exit()
    
if __name__ == "__main__":
    main()
