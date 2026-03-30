import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw")

SCHEMAS = {
    "corridas.csv": ["data", "horario", "valor_corrida", "km_rodado"],
    "horas_trabalhadas.csv": ["data", "hora_inicio", "hora_fim"],
    "abastecimento.csv": ["data", "litros", "valor_total", "km_veiculo"],
    "manutencao.csv": ["data", "tipo_manutencao", "valor"],
    "custos_fixos.csv": ["mes", "descricao", "valor"]
}

def load_csv(file_name):
    file_path = DATA_PATH / file_name
    
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_name}")
    
    df = pd.read_csv(file_path)
    
    expected_cols = SCHEMAS[file_name]
    missing_cols = set(expected_cols) - set(df.columns)
    
    if missing_cols:
        raise ValueError(
            f"Colunas ausentes em {file_name}: {missing_cols}"
        )
    
    return df


def extract_all():
    dataframes = {}
    
    for file_name in SCHEMAS.keys():
        print(f"Extraindo {file_name}...")
        df = load_csv(file_name)
        dataframes[file_name.replace(".csv", "")] = df
    
    print("Extração concluída com sucesso.")
    return dataframes


if __name__ == "__main__":
    extract_all()
