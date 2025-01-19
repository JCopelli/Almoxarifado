from Usuario import Usuario
import pwinput
import pickle

usuarios_path = "C:/Users/TEMP.CCE.015/Documents/usuarios.pkl"

def salvar_dados(dado, caminho):
    try:
        with open(caminho, "wb") as arquivo:
            pickle.dump(dado, arquivo)
            print("Atualizações salvas com sucesso.")
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")

def ler_dados(caminho):
    try:
        with open(caminho, "rb") as arquivo:
            dado = pickle.load(arquivo)
            print("Dados carregados com sucesso.")
            return dado
    except FileNotFoundError:
        print("Arquivo não encontrado. Um novo será criado.")
        return []
    except Exception as e:
        print(f"Erro ao ler os dados: {e}")
        return []

def cadastro_usuario(usuarios):
    try:
        nome = input("Digite o nome do novo usuário: ")
        if not nome.strip():
            raise ValueError("O nome do usuário não pode estar vazio.")
        senha = pwinput.pwinput(prompt="Digite a senha do novo usuário: ", mask="*")
        if not senha.strip():
            raise ValueError("A senha não pode estar vazia.")
        usuarios.append(Usuario(nome, senha))
        print(f"Usuário {nome} cadastrado com sucesso.")
    except ValueError as e:
        print(f"Erro no cadastro do usuário: {e}")
    except Exception as e:
        print(f"Erro inesperado no cadastro do usuário: {e}")

def main():
    try:
        usuarios = ler_dados(usuarios_path)
    except Exception as e:
        print(f"Erro ao carregar os usuários: {e}")
        usuarios = []
        salvar_dados(usuarios, usuarios_path)

    cadastro_usuario(usuarios)

    salvar_dados(usuarios, usuarios_path)

    for user in usuarios:
        try:
            user.mostrar_informacoes()
        except Exception as e:
            print(f"Erro ao mostrar informações do usuário: {e}")

if __name__ == "__main__":
    main()