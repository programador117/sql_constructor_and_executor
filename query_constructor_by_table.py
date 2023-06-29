import os

from file_manager import find_files, save_to_file
from data_extractor import extract_data_from_excel
from query_constructor import construct_sql_query

def process_case(file_path):
    case_name = os.path.basename(os.path.dirname(file_path))
    data = extract_data_from_excel(file_path, 'PosFact.relev.contab', 'Gr.val.concr.tarifa', 'X', 3)
    query_template = """
        SELECT * 
        FROM DTMCO_PRO.ED_OWNER.t_ed_p_sap_operandos_compl a 
        LEFT JOIN DTMCO_PRO.ED_OWNER.t_ed_p_sap_operandos_precios b 
        ON a.cd_precio = b.cd_precio
        WHERE 
        {}
    """
    query = construct_sql_query(data, query_template)
    file_path = os.path.join('consultas_resultantes', f'{case_name}.txt')
    save_to_file(file_path, query)

def construct_sql_queries_for_all_cases():
    folder_path = 'casos'
    excel_files = find_files(folder_path, 'documentoCalculo', '.xlsx')
    for file_path in excel_files:
        process_case(file_path)
