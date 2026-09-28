# Agrupando importações necessárias para o projeto 
import os
import csv
import json
import random
import re
from datetime import datetime, timedelta
from collections import defaultdict # RF05

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


def calcular_metricas(registros):
    """
    Calcula as metricas agregadas da lista de registros.
    Retorna um dicionario no formato {nome_da_metrica: lista_de_linhas}.
    Chaves minimas: por_mes, top_produtos, por_categoria, por_regiao.
    """
    #metricas = {}
    # use dicionarios (ou defaultdict) para acumular receita_total,
    # quantidade e numero de vendas por mes, produto, categoria e
    # regiao; depois converta cada dicionario em uma lista ordenada
    # de registros (dict.items() + sorted())
    
    # Criando as variáveis vazias que receberão os dados:
    caixas_mes = {}
    caixas_produto = {}
    caixas_categoria = {}
    caixas_regiao = {}

    # Percorrendo os registros com for e somando nas variáveis
    for reg in registros:
        
    # --- Agrupando por Mês ---
        mes = reg["mes"]
        if mes not in caixas_mes:
            caixas_mes[mes] = {"receita_total": 0, "quantidade": 0, "n_vendas": 0}
        
        caixas_mes[mes]["receita_total"] += reg["receita_total"]
        caixas_mes[mes]["quantidade"] += reg["quantidade"]
        caixas_mes[mes]["n_vendas"] += 1
        
        # --- Agrupando por Produto ---
        produto = reg["produto"]
        if produto not in caixas_produto:
            caixas_produto[produto] = {"receita_total": 0}
        
        caixas_produto[produto]["receita_total"] += reg["receita_total"]
        
        # --- Agrupando por Categoria ---
        categoria = reg["categoria"]
        if categoria not in caixas_categoria:
            caixas_categoria[categoria] = {"receita_total": 0}
        
        caixas_categoria[categoria]["receita_total"] += reg["receita_total"]
        
        # --- Agrupando por Região ---
        regiao = reg["regiao"]
        if regiao not in caixas_regiao:
            caixas_regiao[regiao] = {"receita_total": 0, "n_vendas": 0}
        
        caixas_regiao[regiao]["receita_total"] += reg["receita_total"]
        caixas_regiao[regiao]["n_vendas"] += 1

    # Transformando Dicts em listas
    # Lista por Mês (ordenada pelo número do mês)
    lista_mes = []
    for m, valores in sorted(caixas_mes.items()):
        lista_mes.append({
            "mes": m,
            "receita_total": round(valores["receita_total"], 2),
            "quantidade": valores["quantidade"],
            "n_vendas": valores["n_vendas"]
        })
    # Lista por Produto (ordenada por maior receita e limitando ao top 5)
    lista_produto = []
    for p, valores in caixas_produto.items():
        lista_produto.append({
            "produto": p, 
            "receita_total": round(valores["receita_total"], 2)
        })
    
    # Ordenando do maior para o menor com base nas receita_total
    lista_produto.sort(key=lambda x: x["receita_total"], reverse=True)
    top_5_produtos = lista_produto[:5]
    # Lista por categoria (ordenada por maior receita)
    lista_categoria = []
    for c, valores in caixas_categoria.items():
        lista_categoria.append({
            "categoria": c, 
            "receita_total": round(valores["receita_total"], 2)
        })
    lista_categoria.sort(key=lambda x: x["receita_total"], reverse=True)
    # Lista por região (com cálculo do Ticket Médio)
    lista_regiao = []
    for r, valores in caixas_regiao.items():
        ticket_medio = valores["receita_total"] / valores["n_vendas"]
        lista_regiao.append({
            "regiao": r, 
            "receita_total": round(valores["receita_total"], 2),
            "ticket_medio": round(ticket_medio, 2)
        })
    lista_regiao.sort(key=lambda x: x["receita_total"], reverse=True)

    # Resumo do dicionário
    metricas = {
        "por_mes": lista_mes,
        "top_produtos": top_5_produtos,
        "por_categoria": lista_categoria,
        "por_regiao": lista_regiao
    }

    return metricas


def segmentar_clientes(registros):
    """
    RF06 - Agrupa a receita total por cliente e classifica o segmento 
    (Bronze, Prata, Ouro) usando uma função lambda.
    """
    
    # Agrupa a receita total por cliente
    total_por_cliente = {}
    for linha in registros:
        nome = linha["cliente"]
        receita = linha["receita_total"]
        
        if nome not in total_por_cliente:
            total_por_cliente[nome] = 0
            
        total_por_cliente[nome] += receita

    # Criando a função lambda de classificação exigida pelo projeto
    # Retorne "Ouro" se total > 15000, senão retorne "Prata" se total >= 5000, senão "Bronze"
    classificar = lambda total: "Ouro" if total > 15000 else ("Prata" if total >= 5000 else "Bronze")
    
    # 3. Construir a lista final já formatada
    lista_clientes = []
    for nome, total in total_por_cliente.items():
        lista_clientes.append({
            "cliente": nome,
            "total_gasto": round(total, 2),
            "segmento": classificar(total) # Aplicando a função lambda aqui!
        })
        
    # 4. Ordenar a lista do cliente que gastou mais para o que gastou menos
    lista_clientes.sort(key=lambda x: x["total_gasto"], reverse=True)
    
    return lista_clientes

def processar_coluna(registros, coluna, funcao_transformacao, nome_saida=None):
    """
    RF07 - Aplica uma função de transformação a um campo específico de cada registro.
    Demonstra o conceito de Função de Ordem Superior (função recebendo função como parâmetro).
    
    Parâmetros:
        registros (list[dict]): Lista de dicionários de dados.
        coluna (str): Nome do campo original a ser processado.
        funcao_transformacao (function): Função (ou lambda) a ser aplicada sobre cada valor.
        nome_saida (str, opcional): Nome da nova coluna gerada. Se omitido, usará '{coluna}_transformado'.
        
    Retorna:
        list[dict]: A lista de registros atualizada com a nova coluna.
    """
    nome_saida = nome_saida or f"{coluna}_transformado"
    for linha in registros:
        linha[nome_saida] = funcao_transformacao(linha[coluna])
    return registros
