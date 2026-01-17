# Projeto TCP/UDP DSD

Demonstração de envio e recebimento de dados utilizando os protocolos TCP e UDP para a disciplina de Desenvolvimento de Sistemas Distribuídos.

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Bulma](https://img.shields.io/badge/Bulma-00D1B2?style=for-the-badge&logo=bulma&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## Funcionamento

Um cliente Python se conecta a um servidor Python via TCP. Uma vez que a conexão foi estabelecida, o cliente passa a mandar um payload JSON com dados demonstrativos de temperatura e umidade gerados aleatoriamente.

Para integrar a uma aplicação web, foi utilizado o Django. Dentro do Django, o servidor atua via channels mandando os dados para um consumer websocket que atualiza o frontend via JavaScript de forma assíncrona, em tempo real.

Por fim, foi utilizado Docker Compose para simplificar o processo de execução e configuração do projeto e suas dependências, como o Redis e as bibliotecas Python.

## Como rodar

Com o Docker instalado na máquina, basta executar ```docker compose up --build``` na pasta raiz do projeto. A aplicação web estará disponível em localhost na porta 8000.


