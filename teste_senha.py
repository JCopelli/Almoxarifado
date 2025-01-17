from Usuario import Usuario
import pwinput
import pickle

usuarios_path = "C:/Users/TEMP.CCE.015/Documents/usuarios.pkl"

def salvar_dados(dado, caminho):
    try:
        with open(caminho,"wb") as arquivo: 
            pickle.dump(dado, arquivo)
            print("Atualizações Salvas")

    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")

def ler_dados(caminho):
    # try:
    with open(caminho, "rb") as arquivo:
        dado = pickle.load(arquivo)
        print("Lendo Arquivos\n")
        return dado
        
    # except Exception as e:
    #     print(f"Erro ao ler o estoque: {e}")



def cadastro_usuario(usuarios):
    nome = input("Digite o nome do novo usuario: ")
    senha = pwinput.pwinput(prompt = "Digite a senha do novo usuario: ", mask = "*")
    usuarios.append(Usuario(nome, senha))


# usuarios = ler_dados(usuarios_path)

# salvar_dados(usuarios, usuarios_path)
try:
    usuarios = ler_dados(usuarios_path)


except:

    usuarios = []
    salvar_dados(usuarios, usuarios_path)

cadastro_usuario(usuarios)

salvar_dados(usuarios, usuarios_path)

for user in usuarios:
    user.mostrar_informacoes()