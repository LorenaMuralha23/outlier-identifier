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


def iqr_method():
    print("IQR method")


def z_score_method():
    print("...to do")


def mad_method():
    print("...to do")


method_map = {
    "1 - IQR (Intervalo Interquartil)": iqr_method,
    "2 - Z-Score": z_score_method,
    "3 - Mad (Desvio Absoluto da Mediana)": mad_method
}


def proccessing_outliers(csv_path, method):
    method_map.get(method, lambda: print("Método inválido"))()
