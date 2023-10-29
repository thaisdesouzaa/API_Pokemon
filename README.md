﻿# API_Pokemon


Esse foi um projeto desenvolvido para o processo seletivo da Triágil.

- A rota GET/api/teams realiza uma busca de todos os times registrados
- A rota POST/api/teams cria um novo time, passando como parâmetro um nome de usuário e uma lista de pokémons
- A rota GET/api/teams{id} realiza uma busca dos times através da ID do time

## Tratamento de erros aplicado no código
### Mundo dos Pokemons
- Não é aceito time com mais de 6 pokémons
- Não é aceito time vazio

### Retorna erro quando o input contém algum erro:
- Nome de pokémon inválido
- Id não encontrado durante a rota GET/api/teams{id}
- Nenhum time encontrado durante a rota GET/api/teams





