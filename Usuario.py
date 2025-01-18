class Usuario:
    def __init__(self, nome, senha): # autenticado=False
        self.__nome = nome
        self.__senha = senha
        self.__autenticado = False
    
    def login(self, senha):
            if senha == self.__senha:
                self.__autenticado = True
            else:
                return False
        
        #Função para mudar senha. 
    def alterar_senha(self, nova_senha):
                self.__senha = nova_senha
                log = f"O usuario {self.__nome} alterou sua senha."
                return log

        #Desconecta o usuário
    def logout(self):
        self.__autenticado = False
        log = f"O usuário {self.__nome} foi desconectado."
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
