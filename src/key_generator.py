import random
from prime_generator import generate_prime

def gcd(a, b):
    """Calcula o máximo divisor comum (MDC)."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Calcula o inverso modular de e módulo phi usando o algoritmo estendido de Euclides."""
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("O inverso modular não existe.")
    return x % phi

def extended_gcd(a, b):
    """Algoritmo estendido de Euclides para encontrar o inverso modular."""
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x
    
def save_keys_to_file(public_key, private_key):
    """Salva as chaves pública e privada em arquivos."""

    with open("security/public.cpa", "w") as public_file:
        public_file.write(f"{public_key}")
    
    with open("security/private.csa", "w") as private_file:
        private_file.write(f"{private_key}")

def generate_rsa_keys():
    """Gera um par de chaves RSA (chave pública e chave privada)."""
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = mod_inverse(e, phi)
    
    public_key = (e, n)
    private_key = (d, n)
    
    save_keys_to_file(public_key, private_key)