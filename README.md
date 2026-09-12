# api-gestao
Será um projeto semelhante ao trello, focado em gerenciar projetos. 
Não haverá autenticação pesada de inicio, só algo para saber quais dados pertencem a quem e quem vai ver aqueles dados.

vai ser um single-tenent, por enquanto, depois penso em evoluir para um multi-tenent

### Dominio do projeto
Teremo um Usuário que vai conseguir manipular as Tarefas (para simplificar esse inicio) e cada tarefa pode ter ou não subtarefas.
Um usuário vai ter nome, email e password_hash (bycript) - Mais para frente da pra adicionar roles e permissões
Os boards serão responsávei por armazenar as tarefas, sendo, por exemplo, um boards de completo, em andamento ou semelhantes 
e terão seu título e ordem, pois deve ser possível manipular se o completo é apresentado primeiro ou não.
As tarefas terão título, descrição, data de encerramento, subtarefas, status.
As subtarefas terão, apenas, descrição, status e data de encerramento.

### Modelo conceitual do banco
users
- id 
- name
- email
- password_hash

boards
- id 
- title
- order 
- user_id

tasks
- id
- title
- description
- due_date
- status
- border_id

subtasks
- id
- description
- completed
- due_date
- task_id

Por enquanto, sem regras de negócios mais complexas, vamos manter no simples.