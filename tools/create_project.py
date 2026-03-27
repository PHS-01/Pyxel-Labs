import os
import sys

MAIN_TEMPLATE = """
import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="{title}")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

App()
"""

README_TEMPLATE = """
# 🎮 {title}

## 📌 Objetivo

Descrever o objetivo do projeto.

## 🧠 O que aprendi

- 

## 💻 Execução

```bash
python main.py
```

## ⚠️ Dificuldades

## 💡 Insights
"""

def create_project(name):
    folder_name = name.replace(" ", "-").lower()
    path = os.path.join(os.getcwd(), folder_name)

    if os.path.exists(path):
        return print("\nErro: pasta já existe.\n")
    else:
        os.makedirs(path)

        # main.py
        main_code = MAIN_TEMPLATE.format(title=name)
        with open(os.path.join(path, "main.py"), "w") as f:
            f.write(main_code)

        # README.md
        readme = README_TEMPLATE.format(title=name)
        with open(os.path.join(path, "README.md"), "w") as f:
            f.write(readme)

        return print(f"\n✔ Projeto '{name}' criado em: {path}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nUso: python create_project.py nome-do-projeto\n")
    else:
        create_project(" ".join(sys.argv[1:]))