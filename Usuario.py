class Usuario:
    def __init__(self, nome, senha):
        try:
            self.__nome = nome
            self.__senha = senha
            self.__autenticado = False
        except Exception as e:
            raise ValueError(f"Erro ao criar usuário: {e}")

    def login(self, senha):
        try:
            if senha == self.__senha:
                self.__autenticado = True
                return f"Usuário {self.__nome} autenticado com sucesso."
            else:
                return "Senha incorreta."
        except Exception as e:
            return f"Erro durante o login: {e}"
        finally:
            print(f"Tentativa de login finalizada para o usuário: {self.__nome}")

    def alterar_senha(self, nova_senha):
        try:
            if not nova_senha:
                raise ValueError("A nova senha não pode estar vazia.")
            self.__senha = nova_senha
            log = f"O usuário {self.__nome} alterou sua senha."
            return log
        except ValueError as e:
            return f"Erro ao alterar senha: {e}"
        except Exception as e:
            return f"Erro inesperado ao alterar senha: {e}"
        finally:
            print(f"Operação de alteração de senha finalizada para o usuário: {self.__nome}")

    def logout(self):
        try:
            if not self.__autenticado:
                return f"Usuário {self.__nome} já está desconectado."
            self.__autenticado = False
            log = f"O usuário {self.__nome} foi desconectado."
            return log
        except Exception as e:
            return f"Erro ao desconectar usuário: {e}"
        finally:
            print(f"Operação de logout finalizada para o usuário: {self.__nome}")

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
        try:
            print(f"Nome: {self.__nome}")
            print(f"Senha: {self.__senha}")
            print(f"Autenticado: {self.__autenticado}")
        except Exception as e:
            print(f"Erro ao mostrar informações do usuário: {e}")