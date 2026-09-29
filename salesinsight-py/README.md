# SalesInsight PY — Análise de Dados de Vendas

Mini-Projeto Avaliativo do **Módulo 01 (Fundamentos de Dados, Programação e Análise Preditiva com Python)** do curso **Desenvolvedor(a) em IA para Análise Preditiva [T4] — SENAI / Lab 365**.

---

## 📌 Sobre o Projeto

O **SalesInsight PY** é uma solução completa de engenharia e análise exploratória de dados de vendas desenvolvida **exclusivamente com a biblioteca padrão do Python** (sem dependências externas como Pandas ou NumPy), consolidando os conhecimentos de lógica, estruturas de dados, funções, expressões regulares, manipulação de arquivos e modularização adquiridos entre as Semanas 01 e 05.

O pipeline carrega registros brutos de transações, inspeciona e valida a consistência estrutural, trata dados ausentes e inconsistentes, cria variáveis temporais e categóricas derivadas, calcula métricas agregadas multidimensionais, segmenta clientes por faixa de gasto com funções de ordem superior e exporta relatórios analíticos em **CSV** e **JSON**.

---

## 🎯 O que o Projeto Analisa

- **Volume e Faturamento Temporal:** Receita total, quantidade de itens comercializados e contagem de transações agrupadas por mês, trimestre e ano.
- **Performance de Produtos:** Identificação e ordenação decrescente do *Top 5 produtos* com maior geração de receita.
- **Distribuição por Categoria:** Volume financeiro transacionado por categoria de produtos.
- **Desempenho Regional e Ticket Médio:** Receita total e ticket médio de vendas desagregados por região geográfica.
- **Segmentação de Clientes (RFM simplificado):** Classificação automática da carteira em categorias **Bronze**, **Prata** e **Ouro** através de regras de corte aplicadas via função `lambda`.
- **Estatísticas Gerais de Negócio:** Cálculo de faturamento global, ticket médio geral e quantificação de vendas com valor individual superior à média do período.

---

## 🧠 Conceitos Aplicados (Módulo 01 — Semanas 01 a 05)

- **Lógica e Controle de Fluxo (S03):** Operadores aritméticos, lógicos e de comparação; estruturas condicionais encadeadas (`if / elif / else`) para faixas de valor e trimestres; laços de repetição (`for`).
- **Estruturas de Dados Compostas (S04):** Listas, tuplas, dicionários aninhados para agrupamento (`groupby` nativo) e conjuntos (`set`).
- **Modularização e Funções (S05):** Separação de responsabilidades em módulos (`funcoes_dataset.py`, `gerar_sementes.py`, `salesinsight.py`), funções com parâmetros, retorno e *docstrings*.
- **Funções de Ordem Superior e Lambdas (S05):** Implementação da Higher-Order Function `processar_coluna()` recebendo transformações dinâmicas via expressões `lambda` em múltiplos contextos.
- **Tratamento de Strings e Regex (S05):** Higienização de textos com `.strip()`, remoção de ruídos com `re.sub()` e validação de padrões de identificação de clientes com `re.compile()`.
- **Datas com Datetime (S05):** Conversão de datas textuais via `strptime`, descarte de entradas corrompidas e extração direta de atributos (`month`, `year`).
- **Persistência de Arquivos (S05):** Leitura de CSVs com `csv.DictReader`, gravação formatada com `csv.DictWriter`, serialização estruturada com `json.dump()` e conferência por desserialização com `json.load()`.
- **Boas Práticas de Engenharia de Software:** GitFlow simplificado (`main`, `develop`, `feat/...`), commits atômicos descritivos e gestão visual com Kanban.

---

## 📁 Estrutura do Repositório

```text
salesinsight-py/
│
├── salesinsight.py              # Ponto de entrada e orquestrador do fluxo (main)
├── salesinsight.ipynb           # Notebook interativo de desenvolvimento e exploração
├── funcoes_dataset.py           # Módulo com todas as funções de tratamento e análise
├── gerar_sementes.py            # Gerador de massa de dados sintética com ruídos
├── vendas.csv                   # Dataset de transações (gerado automaticamente se ausente)
├── README.md                    # Documentação técnica e guia do projeto
│
├── outputs/                     # Resultados e relatórios gerados pelo pipeline
│   ├── metricas_por_mes.csv     # Agregação de receita, quantidade e volume mensal
│   ├── segmentacao_clientes.csv # Carteira de clientes classificada por segmento
│   └── estatisticas_gerais.json # Indicadores globais consolidados
│
└── planejamento/                # Gestão e especificações do projeto
    └── tarefas-kanban.md        # Quadro Kanban de rastreabilidade de requisitos
```

