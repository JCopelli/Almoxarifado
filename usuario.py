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
                print(f"Usuário {self.__nome} conectado com sucesso!")
            else:
                print("Senha incorreta.Tente Novamente!")
                return self.__autenticado
        
        #Função para mudar senha. 
    def alterar_senha(self, usuario):
        if usuario == None: 
            print("você não está conectado!")
            log = f"Usuario não autenticado tentou modificar senha."
            return log
        else:
            senha_atual = input("Para definir uma nova senha, digite sua senha atual: ")
            if senha_atual == self.__senha:
                nova_senha = input("Digite a nova senha: ")
                confirma_senha = input("Confirme a nova senha: ")  #Testa se a senha está correta
                if nova_senha != confirma_senha:
                    while(nova_senha != confirma_senha):    #Repete a condição até que as senhas sejam iguais
                        print("As senhas digitadas não são iguais, tente novamente.")
                        nova_senha = input("Digite a nova senha: ")
                        confirma_senha = input("Confirme a nova senha: ")
                    self.__senha = nova_senha
                    print("Senha alterada com sucesso!")
                    log = f"O usuario {usuario.nome} alterou sua senha."
                    return log
                else:
                    self.__senha = nova_senha
                    print("Senha alterada com sucesso!")
                    log = f"O usuario {usuario.nome} alterou sua senha."
                    return log
            else:
                print("A senha está incorreta!")

        #Desconecta o usuário
    def logout(self, usuario):
        if usuario == None:
            print("você não está conectado!")
            log = f"Usuario não autenticado tentou se desconectar."
            return log
        else:
            self.__autenticado = False
            print(f"o usuário {usuario.nome} foi desconectado")
            log = f"O usuário {usuario.nome} foi desconectado."
            return log
            

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

    def mostrar_informacoes(self):
        print(self.__nome)
        print(self.__senha)
        print(self.__autenticado)
