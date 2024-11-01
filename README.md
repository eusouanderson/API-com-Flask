# API de Jogo Multiplayer 2D

Esta é uma API desenvolvida em Flask para um jogo multiplayer 2D chamado "Akido Arena". A API permite a criação, recuperação, atualização e exclusão de informações sobre os jogos disponíveis.

## Estrutura do Projeto

/api-com-Flask
|-- main.py
|-- bd
| |--  **init** .py # (opcional, mas ajuda com a importação)
| |-- bd.py
|-- models.py



## Tecnologias Utilizadas

- Python 3.x
- Flask

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Você também precisará do gerenciador de pacotes `poetry`.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/api-com-Flask.git
   cd api-com-Flask
   ```
2. Instale as dependências usando o Poetry:
    ```bash
    poetry install
    ```


## Uso

Para executar a API, use o seguinte comando:
```bash
poetry run python main.py
```