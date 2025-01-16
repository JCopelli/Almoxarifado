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
    #      #Requer Autenticação
     #     print("-> (3) Cadastrar Usuario\n")
    #      print("-> (2) Alterar senha")
   
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
        
        global usuario_atual
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
                janela.iconify()
                abrir_menu_principal()

                 # elif opcao == 5:
        #     item_entrada = input ("Digite o item que deseja incrementar: ")
        #     if item_entrada in almoxarifado1.estoque:
        #         log = almoxarifado1.estoque[item_entrada].entrada_de_estoque(usuario_atual)
        #         registrar_log(log)
        #         salvar_alteracoes(almoxarifado1, almoxarifado_path)
        #         continuar_acao()
        #     else:
        #         print("\nEsse item não existe no estoque!")
        #         continuar_acao()


    def abrir_janela_entrada():
        janela_entrada= ctk.CTkToplevel(janela)
        janela_entrada.title("Sistema de Almoxarifado - Entrada no Estoque")
        janela_entrada.geometry("400x400")
        janela_entrada.resizable(width=False, height=False)
        janela_entrada.after(50,janela_entrada.deiconify)
        janela_entrada.focus_force()

        # Configurar o layout da janela
        janela_entrada.grid_columnconfigure(0, weight=1)
        janela_entrada.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkLabel(janela_entrada, text="Entrada no Estoque", font=("Arial", 24, "bold"))
        header.grid(row=0, column=0, pady=20, padx=10)

        # Frame central para alinhar os elementos
        frame_central = ctk.CTkFrame(janela_entrada)
        frame_central.grid(row=1, column=0, pady=20, padx=10, sticky="n")

        # Label Nome do item
        label_nome = ctk.CTkLabel(frame_central, text="Nome do Item", font=("Arial", 16))
        label_nome.grid(row=0, column=0, pady=5)

        # Campo de Nome do item
        campo_nome = ctk.CTkEntry(frame_central, placeholder_text="Digite o nome do item a dar entrada", width=300)
        campo_nome.grid(row=1, column=0, padx=8)
        

        # Label quantidade
        label_quantidade = ctk.CTkLabel(frame_central, text="Quantidade", font=("Arial", 16))
        label_quantidade.grid(row=2, column=0, pady=5)

        # Campo quantidade
        campo_quantidade = ctk.CTkEntry(frame_central, placeholder_text="Digite a quantidade a ser incrementada", width=300)
        campo_quantidade.grid(row=3, column=0, padx=8)

        def entrada():
            global usuario_atual
            nome = campo_nome.get()
            quantidade = campo_quantidade.get()
            if nome in almoxarifado1.estoque:
                log = almoxarifado1.estoque[nome].entrada_de_estoque(usuario_atual, quantidade)
                registrar_log(log)
                salvar_alteracoes(almoxarifado1, almoxarifado_path)
                label_msg_entrada.configure(text=f"Item {nome} incrementado em {quantidade}", text_color='green')
                janela_entrada.after(700, janela_entrada.destroy)
            else:
                label_msg_entrada.configure(text=f"Item {nome} não existe!", text_color="red")

        # botão criar usuário
        botao_entrada = ctk.CTkButton(frame_central, text="Incrementar Estoque", command=entrada)
        botao_entrada.grid(row=4, column=0, pady=15)

        label_msg_entrada = ctk.CTkLabel(frame_central, text="")
        label_msg_entrada.grid(row=5, column=0)



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
    
    def abrir_janela_saida():
        janela_saida= ctk.CTkToplevel(janela)
        janela_saida.title("Sistema de Almoxarifado - Entrada no Estoque")
        janela_saida.geometry("400x400")
        janela_saida.resizable(width=False, height=False)
        janela_saida.after(50,janela_saida.deiconify)
        janela_saida.focus_force()

        # Configurar o layout da janela
        janela_saida.grid_columnconfigure(0, weight=1)
        janela_saida.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkLabel(janela_saida, text="Entrada no Estoque", font=("Arial", 24, "bold"))
        header.grid(row=0, column=0, pady=20, padx=10)

        # Frame central para alinhar os elementos
        frame_central = ctk.CTkFrame(janela_saida)
        frame_central.grid(row=1, column=0, pady=20, padx=10, sticky="n")

        # Label Nome do item
        label_nome = ctk.CTkLabel(frame_central, text="Nome do Item", font=("Arial", 16))
        label_nome.grid(row=0, column=0, pady=5)

        # Campo de Nome do item
        campo_nome = ctk.CTkEntry(frame_central, placeholder_text="Digite o nome do item a dar saída", width=300)
        campo_nome.grid(row=1, column=0, padx=8)
        

        # Label quantidade
        label_quantidade = ctk.CTkLabel(frame_central, text="Quantidade", font=("Arial", 16))
        label_quantidade.grid(row=2, column=0, pady=5)

        # Campo quantidade
        campo_quantidade = ctk.CTkEntry(frame_central, placeholder_text="Digite a quantidade a ser retirada", width=300)
        campo_quantidade.grid(row=3, column=0, padx=8)

        def saida():
            global usuario_atual
            nome = campo_nome.get()
            quantidade = campo_quantidade.get()
            if nome in almoxarifado1.estoque:
                log = almoxarifado1.estoque[nome].saida_de_estoque(usuario_atual, quantidade)
                if log == False:
                    label_msg_entrada.configure(text='Quantidade indisponível', text_color="red",)
                else:
                    registrar_log(log)
                    salvar_alteracoes(almoxarifado1, almoxarifado_path)
                    label_msg_entrada.configure(text=f"Item {nome} retirado em {quantidade}", text_color='green')
                    janela_saida.after(700, janela_saida.destroy)
            else:
                label_msg_entrada.configure(text=f"Item {nome} não existe no estoque!", text_color="red")

        # botão criar usuário
        botao_entrada = ctk.CTkButton(frame_central, text="Retirar do Estoque", command=saida)
        botao_entrada.grid(row=4, column=0, pady=15)

        label_msg_entrada = ctk.CTkLabel(frame_central, text="")
        label_msg_entrada.grid(row=5, column=0)

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

        label_msg_criar_usuario = ctk.CTkLabel(frame_central, text="", font=("bold"))
        label_msg_criar_usuario.grid(row=5, column=0)
  
    def abrir_tela_alterar_senha():

        global usuario_atual
        # Criando a janela principal
        janela_alterar_senha = ctk.CTkToplevel(janela)
        janela_alterar_senha.title("Tela de Alterar Senha")
        janela_alterar_senha.geometry("400x400")
        janela_alterar_senha.resizable(width=False, height=False)
        janela_alterar_senha.after(50, janela_alterar_senha.deiconify)
        janela_alterar_senha.focus_force()

        # Configurar o layout da janela
        janela_alterar_senha.grid_columnconfigure(0, weight=1)
        janela_alterar_senha.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkLabel(janela_alterar_senha, text="Alterar a Senha", font=("Arial", 24, "bold"))
        header.grid(row=0, column=0, pady=20, padx=10)

        # Frame central para alinhar os elementos
        frame_central = ctk.CTkFrame(janela_alterar_senha)
        frame_central.grid(row=1, column=0, pady=20, padx=10, sticky="n")

        # Label Senha
        label_senha = ctk.CTkLabel(frame_central, text="Senha", font=("Arial", 16))
        label_senha.grid(row=0, column=0, pady=5)

        # Campo de Senha
        campo_senha = ctk.CTkEntry(frame_central, placeholder_text="Digite a senha atual", width=300)
        campo_senha.grid(row=1, column=0, padx=8)
        

        # Label Senha nova
        label_senha_nova = ctk.CTkLabel(frame_central, text="Senha nova", font=("Arial", 16))
        label_senha_nova.grid(row=2, column=0, pady=5)

        # Campo de Senha nova
        campo_senha_nova = ctk.CTkEntry(frame_central, placeholder_text="Digite a senha nova", width=300)
        campo_senha_nova.grid(row=3, column=0, padx=8)

        # Label Senha nova confirma
        label_senha_nova_confirma = ctk.CTkLabel(frame_central, text="Senha nova", font=("Arial", 16))
        label_senha_nova_confirma.grid(row=4, column=0, pady=5)

        # Campo de Senha nova senha nova confirma
        campo_senha_nova_confirma = ctk.CTkEntry(frame_central, placeholder_text="Confirme a senha nova", width=300)
        campo_senha_nova_confirma.grid(row=5, column=0, padx=8)


        # # Mensagem no final da página
        # label_alterar_senha = ctk.CTkLabel(frame_central, text="")
        # label_alterar_senha.grid(row=7, column=0)

        label_msg_mod_senha = ctk.CTkLabel(frame_central, text="")
        label_msg_mod_senha.grid(row=7, column=0)

        # Mensagem
        label_msg_login = ctk.CTkLabel(frame_central, text="")
        label_msg_login.grid(row=5, column=0)


        def alterar_senha_main():
            # print("Aqui")
            senha = campo_senha.get()
            senha_nova = campo_senha_nova.get()
            senha_nova_confirma = campo_senha_nova_confirma.get()

            if senha_nova != senha_nova_confirma:
                label_msg_mod_senha.configure(text="As senhas não são iguais! Tente novamente.", text_color="red")
            else:
                if senha == usuario_atual.senha:
                    # print("2")
                    log = usuario_atual.alterar_senha(senha_nova)
                    registrar_log(log)
                    salvar_alteracoes(usuarios, usuarios_path)
                    label_msg_mod_senha.configure(text="Senha alterada com sucesso!", text_color="green")
                    label_msg_mod_senha.after(700, janela_alterar_senha.destroy)
                else:
                    # print(usuario_atual.senha)
                    label_msg_mod_senha.configure(text="Senha Incorreta", text_color="red")


        # botão alterar senha
        botao_alterar_senha = ctk.CTkButton(frame_central, text="Alterar Senha", command=alterar_senha_main)
        botao_alterar_senha.grid(row=6, column=0, pady=15)


        # # Configurar o layout da janela
        # app2.grid_columnconfigure(0, weight=1)
        # app2.grid_rowconfigure(1, weight=1)
        # app2a.grid_rowconfigure(2, weight=1)

        # # Header
        # header = ctk.CTkLabel(app2, text="Bem-vindo ao Sistema de Almoxarifado", font=("Arial", 24, "bold"))
        # header.grid(row=0, column=0, pady=110, padx=10)

        # # Frame central para alinhar os elementos
        # frame_central = ctk.CTkFrame(janela)
        # frame_central.grid(row=1, column=0, padx=40, pady=30, sticky="n")



        # # Criando frame para centralizar os widgets
        # frame_central = ctk.CTkFrame(app2)
        # frame_central.grid(row=0, column=0, sticky="nsew")



        # # Configurando a grid
        # frame_central.grid_rowconfigure(0, weight=1)
        # frame_central.grid_rowconfigure(1, weight=1)
        # frame_central.grid_rowconfigure(2, weight=1)
        # frame_central.grid_rowconfigure(3, weight=1)
        # frame_central.grid_rowconfigure(4, weight=1)
        # frame_central.grid_columnconfigure(0, weight=1)

        # # Criando widgets
        # label_senha = ctk.CTkLabel(frame_central, text="Senha Atual:")
        # label_senha.grid(row=0, column=1, pady=5)

        # entry_senha = ctk.CTkEntry(frame_central, show="*")  # `show="*"` oculta a senha digitada
        # entry_senha.grid(row=1, column=1, pady=5)

        # label_senha_nova = ctk.CTkLabel(frame_central, text="Nova Senha:")
        # label_senha_nova.grid(row=2, column=1, pady=5)



        # entry_senha_nova = ctk.CTkEntry(frame_central, show="*")  # `show="*"` oculta a senha digitada
        # entry_senha_nova.grid(row=3, column=1, pady=5)

        # label_senha_nova_confirma = ctk.CTkLabel(frame_central, text="Confirmar Nova Senha:")
        # label_senha_nova_confirma.grid(row=4, column=1, pady=5)

        # entry_senha_nova_confirma = ctk.CTkEntry(frame_central, show="*")  # `show="*"` oculta a senha digitada
        # entry_senha_nova_confirma.grid(row=5, column=1, pady=5)

        # label_msg_mod_senha = ctk.CTkLabel(frame_central, text="")
        # label_msg_mod_senha.grid(row=6, column=1, pady=10, padx=10)

        # def alterar_senha_main():
        #     print("Aqui")
        #     senha = entry_senha.get()
        #     senha_nova = entry_senha_nova.get()
        #     senha_nova_confirma = entry_senha_nova_confirma.get()

        #     if senha_nova != senha_nova_confirma:
        #         label_msg_mod_senha.configure(text="Confirmação inválida, tente novamente!", text_color="red")
        #     else:
        #         if senha == usuario_atual.senha:
        #             print("2")
        #             log = usuario_atual.alterar_senha(senha_nova)
        #             registrar_log(log)
        #             salvar_alteracoes(usuarios, usuarios_path)
        #             label_msg_mod_senha.configure(text="Senha alterada com sucesso!", text_color="green")
        #             label_msg_mod_senha.after(700, app2.destroy)
        #         else:
        #             print(usuario_atual.senha)
        #             label_msg_mod_senha.configure(text="Senha Incorreta", text_color="red")

        # # Botão de alterar senha
        # btn_login = ctk.CTkButton(frame_central, text="Alterar senha", command=alterar_senha_main)
        # btn_login.grid(row=7, column=1, pady=20)

    def abrir_menu_principal():
    # Criar nova janela para o menu principal
        janela_menu = ctk.CTkToplevel()
        janela_menu.title("Menu Principal")
        janela_menu.geometry("500x500")
        janela_menu.state("zoomed")

        # Configurar o layout da janela
        janela_menu.grid_columnconfigure(0, weight=1)

        # Header
        header = ctk.CTkLabel(janela_menu, text="Menu Principal", font=("Arial", 24, "bold"))
        header.grid(row=0, column=0, pady=130)

        # Frame central para alinhar os botões
        frame_menu = ctk.CTkFrame(janela_menu)
        frame_menu.grid(row=1, column=0, pady=30, padx=20)

        # Botões de opções do menu
        botoes_menu = [
            ("Consultar Estoque", lambda: print("Consultar Estoque selecionado")),
            ("Entrada no Estoque", abrir_janela_entrada),
            ("Saída do Estoque", abrir_janela_saida),
            ("Cadastrar Item", lambda: print("Cadastrar Item selecionado")),
            ("Remover Item", lambda: print("Remover Item selecionado")),
            ("Mudar senha", abrir_tela_alterar_senha),
            ("Logout", lambda: print("Logout selecionado"))           
        ]

        for i, (texto, comando) in enumerate(botoes_menu):
            botao = ctk.CTkButton(
                frame_menu,
                text=texto,
                command=comando,
                font=("Arial", 16, "bold"),
                width=250,
                height=40
            )
            botao.grid(row=i, column=0, pady=5, padx=10)


    ctk.set_appearance_mode("Dark")  # Pode ser "Dark" ou "Light"
    ctk.set_default_color_theme("blue")
    # Criar a janela principal
    janela = ctk.CTk()
    janela.title("Sistema de Almoxarifado - Login")
    janela.state("zoomed")

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
