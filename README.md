# Python RSA Crypt

Este é um projeto simples de criptografia e descriptografia utilizando o algoritmo RSA. Ele permite gerar chaves públicas e privadas, criptografar mensagens e descriptografá-las.

## Estrutura do Projeto

```
python-rsa-crypt/
├── data/
│   ├── input.txt          # Arquivo de entrada para criptografia
│   ├── output.crypt       # Arquivo de saída com o conteúdo criptografado
├── security/
│   ├── private.csa        # Chave privada gerada
│   ├── public.cpa         # Chave pública gerada
├── src/
│   ├── decrypt.py         # Script para descriptografar mensagens
│   ├── encrypt.py         # Script para criptografar mensagens
│   ├── key_generator.py   # Script para gerar chaves RSA
│   ├── main.py            # Interface principal do programa
│   ├── prime_generator.py # Gerador de números primos
├── .gitignore             # Arquivo para ignorar arquivos desnecessários no Git
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

## Funcionalidades

1. **Gerar Chaves**: Gera um par de chaves RSA (pública e privada) e as salva na pasta `security/`.
2. **Criptografar**: Lê o conteúdo do arquivo `data/input.txt`, criptografa utilizando a chave pública e salva o resultado em `data/output.crypt`.
3. **Descriptografar**: Lê o conteúdo do arquivo `data/output.crypt`, descriptografa utilizando a chave privada e exibe o conteúdo original.

## Como Usar

### Pré-requisitos

- Python 3.7 ou superior
- Instale as dependências do projeto com o comando:
    ```bash
    pip install -r requirements.txt
    ```

### Executando o Programa

1. Navegue até a pasta `src/`:
     ```bash
     cd src
     ```

2. Execute o arquivo `main.py`:
     ```bash
     python main.py
     ```

3. Siga as instruções no menu interativo para gerar chaves, criptografar ou descriptografar mensagens.

### Exemplo de Uso

- **Gerar Chaves**: Escolha a opção `1` no menu.
- **Criptografar**: Insira o texto no arquivo `data/input.txt` e escolha a opção `2` no menu.
- **Descriptografar**: Escolha a opção `3` no menu para visualizar o texto original.

## Detalhes Técnicos

- **Algoritmo RSA**: Utiliza números primos gerados pelo script `prime_generator.py` para calcular as chaves pública e privada.
- **Criptografia**: Implementada no script `encrypt.py` utilizando a chave pública.
- **Descriptografia**: Implementada no script `decrypt.py` utilizando a chave privada.
