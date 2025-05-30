import pandas as pd
import numpy as np
from InquirerPy import inquirer
from InquirerPy import prompt


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


def download_csv(dados_sem_outliers):
    df = pd.DataFrame(dados_sem_outliers)

    question = {
        "type": "input",
        "name": "file_name",
        "message": "How do you want to name your file (.csv)?"
    }

    file_name_answer = prompt(question)
    file_name = file_name_answer["file_name"]

    # Salva em CSV
    df.to_csv(f"{file_name}.csv", index=False, header=False)


def iqr_method(data_to_clean):
    print("IQR method")
    q1 = np.quantile(data_to_clean, 0.25)
    q3 = np.quantile(data_to_clean, 0.75)
    iqr = q3 - q1
    inferior_limit = q1 - (1.5 * iqr)
    superior_limit = q3 + (1.5 * iqr)
    print("Inferior limit: ", inferior_limit)
    print("Superior limit: ", superior_limit)
    clean_data = data_to_clean[(data_to_clean >= inferior_limit) & (
        data_to_clean <= superior_limit)].copy()

    user_option = inquirer.select(message="Do you want to download the file with no outliers (.csv)?",
                                  choices=[
                                      "Yes",
                                      "No"
                                  ],
                                  default="Yes",
                                  ).execute()
    if (user_option == 'Yes'):
        download_csv(clean_data)

    return


def z_score_method():
    print("...to do")


def mad_method():
    print("...to do")


def proccessing_outliers(csv_path, method):
    df = read_csv(csv_path)
    numerical_columns = df.select_dtypes(include="number").columns

    print("\nNumerical columns avaliable:")
    for i, col in enumerate(numerical_columns, 1):
        print(f"{i} - {col}")
    escolha = int(input("\nType column number you want to analyse: "))
    chosen_column = numerical_columns[escolha - 1]
    column = df[chosen_column]
    data = column.to_numpy()

    method_map = {
        "1 - IQR (Intervalo Interquartil)": iqr_method,
        "2 - Z-Score": z_score_method,
        "3 - Mad (Desvio Absoluto da Mediana)": mad_method
    }

    method_function = method_map.get(method)
    if method_function:
        method_function(data)
    else:
        print("Invalid Method!")
