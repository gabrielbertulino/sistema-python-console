import time
import json
from cadastro import carregar_usuarios, salvar_usuarios

EXERCICIOS = [
    {
        "pergunta": "Qual é a saída de: print(2 + 3 * 4)?",
        "resposta": "14"
    },
    {
        "pergunta": "Como declarar uma variável com o valor 10?",
        "resposta": "x = 10"
    },
    {
        "pergunta": "Qual estrutura condicional usamos para múltiplas opções?",
        "resposta": "if elif else"
    },
    {
        "pergunta": "Qual é a função para receber dados do usuário?",
        "resposta": "input"
    },
    {
        "pergunta": "Qual é a saída de: print(len('Python'))?",
        "resposta": "6"
    }
]

def iniciar_exercicios(usuario):
    print("\nIniciando exercícios de lógica...")
    acertos = 0
    inicio = time.time()

    for i, ex in enumerate(EXERCICIOS, 1):
        print(f"\nQuestão {i}: {ex['pergunta']}")
        resposta = input("Resposta: ").strip().lower()
        if resposta == ex['resposta'].lower():
            print("✅ Correto!")
            acertos += 1
        else:
            print(f"❌ Errado. Resposta correta: {ex['resposta']}")

    fim = time.time()
    tempo_gasto = round(fim - inicio, 2)

    print(f"\nPontuação final: {acertos}/{len(EXERCICIOS)}")
    print(f"Tempo total: {tempo_gasto} segundos")

    usuarios = carregar_usuarios()
    email = usuario["email"]
    if email in usuarios:
        usuarios[email]["pontuacao"].append(acertos)
        usuarios[email]["tempos"].append(tempo_gasto)
        salvar_usuarios(usuarios)