<h1 align="center"> Pipeline de Dados para Apoio à Tomada de Decisão de Motoristas de Aplicativo </h1>

# Índice

- [Título](#Título)
- [Índice](#índice)
- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Indicadores Gerados](#indicadores-gerados)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)

# Descrição do Projeto

Este projeto acadêmico tem como objetivo o desenvolvimento de um pipeline de dados automatizado para apoiar a tomada de decisão de pequenos empreendedores, com foco em motoristas de aplicativo.

A solução permite coletar, tratar, consolidar e analisar dados operacionais fornecidos pelo próprio motorista, transformando registros simples em indicadores financeiros e operacionais que auxiliam na gestão do negócio.

O projeto foi desenvolvido no contexto da disciplina Projeto de Extensão II, do curso de Engenharia de Software.

# Funcionalidades

- Importação de dados financeiros a partir de arquivos CSV
- Validação automática de campos obrigatórios
- Tratamento e normalização dos dados
- Consolidação mensal de receitas e custos
- Cálculo de indicadores financeiros e operacionais
- Geração de relatórios para apoio à tomada de decisão


# Indicadores Gerados

* Faturamento mensal
* Total de horas trabalhadas
* Ganho médio por hora (R$/h)
* Custos totais (combustível, manutenção e fixos)
* Lucro estimado mensal

Esses indicadores permitem ao motorista avaliar a viabilidade econômica da atividade e identificar oportunidades de melhoria.


# Como Executar o Projeto

1. Clone o repositório

```bash
git clone [https://github.com/sophiavantil/pipeline-motoristas-app.git](https://github.com/sophiavantil/pipeline_motorista.git)
```

2. Instale as dependências

```bash
pip install -r requirements.txt
```

3. Execute as etapas do pipeline

```bash
python scr/extract.py
python scr/transform.py
python scr/indicators.py
```

4. Consulte o relatório gerado em:

```
/reports/indicadores_mensais.csv
```


# Tecnologias Utilizadas

- **Python**
- **Bibliotecas**: **Pandas** e **Pathlib**
- Formato dos dados: **CSV**

<img width="48" height="48" src="https://img.icons8.com/color/48/python--v1.png" alt="python--v1"/> <img width="48" height="48" src="https://img.icons8.com/color/48/pandas.png" alt="pandas"/>  <img width="48" height="48" src="https://img.icons8.com/office/40/csv.png" alt="csv"/>





