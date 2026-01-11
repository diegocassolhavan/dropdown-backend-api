# Implementation Plan: Dropdown Backend API

## Overview

Implementação de uma API REST em Python usando FastAPI para fornecer listas de números e letras, e receber seleções do usuário. FastAPI foi escolhido por sua simplicidade, performance e suporte nativo a validação com Pydantic.

## Tasks

- [x] 1. Configurar projeto e dependências
  - Criar estrutura de diretórios do projeto
  - Criar requirements.txt com FastAPI, uvicorn, pytest, hypothesis
  - Criar arquivo main.py com configuração básica do FastAPI
  - Configurar CORS middleware
  - _Requirements: 4.1, 4.2_

- [x] 2. Implementar serviços de dados
  - [x] 2.1 Criar NumberService com método get_numbers()
    - Retornar lista de inteiros [1-10]
    - _Requirements: 1.1, 1.3_
  - [x] 2.2 Criar LetterService com método get_letters()
    - Retornar lista de letras ["A"-"J"]
    - _Requirements: 2.1, 2.3_
  - [x] 2.3 Criar SelectionService com validação e processamento
    - Método validate_selection(number, letter)
    - Método process_selection(number, letter)
    - _Requirements: 3.1, 3.3, 3.4, 3.5_

- [x] 3. Implementar modelos Pydantic
  - Criar NumberListResponse
  - Criar LetterListResponse
  - Criar SelectionRequest
  - Criar SelectionResponse
  - _Requirements: 1.1, 2.1, 3.1_

- [x] 4. Implementar endpoints da API
  - [x] 4.1 Implementar GET /api/numbers
    - Retornar NumberListResponse com lista de números
    - _Requirements: 1.1, 1.2, 1.3_
  - [x] 4.2 Implementar GET /api/letters
    - Retornar LetterListResponse com lista de letras
    - _Requirements: 2.1, 2.2, 2.3_
  - [x] 4.3 Implementar POST /api/selection
    - Validar entrada usando SelectionService
    - Retornar sucesso ou erro apropriado
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_

- [x] 5. Checkpoint - Verificar funcionamento básico
  - Garantir que todos os endpoints respondem corretamente
  - Verificar CORS está configurado
  - Perguntar ao usuário se há dúvidas

- [x] 6. Implementar testes
  - [x]* 6.1 Escrever testes unitários para serviços
    - Testar NumberService.get_numbers()
    - Testar LetterService.get_letters()
    - Testar SelectionService.validate_selection()
    - _Requirements: 1.1, 2.1, 3.3, 3.4_
  - [x]* 6.2 Escrever property test para validação de seleções válidas
    - **Property 3: Valid selections are accepted**
    - **Validates: Requirements 3.1**
  - [x]* 6.3 Escrever property test para rejeição de entradas inválidas
    - **Property 4: Invalid inputs are rejected**
    - **Validates: Requirements 3.3, 3.4**
  - [x]* 6.4 Escrever testes de integração para endpoints
    - Testar fluxo completo GET → POST
    - Testar respostas de erro
    - _Requirements: 1.1, 2.1, 3.1_

- [x] 7. Checkpoint final
  - Garantir que todos os testes passam
  - Perguntar ao usuário se há dúvidas

## Notes

- Tasks marcadas com `*` são opcionais e podem ser puladas para um MVP mais rápido
- FastAPI com Pydantic fornece validação automática de tipos
- Hypothesis será usado para property-based testing
- uvicorn será o servidor ASGI para rodar a aplicação
