import json
import statistics
from cadastro import carregar_usuarios

def calcular_estatisticas(lista):
    if not lista:
        return "Sem dados"
    try:
        media = statistics.mean(lista)
        moda = statistics.mode(lista)
        mediana = statistics.median(lista)
        return f"Média: {media:.2f}, Moda: {moda}, Mediana: {mediana}"
    except statistics.StatisticsError:
        media = statistics.mean(lista)
        mediana = statistics.median(lista)
        return f"Média: {media:.2f}, Mediana: {mediana} (moda indefinida)"

def mostrar_estatisticas(usuario):
    print("\n--- Estatísticas Individuais ---")
    pontuacoes = usuario.get("pontuacao", [])
    tempos = usuario.get("tempos", [])

    print("Pontuações:", pontuacoes)
    print("Tempos:", tempos)

    print("\nResumo de pontuação:")
    print(calcular_estatisticas(pontuacoes))

    print("\nResumo de tempo:")
    print(calcular_estatisticas(tempos))

    print("\n--- Estatísticas Gerais ---")
    usuarios = carregar_usuarios()
    idades = [u['idade'] for u in usuarios.values() if 'idade' in u]
    todas_pontuacoes = [p for u in usuarios.values() for p in u.get("pontuacao", [])]

    print("\nIdades dos usuários:")
    print(calcular_estatisticas(idades))

    print("\nPontuação geral:")
    print(calcular_estatisticas(todas_pontuacoes))
