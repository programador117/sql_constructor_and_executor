import time, os

from file_manager import find_files, read_from_file, save_result_to_excel, read_connection_data
from connection_manager import create_connection, close_connection
from query_executor import execute_query

def execute_sql_queries_for_all_cases():
    connection_data = read_connection_data('datos_conexion.txt')
    conn = create_connection(connection_data)
    
    folder_path = 'consultas_resultantes'
    txt_files = find_files(folder_path, None, '.txt')
    for file_path in txt_files:
        case_name = os.path.basename(file_path)[:-4]
        
        start_time = time.time()
        query = read_from_file(file_path)
        data = execute_query(conn, query)
        end_time = time.time()
        total_time = end_time - start_time
        
        print(f"Consulta {case_name} terminada en {int(total_time/60)}:{total_time%60:.2f}")
        
        save_result_to_excel(data, case_name)
    
    close_connection(conn)


if __name__ == "__main__":
    pass