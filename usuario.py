class Usuario:
    def __init__(self, nome, senha, autenticado=False):
        self.__nome = nome
        self.__senha = senha
        self.__autenticado = autenticado
    
    def login(self):
        senha = input("Digite sua senha: ")
        if senha == self.__senha:
            self.__autenticado = True
            print(f"O usuário {self.__nome} foi logado")
            return self.__autenticado
        else:
            print("Senha incorreta. Digite uma senha válida!")
            return self.__autenticado
    
    def modificar_senha(self):
        senha_atual = input("Para definir uma nova senha, digite sua senha atual: ")
        if senha_atual == self.__senha:
            nova_senha = input("Digite a nova senha: ")
            confirma_senha = input("Confirme a nova senha: ")
            if nova_senha != confirma_senha:
                while(nova_senha != confirma_senha):
                    print("As senhas digitadas não são iguais, tente novamente.")
                    nova_senha = input("Digite a nova senha: ")
                    confirma_senha = input("Confirme a nova senha: ")
                self.__senha = nova_senha
                print("Senha alterada com sucesso!")
            else:
                self.__senha = nova_senha
                print("Senha alterada com sucesso!")
        else:
            print("A senha está incorreta!") 
