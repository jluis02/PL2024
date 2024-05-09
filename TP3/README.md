# PL2024

## Unidade Curricular

**Nome:** Processamento de linguagens

**Sigla:** PL

**Ano:** 2024

## Aluno

**Nome:** Luís Costa

**Id:** A100749


## Explicação do código do TPC3

Este código em Python lê linhas de entrada do stdin, processa os símbolos encontrados e realiza operações de soma ou desligamento com base nesses símbolos.

1. Se encontrar 'on', define a variável somador como True.
2. Se encontrar 'off', define a variável somador como False.
3. Se encontrar um número (dígitos) e somador for True, adiciona o número à variável current.
4. Se encontrar '=', imprime a soma acumulada (current).
