import pwinput 

class Usuario:
    def __init__(self, nome, senha): # autenticado=False
        self.__nome = nome
        self.__senha = senha
        self.__autenticado = False
    
    def login(self):
            senha = pwinput.pwinput(prompt = "Senha: ", mask = "*")
            if senha == self.__senha:
                self.__autenticado = True
                print(f"Usuário {self.__nome} autenticado")
            else:
                print("Senha incorreta.Tente Novamente!")
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
                print("Senha alterada com sucesso!")
            else:
                self.__senha = nova_senha
                print("Senha alterada com sucesso!")
        else:
            print("A senha está incorreta!")

    @property
    def autenticado(self):
        return self.__autenticado

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha

    def mostrar_informacoes(self):
        print(self.__nome)
        print(self.__senha)
        print(self.__autenticado)
