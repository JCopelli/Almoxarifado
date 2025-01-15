import Almoxarifado 
import pickle
import Usuario
import Item
import pwinput
import datetime
import os
import customtkinter as ctk


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

    usuario_atual = None

    usuarios = ler_dados(usuarios_path)
    if usuarios == None:
        usuarios = {}
        usuarios["admin"] = Usuario.Usuario("admin", "admin")
        salvar_alteracoes(usuarios, usuarios_path)

    almoxarifado1 = ler_dados(almoxarifado_path)
    if almoxarifado1 == None:
        almoxarifado1 = Almoxarifado.Almoxarifado(input("Digite um nome para o novo almoxarifado: "))
        salvar_alteracoes(almoxarifado1, almoxarifado_path)

    # while True:
    #     #os.system("cls") #limpa o ternminal
    #     print("---------Menu---------")
    #     print("\n-> (1) Login") 
    #     print("-> (2) Alterar senha") #Requer Autenticação
    #     print("-> (3) Cadastrar Usuario\n")
    #     print("-> (4) Consultar Estoque") 
    #     print("-> (5) Entrada no estoque")#Requer Autenticação
    #     print("-> (6) Saída do estoque")#Requer Autenticação
    #     print("-> (7) Cadastrar Item") #Requer Autenticação
    #     print("-> (8) Remover Item\n") #Requer Autenticação
    #     print("-> (9) Logout ")   #Requer Autenticação
    #     print("-> (0) Encerrar")
    #     print("----------------------------------------")
    #     opcao = int(input("O que deseja fazer?\n"))

        # if opcao == 1:
    def logar():
        
        usuario = campo_usuario.get()
        if usuario not in usuarios:
            label_msg_login.configure(text="Usuário não cadastrado!", text_color="red" )
        else:
            senha = campo_senha.get()
            log = usuarios[usuario].login(senha)
            if log == False:
                label_msg_login.configure(text="Senha Incorreta, tente novamente", text_color="red")
            else:
                label_msg_login.configure(text=f"Bem-vindo, {usuario}", text_color="green")
                registrar_log(f"Usuário {usuario} conectado")
                usuario_atual = usuarios[usuario]

        # elif opcao == 2:
        #     if usuario_atual == None: 
        #         print("você não está conectado!")
        #         log = "Usuario não autenticado tentou modificar senha."
        #         registrar_log(log)
        #         continuar_acao()
        #     else:
        #         log = usuario_atual.alterar_senha(usuario_atual)
        #         registrar_log(log)
        #         salvar_alteracoes(usuarios, usuarios_path)
        #         continuar_acao()

    

        # elif opcao == 4:
        #     os.system("cls")
        #     print("---------Estoque---------\n")
        #     almoxarifado1 = ler_dados(almoxarifado_path)
        #     if not almoxarifado1.estoque:
        #         print("Almoxarifado Vazio")
        #     else:
        #         estoque = almoxarifado1.estoque
        #         total = 0
        #         for chave, item in estoque.items():
        #             item.mostrar_informacoes()
        #             total += item.valor_estoque
        #         print(f"-----------Valor Total em Estoque------------- \nR$ {total:.2f}\n")
        #     continuar_acao()
            
        # elif opcao == 5:
        #     os.system("cls")
        #     print("---------Entrada de estoque---------\n")
        #     item_entrada = input ("Digite o item que deseja incrementar: ")
        #     if item_entrada in almoxarifado1.estoque:
        #         log = almoxarifado1.estoque[item_entrada].entrada_de_estoque(usuario_atual)
        #         registrar_log(log)
        #         salvar_alteracoes(almoxarifado1, almoxarifado_path)
        #         continuar_acao()
        #     else:
        #         print("\nEsse item não existe no estoque!")
        #         continuar_acao()


        # elif opcao == 6:
        #     os.system("cls")
        #     print("---------Saída de estoque---------\n")
        #     item_saida = input ("Digite o item que deseja retirar: ")
        #     if item_saida in almoxarifado1.estoque:
        #         log = almoxarifado1.estoque[item_saida].saida_de_estoque(usuario_atual)
        #         registrar_log(log)
        #         salvar_alteracoes(almoxarifado1, almoxarifado_path)
        #         continuar_acao()
        #     else:
        #         print("\nEsse item não existe no estoque!")
        #         continuar_acao()

        # elif opcao == 7:
        #     os.system("cls")
        #     print("---------Cadastro de item---------\n")
        #     log = almoxarifado1.adicionar_item(usuario_atual)
        #     registrar_log(log)
        #     salvar_alteracoes(almoxarifado1, almoxarifado_path)
        #     continuar_acao()

        # elif opcao == 8:
        #     os.system("cls")
        #     print("---------Remoção de item---------\n")
        #     log = almoxarifado1.remover_item(usuario_atual)
        #     registrar_log(log)
        #     salvar_alteracoes(almoxarifado1, almoxarifado_path)
        #     continuar_acao()

        # elif opcao == 9:      
        #     if usuario_atual == None:
        #         print("Você não está conectado!")
        #         log = f"Usuario não autenticado tentou se desconectar."
        #         return log
        #     else:
        #         log = usuario_atual.logout(usuario_atual)
        #         registrar_log(log)
        #         salvar_alteracoes(usuarios, usuarios_path)
        #         usuario_atual = None
        #         continuar_acao()

        # else:
        #     os.system("cls")
        #     exit()
    
    def abrir_tela_criar_usuario():
        # Criar nova janela para "Criar Usuário"
        janela_criar_usuario = ctk.CTkToplevel(janela)
        janela_criar_usuario.title("Sistema de Almoxarifado - Criar Usuário")
        janela_criar_usuario.geometry("400x400")
        janela_criar_usuario.resizable(width=False, height=False)
        janela_criar_usuario.after(50,janela_criar_usuario.deiconify)
        janela_criar_usuario.focus_force()

        # Configurar o layout da janela
        janela_criar_usuario.grid_columnconfigure(0, weight=1)
        janela_criar_usuario.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkLabel(janela_criar_usuario, text="Criar Novo Usuário", font=("Arial", 24, "bold"))
        header.grid(row=0, column=0, pady=20, padx=10)

        # Frame central para alinhar os elementos
        frame_central = ctk.CTkFrame(janela_criar_usuario)
        frame_central.grid(row=1, column=0, pady=20, padx=10, sticky="n")

        # Label Nome de Usuário
        label_usuario = ctk.CTkLabel(frame_central, text="Nome de Usuário", font=("Arial", 16))
        label_usuario.grid(row=0, column=0, pady=5)

        # Campo de Nome de Usuário
        campo_usuario = ctk.CTkEntry(frame_central, placeholder_text="Digite o nome do usuário", width=300)
        campo_usuario.grid(row=1, column=0, padx=8)
        

        # Label Senha
        label_senha = ctk.CTkLabel(frame_central, text="Senha", font=("Arial", 16))
        label_senha.grid(row=2, column=0, pady=5)

        # Campo de Senha
        campo_senha = ctk.CTkEntry(frame_central, placeholder_text="Digite a senha", show="*", width=300)
        campo_senha.grid(row=3, column=0, padx=8)

        def criar_usuario():
            nome = campo_usuario.get()
            senha = campo_senha.get()
            salvar_alteracoes(usuarios, usuarios_path)
            log = cadastro_usuario(usuarios, nome, senha)
            label_msg_criar_usuario.configure(text=f"Usuário {nome} criado com sucesso!", text_color='green')
            registrar_log(log)
            janela_criar_usuario.after(700, janela_criar_usuario.destroy)

        # botão criar usuário
        botao_criar_usuario = ctk.CTkButton(frame_central, text="Criar Usuário", command=criar_usuario)
        botao_criar_usuario.grid(row=4, column=0, pady=15)

        label_msg_criar_usuario = ctk.CTkLabel(frame_central, text="")
        label_msg_criar_usuario.grid(row=5, column=0)
 
    ctk.set_appearance_mode("Dark")  # Pode ser "Dark" ou "Light"
    ctk.set_default_color_theme("blue")
    # Criar a janela principal
    janela = ctk.CTk()
    janela.title("Sistema de Almoxarifado - Login")

    # Configurar o layout da janela
    janela.grid_columnconfigure(0, weight=1)
    janela.grid_rowconfigure(1, weight=1)
    janela.grid_rowconfigure(2, weight=1)

    # Header
    header = ctk.CTkLabel(janela, text="Bem-vindo ao Sistema de Almoxarifado", font=("Arial", 24, "bold"))
    header.grid(row=0, column=0, pady=110, padx=10)

    # Frame central para alinhar os elementos
    frame_central = ctk.CTkFrame(janela)
    frame_central.grid(row=1, column=0, padx=40, pady=30, sticky="n")

    # Label Login
    label_login = ctk.CTkLabel(frame_central, text="Login", font=("Arial", 16))
    label_login.grid(row=0, column=0, pady=10)

    # Campo de usuário
    campo_usuario = ctk.CTkEntry(frame_central, placeholder_text="Usuário", width=300)
    campo_usuario.grid(row=1, column=0, pady=5, padx=5)

    # Campo de senha
    campo_senha = ctk.CTkEntry(frame_central, placeholder_text="Senha", show="*", width=300)
    campo_senha.grid(row=2, column=0, pady=5, padx=5)

    # Botão de login
    botao_login = ctk.CTkButton(frame_central, text="Login", command=logar)
    botao_login.grid(row=3, column=0, pady=5)

    # Botão de criar usuário
    botao_tela_criar_usuario= ctk.CTkButton(frame_central, text="Criar Usuário", fg_color="gray", command=abrir_tela_criar_usuario)
    botao_tela_criar_usuario.grid(row=4, column=0, pady=5)

    # Mensagem
    label_msg_login = ctk.CTkLabel(frame_central, text="")
    label_msg_login.grid(row=5, column=0)

    # Rodar a janela
    janela.mainloop()
    
if __name__ == "__main__":
    main()
