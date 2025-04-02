import random

def is_prime(n, k=40):
    """Testa se um número é primo usando o teste de Miller-Rabin."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    # Escreve n - 1 como 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Realiza k iterações do teste de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

def generate_prime(bits=128):
    """Gera um número primo de um determinado número de bits."""
    while True:
        candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1  # Garante que seja ímpar e tenha o tamanho correto
        if is_prime(candidate):
            return candidate