import pandas as pd
from extract import extract_all
from pathlib import Path

PROCESSED_PATH = Path("data/processed")
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

def tratar_corridas(df):
    df["data"] = pd.to_datetime(df["data"])
    df["horario"] = pd.to_datetime(df["horario"], format="%H:%M").dt.time
    df["valor_corrida"] = pd.to_numeric(df["valor_corrida"])
    df["km_rodado"] = pd.to_numeric(df["km_rodado"])
    return df

def tratar_horas_trabalhadas(df):
    df["data"] = pd.to_datetime(df["data"])
    df["hora_inicio"] = pd.to_datetime(df["hora_inicio"], format="%H:%M")
    df["hora_fim"] = pd.to_datetime(df["hora_fim"], format="%H:%M")

    df["horas_trabalhadas"] = (
        (df["hora_fim"] - df["hora_inicio"])
        .dt.total_seconds() / 3600
    )
    return df

def tratar_abastecimento(df):
    df["data"] = pd.to_datetime(df["data"])
    df["litros"] = pd.to_numeric(df["litros"])
    df["valor_total"] = pd.to_numeric(df["valor_total"])
    df["km_veiculo"] = pd.to_numeric(df["km_veiculo"], errors="coerce")
    return df

def tratar_manutencao(df):
    df["data"] = pd.to_datetime(df["data"])
    df["valor"] = pd.to_numeric(df["valor"])
    return df

def tratar_custos_fixos(df):
    df["mes"] = pd.to_datetime(df["mes"], format="%Y-%m")
    df["valor"] = pd.to_numeric(df["valor"])
    return df

def transform_all():
    data = extract_all()

    tratados = {
        "corridas": tratar_corridas(data["corridas"]),
        "horas_trabalhadas": tratar_horas_trabalhadas(data["horas_trabalhadas"]),
        "abastecimento": tratar_abastecimento(data["abastecimento"]),
        "manutencao": tratar_manutencao(data["manutencao"]),
        "custos_fixos": tratar_custos_fixos(data["custos_fixos"])
    }

    for nome, df in tratados.items():
        output = PROCESSED_PATH / f"{nome}.csv"
        df.to_csv(output, index=False)
        print(f"{nome} tratado e salvo em {output}")

    print("Tratamento concluído com sucesso.")
    return tratados

if __name__ == "__main__":
    transform_all()
