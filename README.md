# 🧩 Gerenciador de Tarefas CLI em Python

Projeto desenvolvido em **Python** para gerenciamento de tarefas via **linha de comando (CLI)**, com foco no aprendizado prático de **lógica de programação**, **organização de código**, **persistência de dados** e **boas práticas iniciais de desenvolvimento backend**.

Este é meu **primeiro projeto completo**, construído durante meus estudos em programação e com apoio de **Inteligência Artificial como ferramenta de aprendizado**, sempre buscando entender cada parte do código.

---

## 🚀 Funcionalidades

- Criar novas tarefas  
- Listar tarefas cadastradas  
- Atualizar status das tarefas  
- Remover tarefas  
- Persistência de dados (as tarefas permanecem salvas entre execuções)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **SQLite** (persistência de dados)
- **Git & GitHub**
- **Arquitetura simples em camadas (CLI, serviços, modelos)**

---

## 📂 Estrutura do Projeto

gerenciador_tarefas_cli/
│
├── src/
│   ├── cli.py        # Interface de linha de comando
│   ├── services.py  # Regras de negócio
│   ├── models.py    # Modelos de dados
│   ├── storage.py   # Persistência (SQLite)
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

```bash
git clone https://github.com/edaquinogit/gerenciador_tarefas_cli.git

2️⃣ Acesse a pasta do projeto

cd gerenciador_tarefas_cli

3️⃣ Execute o programa

python main.py

🧠 O que aprendi com este projeto
Organização de código em múltiplos arquivos


Separação de responsabilidades


Manipulação de dados persistentes


Tratamento básico de erros e entradas do usuário


Uso do Git para versionamento


Como transformar um problema simples em um projeto funcional



📌 Próximos Passos (Evolução Planejada)
Melhorar validação de entradas do usuário


Adicionar testes automatizados básicos


Criar documentação técnica mais detalhada


Evoluir o projeto para uma API REST futuramente



👨‍💻 Sobre mim
Sou estudante de Gestão da Tecnologia da Informação, com foco em Backend Python, automação e aprendizado prático através de projetos reais.
📌 Estou em busca de oportunidades de estágio ou vaga júnior, onde eu possa continuar aprendendo e contribuindo com o time.
🔗 LinkedIn:https://www.linkedin.com/in/ednaldo-aquino-6536892b5

⭐ Observação Final
Este projeto representa meu nível atual de aprendizado e minha capacidade de aprender, estruturar e finalizar uma solução funcional, algo essencial para quem está iniciando na área de tecnologia.
Feedbacks e sugestões são muito bem-vindos.
