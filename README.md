# 🧩 Gerenciador de Tarefas CLI em Python

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-concluído-green)
![Tipo](https://img.shields.io/badge/projeto-estudo%20prático-informational)

Projeto de **linha de comando (CLI)** desenvolvido em **Python**. Permite gerenciar tarefas com persistência, interface colorida e menu interativo.  

Mostra boas práticas de programação, modularidade e atenção à experiência do usuário.

---

## 🚀 Funcionalidades

- Adicionar **múltiplas tarefas** de uma vez, evitando duplicatas.
- Remover tarefas pelo **número da lista**.
- Listar tarefas numeradas com cores.
- Persistência de tarefas em `tasks.json`.
- Validação de entradas e tratamento de erros.
- Interface amigável e intuitiva com **colorama**.

---

## 💻 Tecnologias e Conceitos

- **Python 3.10+**
- **colorama** → interface colorida no terminal.
- **JSON** → armazenamento persistente de dados.
- Modularização (`tasks.py` e `main.py` separados).
- Funções, loops, listas e tratamento de exceções.
- Estrutura de pacotes Python (`src`).

---

## 📂 Estrutura do Projeto

gerenciador_tarefas_cli/
│
├─ .venv/ # Ambiente virtual
├─ src/
│ ├─ init.py # Pacote Python
│ ├─ main.py # Menu interativo do CLI
│ └─ tasks.py # Funções de gerenciamento de tarefas
├─ tasks.json # Armazena tarefas persistentes
└─ README.md # Documentação do projeto

---

## ⚡ Como Executar

1. Clone o repositório:

```bash
git clone <https://github.com/edaquinogit/gerenciador_tarefas_cli>
cd gerenciador_tarefas_cli

Crie e ative o ambiente virtual:

python -m venv .venv

.\.venv\Scripts\activate  # Windows

# source .venv/bin/activate  # Linux / Mac

Instale dependências:

pip install colorama

Execute o programa:

python -m src.main
```
**🎯 Exemplos de Uso**

*Adicionar tarefas:*

Escolha uma opção: 1

Digite as tarefas separadas por vírgula: Estudar Python, Ler documentação

*Remover tarefas por número:*

Escolha uma opção: 2

Digite os números das tarefas para remover, separados por vírgula: 1

Listar tarefas:

*Tarefas atuais:*

1. Ler documentação

**✅ Boas Práticas Demonstradas**

Modularização em funções reutilizáveis (add_tasks, remove_tasks, list_tasks).

Persistência de dados com JSON.

Interface colorida e amigável com colorama.

Validação de entradas, tratamento de erros e mensagens de feedback.

Organização do projeto em pacotes Python, alinhado a boas práticas de desenvolvimento.

**🔮 Próximos Passos / Evolução**

Adicionar prioridade ou categoria às tarefas.

Implementar edição de tarefas no CLI.

Exportar tarefas para CSV ou TXT.

Criar testes automatizados com pytest ou unittest.

Implementar logs de ações para histórico de tarefas.

👤 Autor:

Ednaldo Aquino Santos – Desenvolvedor iniciante em Python, focado em problemas reais, boas práticas e projetos práticos para o mercado de TI.