---

## ⚙️ Decisões Técnicas

1. **Uso de Dicionários para Agregação em O(n):** Em vez de iterar repetidamente sobre toda a lista de registros para cada filtro ou mês, utilizou-se dicionários como tabelas de acumulação (*hash maps*). Essa abordagem permite processar o dataset inteiro em uma única passagem, garantindo complexidade de tempo linear e alta eficiência de memória.
2. **Descarte Crítico vs. Preservação:** Registros com datas sintaticamente inválidas ou sem quantidade/preço foram descartados no processo de limpeza, pois impossibilitariam cálculos matemáticos consistentes de receita. Por outro lado, clientes com formatação fora do padrão tiveram apenas os caracteres especiais removidos via Expressões Regulares (`re.sub`), preservando o histórico de compra do cliente.
3. **Encoding `utf-8-sig` nos Arquivos CSV:** A escrita dos relatórios CSV foi configurada com codificação `utf-8-sig` (Byte Order Mark), garantindo que acentuações e caracteres especiais da língua portuguesa sejam abertos diretamente no Microsoft Excel sem corrupção de caracteres.
4. **Função de Ordem Superior (`processar_coluna`):** A implementação da função de ordem superior desacoplou a mecânica de iteração sobre as linhas da regra de transformação de negócio, permitindo que novas regras (como conversão de escala ou perfis de volume) sejam plugadas sob demanda via funções `lambda`.

---

## 🚀 Como Executar o Projeto

Como o projeto utiliza **apenas a biblioteca padrão do Python**, não é necessária a instalação de bibliotecas externas (sem necessidade de `pip install`).

### Pré-requisitos
- Python 3.10 ou superior instalado.

### Opção 1: Linha de Comando / Terminal (Recomendado)
Execute o script principal diretamente a partir da raiz do projeto:

```bash
python salesinsight.py
```

O script garantirá a existência do arquivo `vendas.csv`, executará todas as etapas de limpeza, cálculo e exportará automaticamente os relatórios para a pasta `outputs/`.

### Opção 2: Jupyter Notebook / VS Code
Abra o arquivo [`salesinsight.ipynb`](salesinsight.ipynb) no VS Code ou Jupyter Lab e execute as células sequencialmente para visualizar as saídas formatadas, tabelas e inspeções passo a passo.

### Opção 3: Google Colab
1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Faça o upload dos arquivos `salesinsight.py`, `funcoes_dataset.py` e `gerar_sementes.py`.
3. Em uma célula, execute:
   ```python
   !python salesinsight.py
   ```

---

## 📊 Resultados e Indicadores Gerados

Ao término da execução do fluxo completo, o arquivo [`outputs/estatisticas_gerais.json`](outputs/estatisticas_gerais.json) consolida os indicadores macro da operação:

- **Receita Total Geral:** R$ 1.290.346,30
- **Total de Transações Válidas:** 183 vendas
- **Ticket Médio por Transação:** R$ 7.051,07
- **Vendas com Receita Acima da Média:** 70 transações

Os detalhamentos completos podem ser consultados nos arquivos [`outputs/metricas_por_mes.csv`](outputs/metricas_por_mes.csv) e [`outputs/segmentacao_clientes.csv`](outputs/segmentacao_clientes.csv).

---

## 🎥 Vídeo de Demonstração

- **Link da Apresentação:** `https://drive.google.com/drive/folders/1H4hhB2p70rcg1VQhiiiC2mWMaPXKSVoC?usp=sharing`
- *Duração máxima:* 5 minutos
- *Conteúdo:* Apresentação dos objetivos, demonstração do código em execução no terminal/notebook, justificativa das decisões técnicas e boas práticas de versionamento.

---

## 👨‍💻 Autor / Squad

- **Desenvolvedor:** Maurício Sales
- **Curso:** Desenvolvimento de IA para Análise Preditiva [T4]
- **Instituição:** SENAI / Lab 365
