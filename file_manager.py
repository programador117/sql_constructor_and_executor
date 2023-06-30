import os
import pandas as pd

def find_files(folder_path, file_name, file_extension):
    files = []
    if file_name is not None:
        for subfolder in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder)
            if os.path.isdir(subfolder_path):
                for file in os.listdir(subfolder_path):
                    if file_name in file and file.endswith(file_extension):
                        file_path = os.path.join(subfolder_path, file)
                        files.append(file_path)
    else:
        for subfolder in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder)
            if os.path.isdir(subfolder_path):
                for file in os.listdir(subfolder_path):
                    if file.endswith(file_extension):
                        file_path = os.path.join(subfolder_path, file)
                        files.append(file_path)
            else:
                file = subfolder_path
                if file.endswith(file_extension):
                    file_path = file
                    files.append(file_path)
    return files

def read_from_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def read_dataframe_from_excel(file_path):
    content = pd.read_excel(file_path, header = 0)
    return content

def read_columns_dict_dataframe():
    dict_column_names_dataframe = None
    
    folder_path = 'diccionario_conversion_columnas'
    column_names_files = find_files(folder_path, None, '.xlsx')
    column_names_file = column_names_files[0] if column_names_files is not None and len (column_names_files) > 0 else None
    
    if column_names_file is not None:
        dict_column_names_dataframe = read_dataframe_from_excel(column_names_file)
    
    return dict_column_names_dataframe

def read_connection_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return {
        'host': data[0],
        'database': data[1],
        'user': data[2],
        'password': data[3]
    }

def save_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def save_result_to_excel(data, case_name):
    file_path = os.path.join('resultado_consultas', f'F130_{case_name}.xlsx')
    data.to_excel(file_path, index=False)