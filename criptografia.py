import os

# Caminho do diretório que você quer criar
caminho_diretorio = "meu_diretorio_com_arquivos"

# Verifica se o diretório já existe, caso contrário cria o diretório
if not os.path.exists(caminho_diretorio):
    os.makedirs(caminho_diretorio)
    print(f"Diretório '{caminho_diretorio}' criado com sucesso!")
else:
    print(f"O diretório '{caminho_diretorio}' já existe.")

# Cria alguns arquivos dentro do diretório recém-criado
arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]
conteudo_arquivos = ["qyalquer coisa", "Aleatorio", "oi tudo bem"]

for i, nome_arquivo in enumerate(arquivos):
    caminho_arquivo = os.path.join(caminho_diretorio, nome_arquivo)
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo_arquivos[i])
        print(f"Arquivo '{nome_arquivo}' criado com sucesso no diretório '{caminho_diretorio}'!")
