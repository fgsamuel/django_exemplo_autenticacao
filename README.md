# Tutorial: Autenticação no Django

Este repositório é baseado no vídeo tutorial do YouTube que pode ser acessado neste [link](https://youtu.be/nLQoAlxABX4).

Se você gostar do projeto/vídeo, lembre de marcar este projeto com uma estrela para fortalecer o projeto.

## Rodando o projeto localmente

* Faça o checkout do projeto para a sua máquina local
* Acesse a pasta que acabou de baixar
* Execute o comando `pip install -r requirements.txt` para instalar as dependências
* Execute o comando `python manage.py migrate` para gerar o banco de dados sqlite3
* Execute o comando `python manage.py createsuperuser` e informe usuário e senha para criar um administrador
* Execute o comando `python manage.py runserver` para inicar o projeto
* Acesse o endereço `localhost:8000` para ver o projeto rodando.

Quando você tentar acessar as páginas 1 ou 2 você será redirecionado para a página de login.

A página de login foi retirada deste [link](https://bootsnipp.com/snippets/GaZG0)