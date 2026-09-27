# Agrupando importações necessárias para o projeto 
import os
import csv
import json
import random
import re
from datetime import datetime, timedelta

def carregar_dataset(caminho_csv):
    """Le o CSV e retorna uma lista de dicionarios (um por registro)."""
    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        registros = list(leitor)
    return registros

def inspecionar_dados(registros):
    """Exibe as informacoes estruturais da lista de registros."""
    total = len(registros)
    colunas = list(registros[0].keys()) if registros else []

    nulos = {coluna: 0 for coluna in colunas}
    for linha in registros:
        for coluna in colunas:
            if linha.get(coluna, "").strip() == "":
                nulos[coluna] += 1

    print("\n=== INSPECAO INICIAL DO DATASET ===")
    print(f"Total de registros: {total}")
    print(f"\nColunas: {colunas}")
    print(f"\nValores ausentes por coluna:\n{nulos}")
    print("\nPrimeiros registros:")
    for linha in registros[:5]:
        print(linha)
    return registros

# Próximo bloco de funções em cumprimento ao RF03 do guia

def limpar_dados(registros):
    """
    Limpa e trata a lista de registros de vendas.
    Retorna: (registros_limpos, relatorio), onde relatorio e um dicionario
    com as contagens de registros iniciais, removidos e finais.
    """
    relatorio = {"iniciais": len(registros), "removidos_data": 0,
                 "removidos_nulos": 0, "finais": 0}
    padrao_cliente = re.compile(r"^Cliente_\d{3}$", flags=re.IGNORECASE)
    limpos = []

    for linha in registros:
        # 1. remover espacos extras nas colunas de texto
        for chave in ("cliente", "produto", "categoria", "regiao"):
            linha[chave] = linha[chave].strip()

        # 2. converter data_venda e descartar datas invalidas
        try:
            linha["data_venda"] = datetime.strptime(linha["data_venda"], "%Y-%m-%d")
        except ValueError:
            relatorio["removidos_data"] += 1
            continue

        # 3. descartar nulos em quantidade e preco_unitario
        if linha["quantidade"] == "" or linha["preco_unitario"] == "":
            relatorio["removidos_nulos"] += 1
            continue

        # 4. ajustar os tipos numericos
        linha["quantidade"] = int(float(linha["quantidade"]))
        linha["preco_unitario"] = float(linha["preco_unitario"])

        # 5. padronizar o nome do cliente com re.sub()
        nome_limpo = re.sub(r"[^A-Za-z0-9_]", "", linha["cliente"])
        linha["cliente"] = nome_limpo
        linha["cliente_fora_do_padrao"] = padrao_cliente.match(nome_limpo) is None

        limpos.append(linha)

    # 6. montar e imprimir o relatorio de limpeza
    relatorio["finais"] = len(limpos)
    print("\n=== RELATORIO DE LIMPEZA ===")
    print(relatorio)
    return limpos, relatorio

# Trecho de apoio:
# # conversao de data com tratamento de erro
# def converter_data(registros):
#     texto_data = registros["data_venda"]
#     nome = ""
#     try:
#         data = datetime.strptime(texto_data, "%Y-%m-%d")
#     except ValueError:
#         data = None                       # marca como invalida

#     # limpeza de texto com expressao regular
#     nome_limpo = re.sub(r"[^A-Za-z0-9_]", "", nome.strip())

#     # validacao de formato com padrao compilado
#     padrao_cliente = re.compile(r"^Cliente_\d{3}$", flags=re.IGNORECASE)
#     return padrao_cliente

def criar_colunas_derivadas(registros):
    # Mapeamento de meses em portugues (Semana 04/05 - Dicionários)
    nome_mes = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    for linha in registros:
        # Cálculo da receita total
        receita = round(linha["quantidade"] * linha["preco_unitario"], 2)
        linha["receita_total"] = receita

        # Extracao de mes e ano via objeto datetime (Semana 05)
        mes = linha["data_venda"].month
        linha["mes"] = mes
        linha["ano"] = linha["data_venda"].year

        # Nome do mes em portugues
        linha["mes_nome"] = nome_mes[mes]

        # Classificacao do trimestre com if/elif/else (S03)
        if mes in (1, 2, 3):
            linha["trimestre"] = "Q1"
        elif mes in (4, 5, 6):
            linha["trimestre"] = "Q2"
        elif mes in (7, 8, 9):
            linha["trimestre"] = "Q3"
        else:
            linha["trimestre"] = "Q4"

        # Classificacao da faixa de receita do item (S03)
        if receita < 500:
            linha["faixa_receita_item"] = "Baixo Valor"
        elif receita < 5000:
            linha["faixa_receita_item"] = "Medio Valor"
        else:
            linha["faixa_receita_item"] = "Alto Valor"

    return registros
