# 🧩 Gerenciador de Tarefas CLI em Python

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-concluído-green)
![Tipo](https://img.shields.io/badge/projeto-estudo%20prático-informational)

Projeto desenvolvido em **Python** para gerenciamento de tarefas via **linha de comando (CLI)**, com foco no aprendizado prático de **lógica de programação**, **organização de código**, **persistência de dados** e **boas práticas iniciais de desenvolvimento backend**.

Este é meu **primeiro projeto completo**, construído durante meus estudos em programação, utilizando **Inteligência Artificial como ferramenta de apoio ao aprendizado**, sempre priorizando a compreensão do código e das decisões técnicas.

---

## 🚀 Funcionalidades

- Criar novas tarefas  
- Listar tarefas cadastradas  
- Atualizar o status das tarefas  
- Remover tarefas  
- Persistência de dados (as tarefas permanecem salvas entre execuções)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **SQLite** (persistência de dados)
- **Git & GitHub**
- **Aplicação CLI (Command Line Interface)**

---

## 📌 Pré-requisitos

- Python **3.10 ou superior**
- Git
- Terminal (Windows, Linux ou macOS)

---

## 📂 Estrutura do Projeto

gerenciador_tarefas_cli/
│
├── src/
│   ├── cli.py        # Interface de linha de comando
│   ├── services.py  # Regras de negócio
│   ├── models.py    # Modelos de dados
│   ├── storage.py   # Persistência de dados (SQLite)
│   └── init.py
│
├── main.py           # Ponto de entrada da aplicação
├── tarefas.db        # Banco de dados SQLite
├── README.md
├── .gitignore
└── LICENSE
---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório


git clone https://github.com/edaquinogit/gerenciador_tarefas_cli.git

2️⃣ Acesse a pasta do projeto

cd gerenciador_tarefas_cli

3️⃣ Execute a aplicação

python main.py

```bash
🖥️ Exemplo de Uso no Terminal

$ python main.py

1 - Criar tarefa
2 - Listar tarefas
3 - Atualizar status
4 - Remover tarefa
5 - Sair

Escolha uma opção: 1
Digite o título da tarefa: Estudar Python
Digite a descrição: Revisar conceitos de funções
Tarefa criada com sucesso!

```
🧠 O que aprendi com este projeto
Organização de código em múltiplos arquivos


Separação de responsabilidades


Manipulação de dados persistentes


Uso de banco de dados SQLite


Tratamento básico de entradas do usuário


Versionamento de código com Git e GitHub


Como transformar um problema simples em uma aplicação funcional



📌 Próximos Passos (Evolução Planejada)
Melhorar validação de entradas do usuário


Adicionar testes automatizados básicos


Criar documentação técnica mais detalhada


Evoluir o projeto para uma API REST futuramente


👨‍💻 Sobre mim
Sou estudante de Gestão da Tecnologia da Informação, com foco em Backend Python, automação e aprendizado prático através de projetos reais.
📌 Estou em busca de oportunidades de estágio ou vaga júnior, onde eu possa continuar evoluindo tecnicamente e contribuir com o time.
🔗 LinkedIn: https://www.linkedin.com/in/ednaldo-aquino-6536892b5

⭐ Observação Final
Este projeto representa meu nível atual de aprendizado e minha capacidade de planejar, estruturar e finalizar uma solução funcional, habilidades fundamentais para quem está iniciando na área de tecnologia.
Feedbacks e sugestões são sempre bem-vindos.

