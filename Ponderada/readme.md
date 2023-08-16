# Pablinho's Robot

O seguinte projeto foi desenvolvido para a disciplina de Engenharia de Computação no Inteli - Instituto de Tecnologia e Liderança, em 2023.

Para essa simulação da movimentação de um braço robótico, foram utilizados os seguintes tecnologias:

1. Frontend: HTML5 e CSS3, que permitem as entradas das coordenadas da posição do robô na simulação.
2. Backend: servidor desenvolvido em Flask, upado no host CodeSandBox, e banco de dados SQLite para armazenamento das posições.
3. Simulação: software Godot, que permite a visualização de um objeto em 2D, simulando o movimento de um robô.

## Utilizando a aplicação

1. Clone o repositório
2. Realize o download do software Godot 3.
3. Importe o arquivo 'project.godot' disponível no caminho 'godot'
4. Execute a simulação, através do comando 'F5' ou 'F6' no teclado.
5. Abra a página <https://nbo2vi-5000.csb.app/> e realize as entradas de coordenadas.
6. Ao clicar no botão 'Update', as coordenadas serão enviadas para o banco de dados e a simulação será atualizada.

### Documentação da API

Rota de postagem no banco de dados <https://nbo2vi-5000.csb.app/rota>.

Rota de get na última linha do banco de dados <https://nbo2vi-5000.csb.app/get>.
