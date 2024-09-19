# Secure-File-Encryptor

---

Este projeto contém scripts Python para criptografar e descriptografar arquivos usando o algoritmo AES no modo CBC. Além disso, inclui funcionalidades para criar diretórios e arquivos de exemplo.

## Funcionalidades

- **Criptografar Arquivos**: Criptografa arquivos de uma pasta de origem e salva os arquivos criptografados em uma pasta de destino.
- **Descriptografar Arquivos**: Descriptografa arquivos criptografados e salva os arquivos descriptografados em uma pasta de destino.
- **Criar Diretórios e Arquivos de Exemplo**: Scripts para criar diretórios e arquivos de exemplo para teste.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `pycryptodome`: Para criptografia AES.
  
  Você pode instalar a biblioteca necessária usando o seguinte comando:
  ```bash
  pip install pycryptodome
  ```

## Uso

1. **Criação de Diretórios e Arquivos de Exemplo**

   Execute o script `criar_diretorios_e_arquivos.py` para criar um diretório e arquivos de exemplo:

   ```bash
   python criar_diretorios_e_arquivos.py
   ```

2. **Criptografar Arquivos**

   Execute o script `criptografar_arquivos.py` para criptografar arquivos em um diretório de origem:

   ```bash
   python criptografar_arquivos.py
   ```

   O script solicitará a chave de criptografia (16 bytes) e a operação desejada.

3. **Descriptografar Arquivos**

   Execute o script `descriptografar_arquivos.py` para descriptografar arquivos criptografados:

   ```bash
   python descriptografar_arquivos.py
   ```

   O script solicitará a chave de criptografia (16 bytes) e a operação desejada.

## Scripts

### `criar_diretorios_e_arquivos.py`

Cria um diretório e arquivos de exemplo. Utilizado para preparar o ambiente para criptografia e descriptografia.

### `criptografar_arquivos.py`

Script para criptografar arquivos em um diretório de origem e salvar os arquivos criptografados em um diretório de destino.

### `descriptografar_arquivos.py`

Script para descriptografar arquivos criptografados e salvar os arquivos descriptografados em um diretório de destino.

## Exemplo de Uso

1. Crie diretórios e arquivos de exemplo:
   ```bash
   python criar_diretorios_e_arquivos.py
   ```

2. Criptografe os arquivos:
   ```bash
   python criptografar_arquivos.py
   ```

3. Descriptografe os arquivos:
   ```bash
   python descriptografar_arquivos.py
   ```

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

Você pode ajustar as informações de acordo com os detalhes específicos do seu projeto e adicionar qualquer outra seção que considerar relevante.
