import pandas as pd
from pathlib import Path

PROCESSED_PATH = Path("data/processed")
REPORTS_PATH = Path("reports")
REPORTS_PATH.mkdir(exist_ok=True)

def gerar_indicadores():
    corridas = pd.read_csv(PROCESSED_PATH / "corridas.csv", parse_dates=["data"])
    horas = pd.read_csv(PROCESSED_PATH / "horas_trabalhadas.csv", parse_dates=["data"])
    abastecimentos = pd.read_csv(PROCESSED_PATH / "abastecimento.csv", parse_dates=["data"])
    manutencao = pd.read_csv(PROCESSED_PATH / "manutencao.csv", parse_dates=["data"])
    custos_fixos = pd.read_csv(PROCESSED_PATH / "custos_fixos.csv", parse_dates=["mes"])
  
    faturamento = corridas.groupby(corridas["data"].dt.to_period("M"))["valor_corrida"].sum()

    horas_trabalhadas = horas.groupby(horas["data"].dt.to_period("M"))["horas_trabalhadas"].sum()

    ganho_por_hora = faturamento / horas_trabalhadas

    custo_combustivel = abastecimentos.groupby(abastecimentos["data"].dt.to_period("M"))["valor_total"].sum()
    custo_manutencao = manutencao.groupby(manutencao["data"].dt.to_period("M"))["valor"].sum()
    custo_fixo = custos_fixos.groupby(custos_fixos["mes"].dt.to_period("M"))["valor"].sum()

    custos_totais = custo_combustivel + custo_manutencao + custo_fixo

    lucro = faturamento - custos_totais
    indicadores = pd.DataFrame({
        "faturamento": faturamento,
        "horas_trabalhadas": horas_trabalhadas,
        "ganho_por_hora": ganho_por_hora,
        "custo_total": custos_totais,
        "lucro_estimado": lucro
    }).reset_index()

    indicadores.rename(columns={"data": "mes"}, inplace=True)

    indicadores.to_csv(REPORTS_PATH / "indicadores_mensais.csv", index=False)
    print("Indicadores gerados com sucesso.")

    return indicadores


if __name__ == "__main__":
    gerar_indicadores()
