# DesafioFabricaSoftware
 Desafio da fabrica de software 2024.2

# Chuck Norris Joke Application

Este projeto é uma aplicação web simples em Django que exibe piadas do Chuck Norris. Os usuários podem visualizar uma piada aleatória e traduzi-la para outro idioma.

## Funcionalidades

- Exibir uma piada aleatória do Chuck Norris.
- Traduzir a piada para outro idioma.
- Cadastro e login de usuários.

## Requisitos

- Python 3.x
- Django 5.x
- requests
- googletrans

## Instalação

1. **Crie um ambiente virtual e ative-o**

    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    
2. **Instale as dependências**

    pip install -r requirements.txt

3. **Configure o banco de dados**

    python manage.py migrate

4. **Inicie o servidor**

    python manage.py runserver

5. **Acesse a aplicação**

    Abra o navegador e vá para http://127.0.0.1:8000/.