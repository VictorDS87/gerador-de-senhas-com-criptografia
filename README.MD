# Gerador e Gerenciador de Senhas

Este projeto é uma aplicação simples em Python para gerar senhas aleatórias, criptografá-las usando uma técnica de XOR e salvá-las em um arquivo. Além disso, permite recuperar senhas criptografadas usando a mesma técnica de descriptografia.

## Funcionalidades

- **Gerar Senha**: Cria uma senha aleatória com base nas preferências do usuário (tamanho, letras maiúsculas, minúsculas, números e caracteres especiais).
- **Criptografar Senha**: Usa uma chave fornecida pelo usuário para criptografar a senha gerada.
- **Salvar Senha**: Armazena a senha criptografada em um arquivo.
- **Recuperar Senha**: Descriptografa a senha armazenada usando a chave fornecida e exibe a senha original.

## Requisitos

- Python 3.x
- Biblioteca `pyperclip` (para copiar as senhas)

## Uso

Execute o programa com o comando:

```bash
py app.py
