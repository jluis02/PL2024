# PL2024

## Unidade Curricular

**Nome:** Processamento de linguagens

**Sigla:** PL

**Ano:** 2024

## Aluno

**Nome:** Luís Costa

**Id:** A100749


# Análise de Dados de Atletas Desportivos

Este conjunto de scripts em Python realiza análises em um conjunto de dados de atletas desportivos, armazenados num arquivo CSV. Cada linha do arquivo representa um atleta e contém informações como `_id`, `nome/primeiro`, `nome/último`, `idade`, `género`, `modalidade`, `federado`, etc.

## Funcionalidades

### Função `ler_dados`

- Lê o conteúdo do arquivo CSV e converte cada linha em uma lista.
- Retorna uma lista de listas, representando os dados dos atletas, excluindo o cabeçalho.

### Função `lista_modalidades_alfabeticamente`

- Organiza as modalidades dos atletas em ordem alfabética.
- Escreve a lista ordenada de modalidades no arquivo "resultados.txt".

### Função `percentagens_aptos_inaptos`

- Calcula as percentagens de atletas aptos e inaptos com base na informação de federado.
- Escreve as percentagens no arquivo "resultados.txt".

### Função `distribuicao_atletas_por_idade`

- Calcula a distribuição de atletas por escalão etário (intervalo de 5 anos).
- Escreve a distribuição no arquivo "resultados.txt".

## Execução

1. Carregue os dados do arquivo "emd.csv".
2. Chame cada uma das funções para realizar as análises e escrever os resultados no arquivo "resultados.txt".

Este código modular fornece diversas análises estatísticas sobre os atletas e documenta os resultados em um arquivo de texto com o nome "resultados.txt".
