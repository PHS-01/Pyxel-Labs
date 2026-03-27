# 🛠️ Tools

Esta pasta contém scripts utilitários desenvolvidos para auxiliar na criação e organização de projetos.

As ferramentas aqui presentes têm como objetivo automatizar tarefas repetitivas e fornecer uma base inicial padronizada para novos projetos.

---

## 📦 create_project.py

Script responsável por criar automaticamente a estrutura base de um novo projeto.

---

## 🎯 Funcionalidades

* Criação automática de uma pasta com o nome do projeto
* Padronização do nome em *kebab-case*
* Geração de:

  * `main.py` → Arquivo principal com a estrutura base do Pyxel
  * `README.md` → Documento inicial para registrar o objetivo e aprendizados do projeto
* Independente de estrutura de diretórios fixa

---

## ▶️ Como utilizar

Execute o script passando o nome do projeto:

```bash id="v5o4j3"
python tools/create_project.py Nome do Projeto
```

---

## 📁 Estrutura Gerada

Ao executar o script, a seguinte estrutura será criada:

```bash
nome-do-projeto/
├── main.py
└── README.md
```

---

## ⚙️ Funcionamento

O script:

1. Converte o nome do projeto para um formato padronizado (*kebab-case*)
2. Cria um diretório no local atual
3. Gera os arquivos iniciais a partir de templates internos

---

## 💡 Observações

* O projeto é criado no diretório atual (`os.getcwd()`)
* O script não sobrescreve pastas existentes
* Os templates podem ser modificados diretamente no código
* O foco da ferramenta é simplicidade e reutilização

---

## 🚀 Possíveis melhorias

* Permitir definição de diretório de destino
* Adicionar criação opcional de pasta `assets/`
* Implementar validação mais robusta do nome
* Transformar o script em uma CLI mais avançada

---

## 🧠 Motivação

A criação dessa ferramenta tem como objetivo:

* Padronizar a criação de novos projetos
* Reduzir repetição de código
* Facilitar o início de novos experimentos
* Tornar o fluxo de desenvolvimento mais ágil

---