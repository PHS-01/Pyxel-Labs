<div align="center">
  <a href="https://github.com/kitao/pyxel"><img src="https://raw.githubusercontent.com/kitao/pyxel/main/docs/images/pyxel_logo_152x64.png" alt="Logo" height="90"></a>
  <p align="center"><a href="https://kitao.github.io/pyxel/web/user-guide/"><strong>Documentação »</strong></a></p>
</div>

# 📘 Introdução

O **Pyxel** é uma engine de jogos retrô (caracterizados por limitações intencionais) para Python, focada na simplicidade e produtividade. Ele permite o desenvolvimento de jogos 2D com gráficos em pixel art, suporte a áudio (efeitos sonoros e música) e uma estrutura de execução direta, sendo especialmente adequado para iniciantes e para prototipação rápida.

Este repositório tem como objetivo documentar meu processo de aprendizado com a ferramenta, reunindo conceitos fundamentais, boas práticas e exemplos práticos desenvolvidos ao longo dos estudos.

# 🏗️ Estrutura de um Projeto em Pyxel

O Pyxel recomenda organizar o projeto utilizando **encapsulamento em classe**, centralizando a lógica do jogo em um único objeto, juntamente com configurações de execução e metadados para distribuição.

Essa abordagem facilita a manutenção, organização e escalabilidade do projeto.

## 🧱 Estrutura Base do Código

Um projeto típico em Pyxel pode ser estruturado da seguinte forma:

```python
# title: Meu Jogo
# author: Seu Nome
# desc: Exemplo de estrutura básica em Pyxel
# version: 1.0

import pyxel

class App:
    def __init__(self):
        # 🎛️ Inicialização da aplicação
        # Nem todos os parâmetros são obrigatórios
        pyxel.init(
            width=160,
            height=120,
            title="Meu Jogo",
            fps=60
        )

        # 🔄 Estado inicial das variáveis
        self.x = 80
        self.y = 60

        # ▶️ Loop principal
        pyxel.run(self.update, self.draw)

    def update(self):
        # 🧠 Lógica do jogo
        # Responsável por atualizar estados com base na lógica definida

    def draw(self):
        # 🎨 Renderização
        # Responsável apenas por desenhar os elementos na tela
        # Evitar colocar lógica aqui
        pyxel.cls(0)

# 🚀 Execução
App()
```

## ⚙️ Configuração da Aplicação

A função `pyxel.init()` define os parâmetros de execução do jogo.

### 📌 Principais parâmetros

- `width` → largura da tela  
- `height` → altura da tela  
- `title` → título da janela  
- `fps` → taxa de atualização  
    
Essas configurações afetam diretamente o comportamento da aplicação em tempo de execução.

## 📦 Metadados para Distribuição

Os metadados utilizados na distribuição são definidos no topo do arquivo principal:

```python
# title: Meu Jogo
# author: Seu Nome
# desc: Descrição do projeto
# site: https://seusite.com
# license: MIT
# version: 1.0
```

### 📌 Campos disponíveis

-   `title` (obrigatório)
-   `author` (obrigatório)
-   `desc`
-   `site`  
-   `license`   
-   `version`
    
Esses dados são utilizados na criação do arquivo `.pyxapp`.

## 🔄 Empacotamento e Execução

### 📦 Gerar aplicação

```bash
pyxel package APP_DIR STARTUP_SCRIPT_FILE
```

### ▶️ Executar aplicação

```bash
pyxel play NOME_DO_APP.pyxapp
```

### 🔧 Conversão

-   Executável:
    
```bash
pyxel app2exe NOME_DO_APP.pyxapp
```

-   HTML:
    
```bash
pyxel app2html NOME_DO_APP.pyxapp
```

## 💡 Observações

- O uso de **encapsulamento em classe** não é obrigatório, mas é uma boa prática recomendada  
- A separação entre `update()` e `draw()` melhora a organização e previsibilidade do código  
- `pyxel.init()` define o comportamento da aplicação em tempo de execução  
- Os metadados são utilizados apenas para distribuição  
- Essa estrutura serve como base para projetos mais complexos  

## 🔗 Referências

> Escrito com [StackEdit](https://stackedit.io/)  
> Repositório do Projeto: [Pyxel](https://github.com/kitao/pyxel)  
> Desenvolvedor: [Takashi Kitao](https://github.com/kitao)  
> Documentação: [Guia Oficial](https://kitao.github.io/pyxel/web/user-guide/)

---
