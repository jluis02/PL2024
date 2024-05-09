# _id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado

def ler_dados(arquivo):
    with open(arquivo, "r") as file:
        linhas = file.readlines()
    return [linha.strip().split(',') for linha in linhas[1:]]

def lista_modalidades_alfabeticamente(data):
    modalidades = sorted(set(dado[8] for dado in data))  # dado[8] é a modalidade
    with open("resultados.txt", "a") as output_file:
        output_file.write("Lista ordenada alfabeticamente das modalidades desportivas:\n")
        for modalidade in modalidades:
            output_file.write(modalidade + "\n")
        output_file.write("\n___________________________________\n")

def percentagens_aptos_inaptos(data):
    total_atletas = len(data)
    aptos = sum(dado[12] == 'true' for dado in data)
    inaptos = total_atletas - aptos
    perc_aptos = (aptos/total_atletas) * 100
    perc_inaptos = (inaptos/total_atletas) * 100
    with open("resultados.txt", "a") as output_file:
        output_file.write("Percentagens de atletas aptos e não aptos para a prática desportiva:\n")
        output_file.write(f"Percentagens de atletas aptos: {perc_aptos}%\n")
        output_file.write(f"Percentagem de atletas inaptos: {perc_inaptos}%\n")
        output_file.write("\n___________________________________\n")

def distribuicao_atletas_por_idade(data):
    distribuicao_idades = {}
    for dado in data:
        idade = int(dado[5])
        intervalo = f"[{idade // 5 * 5}-{idade // 5 * 5 + 4}]"
        distribuicao_idades[intervalo] = distribuicao_idades.get(intervalo, 0) + 1
    with open("resultados.txt", "a") as output_file:
        output_file.write("Distribuição de atletas por escalão etário:\n")
        for interval, quantity in sorted(distribuicao_idades.items()):
            output_file.write(f"{interval}: {quantity}\n")
        output_file.write("\n___________________________________\n")

# Executando as funções
dados = ler_dados("emd.csv")
lista_modalidades_alfabeticamente(dados)
percentagens_aptos_inaptos(dados)
distribuicao_atletas_por_idade(dados)
