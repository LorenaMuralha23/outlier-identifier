import pandas as pd


def read_csv(file_name):
    try:
        df = pd.read_csv(file_name, encoding='utf-8')
        return df
    except FileNotFoundError:
        print(f"Erro: File '{file_name}' was not found.")
        return None
    except Exception as e:
        print(f"An error ocurred: {e}")
        return None
