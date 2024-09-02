import random
import os
import pyperclip

# Definindo os caracteres disponíveis
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
caracteres_especiais = '/?°"\'!@#$%¨&*()-_=+´[]}{~^<,>.>:;'

# Função para gerar senha aleatória com base nas preferências do usuário
def gerar_senha(tamanho=12, usar_letras_minusculas=True, usar_letras_maiusculas=True, usar_numeros=True, usar_caracteres_especiais=True):
    # Montando a lista de caracteres disponíveis com base nas preferências do usuário
    caracteres_disponiveis = ''
    if usar_letras_minusculas:
        caracteres_disponiveis += letras_minusculas
    if usar_letras_maiusculas:
        caracteres_disponiveis += letras_maiusculas
    if usar_numeros:
        caracteres_disponiveis += numeros
    if usar_caracteres_especiais:
        caracteres_disponiveis += caracteres_especiais

    if not caracteres_disponiveis:
        print("Nenhuma opção de caractere selecionada. A senha não pode ser gerada.")
        return ''

    # Gerando a senha aleatória
    senha_gerada = ''.join(random.choice(caracteres_disponiveis) for _ in range(tamanho))
    return senha_gerada

# Função para criptografar a senha usando XOR
def criptografar(senha, chave):
    senha_criptografada = ''.join(chr(ord(senha[i]) ^ ord(chave[i % len(chave)])) for i in range(len(senha)))
    return senha_criptografada

# Função para descriptografar a senha usando XOR
def descriptografar(senha_criptografada, chave):
    senha_original = ''.join(chr(ord(senha_criptografada[i]) ^ ord(chave[i % len(chave)])) for i in range(len(senha_criptografada)))
    return senha_original

# Função para salvar a senha criptografada em um arquivo
def salvar_senha(nome, senha_criptografada):
    with open('senhas.txt', 'a', encoding='utf-8') as f:
        f.write(f'{nome}:{senha_criptografada}\n')

# Função para carregar a senha criptografada de um arquivo
def carregar_senha(nome):
    if not os.path.exists('senhas.txt'):
        print("Nenhuma senha salva.")
        return None
    with open('senhas.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # Remove espaços em branco ou quebras de linha
            if line.startswith(f'{nome}:'):
                return line.split(':', 1)[1]  # Split apenas no primeiro ':' encontrado
    print("Senha não encontrada.")
    return None

# Menu principal
def main():
    while True:
        escolha = input("Você deseja (1) Gerar uma nova senha ou (2) Recuperar uma senha? (0 para sair): ")
        if escolha == '1':
            nome = input("Digite um nome para a senha: ")
            chave = input("Digite a chave de criptografia: ")
            
            # Perguntar as preferências do usuário
            usar_letras_minusculas = input("Usar letras minúsculas? (s/n): ").lower() == 's'
            usar_letras_maiusculas = input("Usar letras maiúsculas? (s/n): ").lower() == 's'
            usar_numeros = input("Usar números? (s/n): ").lower() == 's'
            usar_caracteres_especiais = input("Usar caracteres especiais? (s/n): ").lower() == 's'
            
            tamanho_senha = int(input("Digite o tamanho da senha desejada (mínimo 1, máximo 15): "))
            if tamanho_senha > 15:
                print("Tamanho da senha alto demais.")
                break
            elif tamanho_senha < 1:
                print("Tamanho da senha baixo demais.")
                break

            senha = gerar_senha(
                tamanho=tamanho_senha,
                usar_letras_minusculas=usar_letras_minusculas,
                usar_letras_maiusculas=usar_letras_maiusculas,
                usar_numeros=usar_numeros,
                usar_caracteres_especiais=usar_caracteres_especiais
            )

            if senha:  # Verifica se a senha foi gerada com sucesso
                senha_criptografada = criptografar(senha, chave)
                salvar_senha(nome, senha_criptografada)
                print(f"Senha gerada e salva.")
            else:
                print("A senha não pôde ser gerada devido à falta de opções de caracteres.")

        elif escolha == '2':
            chave = input("Digite a chave de criptografia: ")
            nome = input("Digite o nome da senha a ser recuperada: ")
            senha_criptografada = carregar_senha(nome)
            if senha_criptografada:
                senha_original = descriptografar(senha_criptografada, chave)
                pyperclip.copy(senha_original)
                print(f"Senha recuperada: {senha_original}. Salva para a área de transferência")
        elif escolha == '0':
            print("Encerrando o programa.")
            break
        else:
            print("Escolha inválida.")

# Executa o programa
if __name__ == "__main__":
    main()

