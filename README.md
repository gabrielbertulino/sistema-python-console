# Sistema de Exercícios em Python (Console)

Este projeto é um sistema de exercícios de lógica e fundamentos de Python em modo console, com cadastro de usuários, login seguro, estatísticas e pontuações salvas.

## Funcionalidades

- Cadastro de usuário com nome, idade, e-mail e senha (criptografada)
- Login com autenticação segura (hash com `bcrypt`)
- Módulo de exercícios interativos de Python (if, loops, variáveis)
- Correção automática com feedback
- Registro de pontuação e tempo
- Estatísticas individuais e gerais (média, moda e mediana)
- Indicação de status: 🟢 Online / 🔴 Offline
- Mensagem de finalização com delay e clear na tela

## Requisitos

- Python 3.10+
- Bibliotecas:
  - `bcrypt`
  - `statistics`

Instale o `bcrypt` com:
```bash
pip install bcrypt
```

## Como executar

1. Clone o repositório:
```bash
git https://github.com/gabrielbertulino/gabrielbertulino
cd sistema-python-console
```

2. Execute o sistema principal:
```bash
python main.py
```

## Estrutura de arquivos

```
sistema-python-console/
├── main.py              # Menu principal
├── cadastro.py          # Cadastro, login, logout e segurança
├── seguranca.py         # Funções de hash e criptografia
├── exercicios.py        # Questões, correção e pontuação
├── estatisticas.py      # Relatórios e análises
├── usuarios.json        # Base de dados local
└── README.md
```

## Autor

Projeto desenvolvido por Gabriel Bertulino Sobrinho para fins educacionais.
