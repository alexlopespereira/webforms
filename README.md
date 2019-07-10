## Passos para rodar a aplicação

1) Executar o run_generator.py. Ele é uma aplicação web onde o usuário pode escolher os campos que vão compor o formulario da aplicação web. 
Essa aplicação cria um arquivo chamado curr_schema.js. É esse arquivo que é usado para gerar o formulário que o usuário visualiza.

python run_generator.py

2) Executar a aplicação web que retorna o formulario do serviço criado pelo gerador

python run.py

