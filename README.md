# Minhas tarefas

Este é um trabalho de programação python, utilizando o kivymd dos alunos Elzear, Yago, Juan, Gustavo e Lucas da turma de Técnico em Desenvolvimento de Sistemas do SENAI de Itumbiara-GO.

## Sobre o projeto

O projeto foi pensado para ser um app estilo agenda para anotar tarefas para se fazer. Nele há um sistema de login básico, onde não existem usuários, porém deverá ser acessado por qualquer nome de usuário e qualquer senha, onde os campos de senha deverão ser iguais. Deve ser acessado para se conseguir adicionar, remover ou visualizar as tarefas presentes.

### Uso do app

O uso do app é bem simples, basta logar com qualquer usuario ou senha, após isso, aprecerá a página da agenda onde é possivel adicionar novos registros (com um tipo de prioridade, como por exemplo: registro Lavar a Louça, prioridade Média). No topo, há um botão com ícone de lixeira, onde todos os registros são apagados.

### Programação do app

Na tela de login, são utilizados MDTopBar (para um acabamento, onde há um botão que quando é clicado o app é fechado) MDTextField (para inserir os dados), MDRaisedButton, para confirmar o login e um popup caso o login esteja errado;

Na tela de tarefas, foram utilizados um MDTopBar (onde há a opção de voltar apra a tela de login, e também há o ícone de lixeira, para apagar os registros), o MDList para armazenar cada tarefa, MDTextField para inserir dados do registro e um botão para inserir o registro;

No back end, foi utilizado o json para armazenar a lista com as tarefas, para que elas fiquem salvas mesmo após encerrar o app.

Dependências: kivymd e kaki
