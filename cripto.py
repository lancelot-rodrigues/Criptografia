import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def criptografar_arquivo(caminho_arquivo, chave, pasta_destino):
    # Lê o conteúdo do arquivo original
    with open(caminho_arquivo, 'rb') as arquivo:
        conteudo = arquivo.read()
    
    # Gera um IV de 16 bytes
    iv = get_random_bytes(16)
    
    # Cria o objeto AES em modo CBC
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    
    # Adiciona padding ao conteúdo para garantir que tenha múltiplo de 16 bytes
    conteudo_criptografado = cipher.encrypt(pad(conteudo, AES.block_size))
    
    # Gera o caminho do arquivo criptografado
    nome_arquivo = os.path.basename(caminho_arquivo)
    caminho_criptografado = os.path.join(pasta_destino, nome_arquivo + ".enc")
    
    # Escreve o IV e o conteúdo criptografado no novo arquivo
    with open(caminho_criptografado, 'wb') as arquivo_cripto:
        arquivo_cripto.write(iv + conteudo_criptografado)
    
    print(f"Arquivo '{nome_arquivo}' criptografado com sucesso!")


def descriptografar_arquivo(caminho_arquivo_criptografado, chave, pasta_destino):
    # Lê o conteúdo do arquivo criptografado
    with open(caminho_arquivo_criptografado, 'rb') as arquivo:
        conteudo = arquivo.read()
    
    # Extrai o IV dos primeiros 16 bytes
    iv = conteudo[:16]
    
    # O conteúdo criptografado vem após o IV
    conteudo_criptografado = conteudo[16:]
    
    # Cria o objeto AES em modo CBC
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    
    # Descriptografa e remove o padding
    conteudo_original = unpad(cipher.decrypt(conteudo_criptografado), AES.block_size)
    
    # Gera o caminho do arquivo descriptografado
    nome_arquivo = os.path.basename(caminho_arquivo_criptografado).replace(".enc", "")
    caminho_descriptografado = os.path.join(pasta_destino, nome_arquivo)
    
    # Escreve o conteúdo original no novo arquivo
    with open(caminho_descriptografado, 'wb') as arquivo_original:
        arquivo_original.write(conteudo_original)
    
    print(f"Arquivo '{nome_arquivo}' descriptografado com sucesso!")


def processar_pasta(pasta_origem, pasta_destino, chave, modo='criptografar'):
    # Cria a pasta de destino, se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Itera por todos os arquivos na pasta de origem
    for nome_arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
        
        # Se o caminho for um arquivo (não uma pasta), processa-o
        if os.path.isfile(caminho_arquivo):
            if modo == 'criptografar':
                criptografar_arquivo(caminho_arquivo, chave, pasta_destino)
            elif modo == 'descriptografar':
                descriptografar_arquivo(caminho_arquivo, chave, pasta_destino)


# Exemplo de uso
if __name__ == "__main__":
    # Solicita ao usuário a chave AES de 16 bytes
    chave = input("Digite uma chave de 16 bytes para criptografia: ").encode('utf-8')

    if len(chave) != 16:
        print("A chave deve ter exatamente 16 bytes!")
        exit()
    
    # Define os diretórios de origem e destino
    pasta_origem = 'meu_diretorio_com_arquivos'
    pasta_criptografada = 'dados_criptografados'
    pasta_descriptografada = 'dados_descriptografados'

    # Escolha: Criptografar ou Descriptografar
    opcao = input("Deseja 'criptografar' ou 'descriptografar' os arquivos? ")

    if opcao == 'criptografar':
        processar_pasta(pasta_origem, pasta_criptografada, chave, modo='criptografar')
    elif opcao == 'descriptografar':
        processar_pasta(pasta_criptografada, pasta_descriptografada, chave, modo='descriptografar')
    else:
        print("Opção inválida!")
