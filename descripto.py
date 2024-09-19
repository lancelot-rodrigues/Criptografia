import os

# Definir o caminho do diretório onde os dados descriptografados serão restaurados
pasta_descriptografada = "dados_descriptografados"

# Verifica se o diretório já existe, caso contrário, cria o diretório
if not os.path.exists(pasta_descriptografada):
    os.makedirs(pasta_descriptografada)
    print(f"Diretório '{pasta_descriptografada}' criado com sucesso para armazenar dados descriptografados!")
else:
    print(f"O diretório '{pasta_descriptografada}' já existe.")


