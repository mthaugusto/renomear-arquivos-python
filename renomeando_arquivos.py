import os

# Diretório contendo as imagens
diretorio = "caminho/"


# Lista todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Iniciando contador
contador = 1

# Itera sobre cada arquivo na pasta
for arquivo in arquivos:

    # Verifica se o arquivo é uma imagem (extensão .jpg, .jpeg, .png, etc.)
    if arquivo.endswith(".jpg") or arquivo.endswith(".jpeg") or arquivo.endswith(".png"):

        # Constrói o novo nome do arquivo
        novo_nome = f"novo_nome{contador}.jpg"

        # Renomeia o arquivo
        # A função os.rename recebe dois parametros, o caminho antigo e o novo
        # Exemplo: os.rename("diretorio/antigo.txt", "diretorio/novo.txt")
        # Já a função os.path.join - recebe o caminho do diretorio e os arquivos que serão colocados nele
        # Exemplo:
        # Concatena os diretórios 'diretorio' e 'subdiretorio' com o nome do arquivo 'arquivo.txt'
        # caminho_completo = os.path.join('diretorio', 'subdiretorio', 'arquivo.txt')
        os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio, novo_nome))

        # Incrementa o contador
        contador += 1

print("Renomeação concluída.")
