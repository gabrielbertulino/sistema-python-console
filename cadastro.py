import json
import os
import bcrypt

ARQUIVO_USUARIOS = 'usuarios.json'

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {}
    try:
        with open(ARQUIVO_USUARIOS, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f, indent=4)

def criptografar_senha(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt).decode('utf-8')

def verificar_senha(senha, senha_armazenada):
    return bcrypt.checkpw(senha.encode(), senha_armazenada.encode())

def cadastrar_usuario():
    usuarios = carregar_usuarios()
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")
    if email in usuarios:
        print("Usuário já cadastrado.")
        return None
    senha = input("Senha: ")
    senha_criptografada = criptografar_senha(senha)

    usuarios[email] = {
        "nome": nome,
        "idade": int(idade),
        "email": email,
        "senha": senha_criptografada,
        "pontuacao": [],
        "tempos": [],
        "online": False
    }
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")
    return usuarios[email]

def login():
    usuarios = carregar_usuarios()
    email = input("Email: ")
    senha = input("Senha: ")
    if email in usuarios and verificar_senha(senha, usuarios[email]['senha']):
        usuarios[email]['online'] = True
        salvar_usuarios(usuarios)
        print(f"Login realizado com sucesso! 🟢 Online")
        return usuarios[email]
    print("Email ou senha incorretos!")
    return None

def logout(email):
    usuarios = carregar_usuarios()
    if email in usuarios:
        usuarios[email]['online'] = False
        salvar_usuarios(usuarios)
        print("Usuário saiu do sistema. 🔴 Offline")

def menu_cadastro_login():
    while True:
        print("\n1. Cadastrar usuário")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            user = cadastrar_usuario()
            if user:
                return user
        elif opcao == "2":
            user = login()
            if user:
                return user
        elif opcao == "3":
            return None
        else:
            print("Opção inválida!")