import os

def read_public_key(public_key_path):
    """Lê a chave pública do arquivo."""
    with open(public_key_path, "r") as file:
        content = file.read().strip().replace("(", "").replace(")", "")
        e, n = map(int, content.split(","))
    return e, n

def encrypt_content(content, public_key):
    """Criptografa o conteúdo usando a chave pública RSA."""
    e, n = public_key
    return [pow(ord(char), e, n) for char in content]

def save_encrypted_content(output_path, encrypted_content):
    """Salva o conteúdo criptografado em um arquivo."""
    with open(output_path, "w") as file:
        file.write(",".join(map(str, encrypted_content)))

def encrypt_file():
    """Lê o arquivo input.txt, criptografa e salva o resultado em output.crypt."""
    input_path = "data/input.txt"
    public_key_path = "security/public.cpa"
    output_path = "data/output.crypt"

    if not os.path.exists(input_path):
        raise FileNotFoundError("Arquivo de entrada não encontrado.")

    if not os.path.exists(public_key_path):
        raise FileNotFoundError("Arquivo de chave pública não encontrado.")

    with open(input_path, "r") as file:
        content = file.read()

    public_key = read_public_key(public_key_path)
    encrypted_content = encrypt_content(content, public_key)
    save_encrypted_content(output_path, encrypted_content)