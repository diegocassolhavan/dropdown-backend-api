# Requirements Document

## Introduction

API back-end para fornecer dados aos dropdowns de uma aplicação front-end "Seletor de Opções". A API deve disponibilizar listas de números e letras, além de receber e processar as seleções feitas pelo usuário.

## Glossary

- **API**: Interface de programação que expõe endpoints HTTP REST
- **Dropdown_Service**: Serviço responsável por fornecer as listas de opções
- **Selection_Service**: Serviço responsável por receber e processar as seleções do usuário
- **Number_List**: Lista de números disponíveis para seleção
- **Letter_List**: Lista de letras disponíveis para seleção
- **User_Selection**: Objeto contendo o número e a letra escolhidos pelo usuário

## Requirements

### Requirement 1: Fornecer Lista de Números

**User Story:** Como front-end, eu quero obter uma lista de números via API, para que eu possa popular o dropdown de números.

#### Acceptance Criteria

1. WHEN o front-end faz uma requisição GET para o endpoint de números THEN THE Dropdown_Service SHALL retornar uma lista de números em formato JSON
2. WHEN a requisição é bem-sucedida THEN THE Dropdown_Service SHALL retornar status HTTP 200
3. THE Number_List SHALL conter números inteiros

### Requirement 2: Fornecer Lista de Letras

**User Story:** Como front-end, eu quero obter uma lista de letras via API, para que eu possa popular o dropdown de letras.

#### Acceptance Criteria

1. WHEN o front-end faz uma requisição GET para o endpoint de letras THEN THE Dropdown_Service SHALL retornar uma lista de letras em formato JSON
2. WHEN a requisição é bem-sucedida THEN THE Dropdown_Service SHALL retornar status HTTP 200
3. THE Letter_List SHALL conter letras do alfabeto

### Requirement 3: Receber Seleção do Usuário

**User Story:** Como front-end, eu quero enviar a seleção do usuário (número e letra) para o back-end, para que a escolha seja processada.

#### Acceptance Criteria

1. WHEN o front-end envia uma requisição POST com número e letra selecionados THEN THE Selection_Service SHALL receber e processar os dados
2. WHEN a seleção é recebida com sucesso THEN THE Selection_Service SHALL retornar status HTTP 200 com confirmação
3. IF o número enviado não estiver na lista válida THEN THE Selection_Service SHALL retornar status HTTP 400 com mensagem de erro
4. IF a letra enviada não estiver na lista válida THEN THE Selection_Service SHALL retornar status HTTP 400 com mensagem de erro
5. IF o corpo da requisição estiver incompleto THEN THE Selection_Service SHALL retornar status HTTP 400 com mensagem de erro

### Requirement 4: Suporte a CORS

**User Story:** Como front-end hospedado em domínio diferente, eu quero que a API permita requisições cross-origin, para que eu possa consumir os endpoints.

#### Acceptance Criteria

1. THE API SHALL incluir headers CORS apropriados para permitir requisições de origens diferentes
2. WHEN uma requisição OPTIONS é recebida THEN THE API SHALL responder com os headers CORS corretos
