# Parser de CNAB

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt-br.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](README.es.md)

Uma aplicação web em Django que faz a análise de arquivos CNAB. Esta aplicação permite que você faça upload de um arquivo .txt no formato CNAB, extraia os dados das transações e os armazene em um banco de dados. Os dados de transação podem então ser visualizados e pesquisados através de uma interface amigável ao usuário.

## Tecnologias utilizadas

- Python 3.x
- Django 3.x
- Django Rest Framework
- SQLite3
- Bootstrap 5

## Funcionalidades
- Upload de arquivo CNAB
- Extração de dados de transações
- Exibição de detalhes de transações
- Rotas de transações por ID: `transaction/<int:id>/`
- Busca de transações por CPF
- Validação de tipo de arquivo

## Instalação
- Clone o repositório: `git clone https://github.com/gabrieuz/cnab-parser.git`
- Instale as dependências: `pip install -r requirements.txt`
- Execute as migrações: `python manage.py migrate`
- Inicie o servidor de desenvolvimento: `python manage.py runserver`
- Acesse a aplicação em `http://localhost:8000`

## Uso
- Vá para a página inicial e clique no botão "Escolher arquivo".
- Escolha um arquivo CNAB para fazer upload (CNAB_Example.txt está disponível como exemplo).
- Os dados das transações serão extraídos e exibidos em uma tabela.
- Utilize a barra de pesquisa na barra de navegação para pesquisar transações por CPF.

## Visualizações da interface
![Prévia da interface 1](preview1.png)
![Prévia da interface 2](preview2.png)

## Contribuições
Este é um projeto de código aberto, e contribuições são bem-vindas. Se você tiver alguma ideia ou sugestão, sinta-se à vontade para criar uma pull request.