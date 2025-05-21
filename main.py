import os
import time
from cadastro import menu_cadastro_login, logout
from exercicios import iniciar_exercicios
from estatisticas import mostrar_estatisticas

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    usuario = menu_cadastro_login()
    if usuario:
        email = usuario.get("email", "usuário")
        while True:
            print(f"\n🟢 {email} está Online")
            print("\nMenu Principal")
            print("1. Fazer exercícios")
            print("2. Ver estatísticas")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                iniciar_exercicios(usuario)
            elif opcao == "2":
                mostrar_estatisticas(usuario)
            elif opcao == "3":
                print("Saindo...")
                logout(email)
                time.sleep(3)
                limpar_tela()
                print("Finalizado com sucesso.")
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
