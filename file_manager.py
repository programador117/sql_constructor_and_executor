import os

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

def save_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
