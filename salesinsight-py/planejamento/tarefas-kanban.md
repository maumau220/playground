# Quadro Kanban — SalesInsight PY

Quadro de gestão visual das tarefas do **Mini-Projeto Avaliativo (Módulo 1 - Semana 08)** do curso **Desenvolvedor(a) em IA para Análise Preditiva [T4] - SENAI / Lab 365**.

---

## 📌 Colunas do Kanban

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   📋 A Fazer    │ ──> │ ⏳ Em Andamento │ ──> │   🔍 Em Teste   │ ──> │  ✅ Concluído   │
│    (Backlog)    │     │   (In Progress) │     │    (Review)     │     │     (Done)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## 📋 Backlog / A Fazer

*(Nenhuma tarefa pendente no backlog.)*

---

## ⏳ Em Andamento

*(Nenhuma tarefa em andamento. Todas as etapas concluídas!)*

---

## 🔍 Em Teste / Revisão

*(Nenhuma tarefa em teste.)*

---

## ✅ Concluído

- [x] **TASK-01** — Configuração Inicial do Ambiente e Repositório Git (S01 / S04)
  - *Entregável:* Estrutura de pastas (`outputs/`, `planejamento/`), arquivo `.gitignore` e configuração inicial do repositório.

- [x] **TASK-02** — Criação do Gerador de Sementes Sintéticas (RF01 - S05)
  - *Entregável:* Arquivo `gerar_sementes.py` com a função `gerar_dataset_vendas()` gerando `vendas.csv` com dados sujos propositais.

- [x] **TASK-03** — Inspeção Estrutural dos Dados Brutos (RF02 - S05)
  - *Entregável:* Funções `carregar_dataset()` e `inspecionar_dados()` em `funcoes_dataset.py`, exibindo total de registros, colunas e contagem de nulos.

- [x] **TASK-04** — Limpeza e Tratamento com Datetime e Regex (RF03 - S05)
  - *Entregável:* Função `limpar_dados()` em `funcoes_dataset.py` tratando espaços (`.strip()`), conversão de datas com `datetime.strptime`, remoção de nulos críticos, ajuste de tipos numéricos e padronização com `re.sub`/`re.compile`. Relatório de limpeza exibido com sucesso.

- [x] **TASK-05** — Criação de Colunas Derivadas e Transformações Condicionais (RF04 - S03 / S05)
  - *Entregável:* Função `criar_colunas_derivadas()` adicionando `receita_total`, `mes`, `mes_nome`, `trimestre`, `ano` e `faixa_receita_item`.

- [x] **TASK-06** — Cálculo de Métricas Agregadas (RF05 - S04 / S05)
  - *Entregável:* Função `calcular_metricas()` com dicionários de acumulação gerando agregações mensais, Top 5 produtos ordenados decrescentemente, receita por categoria e por região com ticket médio.

- [x] **TASK-07** — Segmentação de Clientes por Faixa de Gasto (RF06 - S04 / S05)
  - *Entregável:* Função `segmentar_clientes()` agrupando faturamento por cliente e classificando em Bronze/Prata/Ouro utilizando função `lambda`.

- [x] **TASK-08** — Modularização e Função de Ordem Superior (RF07 - S05)
  - *Entregável:* Função `processar_coluna()` como Higher-Order Function aplicada com lambdas em dois contextos distintos (`receita_em_milhares` e `perfil_volume`).

- [x] **TASK-09** — Exportação de Resultados em CSV e JSON (RF08 - S05)
  - *Entregável:* Função `exportar_resultados()` gerando `outputs/metricas_por_mes.csv`, `outputs/segmentacao_clientes.csv` e `outputs/estatisticas_gerais.json`, com releitura de validação via `json.load()`.

- [x] **TASK-10** — Ponto de Entrada e Fluxo Principal `main()` (RF09 - S05)
  - *Entregável:* Orquestrador completo no arquivo `salesinsight.py` com ponto de entrada `if __name__ == "__main__":` e execução sequencial sem erros.

- [x] **TASK-11** — Elaboração da Documentação Técnica (README.md - S04 / S05)
  - *Entregável:* Arquivo `README.md` completo com apresentação do projeto, decisões técnicas, arquitetura, instruções de execução e resultados consolidados.

- [x] **TASK-12** — Gravação e Publicação do Vídeo de Demonstração (S08)
  - *Entregável:* Roteiro de apresentação gravado e link inserido na documentação principal do repositório.

- [x] **TASK-13** — Checklist Final, Versionamento Git e Submissão no AVA (S08)
  - *Entregável:* Repositório validado, versionado via GitFlow e submetido para avaliação.

---

## 📊 Matriz de Rastreabilidade (Requisitos x Tarefas)

| Requisito | Descrição | Tarefa Kanban | Status |
| :--- | :--- | :--- | :---: |
| **RF01** | Criar ou Carregar Dataset de Vendas | TASK-02 | ✅ Concluído |
| **RF02** | Inspecionar e Descrever Dados | TASK-03 | ✅ Concluído |
| **RF03** | Limpar e Tratar Dados (`datetime` e `re`) | TASK-04 | ✅ Concluído |
| **RF04** | Criar Colunas Derivadas e Condicionais | TASK-05 | ✅ Concluído |
| **RF05** | Calcular Métricas Agregadas (`groupby` nativo) | TASK-06 | ✅ Concluído |
| **RF06** | Segmentar Clientes com Função `lambda` | TASK-07 | ✅ Concluído |
| **RF07** | Modularização e Função de Ordem Superior | TASK-08 | ✅ Concluído |
| **RF08** | Exportar Resultados em CSV e JSON | TASK-09 | ✅ Concluído |
| **RF09** | Ponto de Entrada e Fluxo Completo `main()` | TASK-10 | ✅ Concluído |
| **DOCS** | Documentação Técnica (`README.md`) | TASK-11 | ✅ Concluído |
| **VIDEO** | Gravação do Vídeo de Apresentação (5 min) | TASK-12 | ✅ Concluído |
| **FINAL** | Versionamento Git, Checklist e Submissão AVA | TASK-01 / TASK-13 | ✅ Concluído |
