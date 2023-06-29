import pandas as pd

def extract_data_from_excel(file_path, column1, column2, value1, value2):
    df = pd.read_excel(file_path)
    data = df.loc[df[column1] == value1, column2]
    data = data[data.str.len() == value2].unique()
    return data
