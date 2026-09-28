"""
SalesInsight PY — Análise de Dados de Vendas
Ponto de entrada principal do projeto (RF09).
"""

import os
from gerar_sementes import gerar_dataset_vendas
from funcoes_dataset import (
    carregar_dataset,
    inspecionar_dados,
    limpar_dados,
    criar_colunas_derivadas,
    processar_coluna,
    calcular_metricas,
    segmentar_clientes,
    exportar_resultados
)

def main():
    """Executa o pipeline completo do SalesInsight PY."""
    print("=" * 65)
    print("        SALESINSIGHT PY - Análise de Dados de Vendas")
    print("=" * 65)

    caminho_csv = "vendas.csv"

    # Etapa 0: Garantir a existência do arquivo de dados (RF01)
    if not os.path.exists(caminho_csv):
        print("\n[ETAPA 0] Gerando dataset sintético inicial...")
        gerar_dataset_vendas(caminho_csv=caminho_csv, n_registros=200, seed=42)

    # Etapa 1 e 2: Carregar e Inspecionar os dados (RF02)
    print("\n[ETAPA 1 e 2] Carregando e inspecionando dados brutos...")
    registros = carregar_dataset(caminho_csv)
    inspecionar_dados(registros)

    # Etapa 3: Limpeza e Tratamento dos Dados (RF03)
    print("\n[ETAPA 3] Limpando dados com datetime e regex...")
    registros_limpos, relatorio = limpar_dados(registros)

    # Etapa 4: Criar Colunas Derivadas (RF04)
    print("\n[ETAPA 4] Criando colunas derivadas e temporais...")
    registros_limpos = criar_colunas_derivadas(registros_limpos)

    # Etapa 5: Ordem Superior e Lambdas (RF07)
    print("\n[ETAPA 5] Aplicando funções de ordem superior com lambda...")
    registros_limpos = processar_coluna(
        registros_limpos,
        coluna="receita_total",
        funcao_transformacao=lambda x: round(x / 1000, 2),
        nome_saida="receita_em_milhares"
    )
    registros_limpos = processar_coluna(
        registros_limpos,
        coluna="quantidade",
        funcao_transformacao=lambda q: "Alto Volume" if q > 5 else "Baixo Volume",
        nome_saida="perfil_volume"
    )

    # Etapa 6: Métricas Agregadas (RF05)
    print("\n[ETAPA 6] Calculando métricas agregadas...")
    metricas = calcular_metricas(registros_limpos)

    # Etapa 7: Segmentação de Clientes (RF06)
    print("\n[ETAPA 7] Segmentando clientes por faixa de gasto...")
    clientes = segmentar_clientes(registros_limpos)

    # Etapa 8: Exportação de Resultados e Estatísticas (RF08)
    print("\n[ETAPA 8] Exportando resultados em CSV e JSON...")
    receita_geral = sum(r["receita_total"] for r in registros_limpos)
    total_transacoes = len(registros_limpos)
    ticket_medio_geral = receita_geral / total_transacoes
    vendas_acima_media = sum(1 for r in registros_limpos if r["receita_total"] > ticket_medio_geral)

    estatisticas = {
        "receita_total_geral": receita_geral,
        "total_transacoes": total_transacoes,
        "ticket_medio_geral": ticket_medio_geral,
        "vendas_acima_da_media": vendas_acima_media
    }

    exportar_resultados(metricas, clientes, estatisticas)

    print("\n" + "=" * 65)
    print(" [CONCLUÍDO] Fluxo completo executado com sucesso!")
    print("=" * 65)

if __name__ == "__main__":
    main()