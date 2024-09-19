import os

# Definir o caminho do diretório onde os dados criptografados serão armazenados
pasta_criptografada = "dados_criptografados"

# Verifica se o diretório já existe, caso contrário, cria o diretório
if not os.path.exists(pasta_criptografada):
    os.makedirs(pasta_criptografada)
    print(f"Diretório '{pasta_criptografada}' criado com sucesso para armazenar dados criptografados!")
else:
    print(f"O diretório '{pasta_criptografada}' já existe.")

# Você pode agora salvar seus arquivos criptografados neste diretório
