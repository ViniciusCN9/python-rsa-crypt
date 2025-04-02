import os

def read_private_key(private_key_path):
    """Lê a chave privada do arquivo."""
    with open(private_key_path, "r") as file:
        content = file.read().strip().replace("(", "").replace(")", "")
        d, n = map(int, content.split(","))
    return d, n

def decrypt_content(encrypted_content, private_key):
    """Descriptografa o conteúdo usando a chave privada RSA."""
    d, n = private_key
    return "".join([chr(pow(int(char), d, n)) for char in encrypted_content])

def decrypt_file():
    """Lê o arquivo output.crypt, descriptografa e retorna o conteúdo original."""
    encrypted_file_path = "data/output.crypt"
    private_key_path = "security/private.csa"

    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError("Arquivo criptografado não encontrado.")
    
    if not os.path.exists(private_key_path):
        raise FileNotFoundError("Arquivo de chave privada não encontrado.")

    with open(encrypted_file_path, "r") as file:
        encrypted_content = file.read().split(",")

    private_key = read_private_key(private_key_path)
    decrypted_content = decrypt_content(encrypted_content, private_key)
    return decrypted_content