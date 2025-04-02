import os
from colorama import init as colorama_init
from colorama import Fore, Style
from decrypt import decrypt_file
from encrypt import encrypt_file
from key_generator import generate_rsa_keys

colorama_init()

def generate_keys():
    print(f"{Fore.YELLOW}Gerando chaves...{Style.RESET_ALL}")
    generate_rsa_keys()
    input(f"{Fore.GREEN}Chaves geradas com sucesso! Pressione qualquer tecla para continuar.{Style.RESET_ALL}")

def encrypt():
    print(f"{Fore.YELLOW}Criptografando dados...{Style.RESET_ALL}")
    try:
        encrypt_file()
    except FileNotFoundError as e:
        input(f"{Fore.RED}Erro: {e} Pressione qualquer tecla para continuar.{Style.RESET_ALL}")
        return
    input(f"{Fore.GREEN}Dados criptografados com sucesso! Pressione qualquer tecla para continuar.{Style.RESET_ALL}")

def decrypt():
    print(f"{Fore.YELLOW}Descriptografando dados...{Style.RESET_ALL}")
    try:
        content = decrypt_file()
    except FileNotFoundError as e:
        input(f"{Fore.RED}Erro: {e} Pressione qualquer tecla para continuar{Style.RESET_ALL}")
        return
    print(f"{Fore.MAGENTA}Conteúdo original: {Style.RESET_ALL}{content}")
    input(f"{Fore.GREEN}Dados descriptografados com sucesso! Pressione qualquer tecla para continuar.{Style.RESET_ALL}")

if __name__ == "__main__":
    while True:
        os.system('cls')
        print(f"\n{Fore.CYAN}============= BEM VINDO ============={Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. Gerar chaves{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2. Criptografar{Style.RESET_ALL} - {Fore.YELLOW}Necessário chaves geradas e arquivo de entrada{Style.RESET_ALL}")
        print(f"{Fore.CYAN}3. Descriptografar{Style.RESET_ALL} - {Fore.YELLOW}Necessário chaves geradas e arquivo criptografado{Style.RESET_ALL}")
        print(f"{Fore.CYAN}0. Sair{Style.RESET_ALL}")
        
        try:
            option = int(input(f"{Fore.CYAN}Escolha uma opção: {Style.RESET_ALL}"))
        except ValueError:
            input(f"{Fore.RED}Opção inválida! Por favor, insira um número entre 0 e 3! Pressione qualquer tecla para continuar.{Style.RESET_ALL}")
            continue

        if option == 1:
            generate_keys()
        elif option == 2:
            encrypt()
        elif option == 3:
            decrypt()
        elif option == 0:
            print(f"{Fore.GREEN}Saindo...{Style.RESET_ALL}")
            break
        else:
            input(f"{Fore.RED}Opção inválida! Por favor, escolha um número entre 0 e 3! Pressione qualquer tecla para continuar.{Style.RESET_ALL}")