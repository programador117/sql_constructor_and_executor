import os
import pandas as pd

def find_files(folder_path, file_name, file_extension):
    files = []
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            for file in os.listdir(subfolder_path):
                if file_name in file and file.endswith(file_extension):
                    file_path = os.path.join(subfolder_path, file)
                    files.append(file_path)
    return files

def read_from_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

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