import pandas as pd
from tabulate import tabulate

def carregar_dados(nome_arquivo, campos):
    try:
        df = pd.read_csv(nome_arquivo)
        print("Tabela existente:")
        print(tabulate(df, headers='keys', tablefmt='grid'))
    except FileNotFoundError:
        df = pd.DataFrame(columns=campos)
    return df

def salvar_dados(df):
    if input("Salvar dados? (s/n): ").strip().lower() == 's':
        nome_arquivo = input("Nome do arquivo: ").strip()
        if not nome_arquivo.lower().endswith('.csv'):
            nome_arquivo += '.csv'
        df.to_csv(nome_arquivo, index=False)
        print("Dados salvos!")