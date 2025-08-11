import pandas as pd

def pode_adicionar(df, nome):
    try:
        if (df['Nome'] == nome).any():
            print("Atenção: Nome já existe na tabela!")
            continuar = input("Deseja adicionar mesmo assim? (s/n): ").strip().lower()
            if continuar != 's':
                print("Entrada descartada.")
                return False
        return True
    except KeyError:
        return True

def entrada_valida(campo):
    while True:
        valor = input(f"{campo}? ").strip()
        if not valor:
            print(f"{campo} não pode ser vazio.")
        else:
            return valor