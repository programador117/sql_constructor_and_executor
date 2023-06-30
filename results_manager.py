import pandas as pd
from file_manager import read_dataframe_from_excel, read_columns_dict_dataframe, find_files, save_result_to_excel
from utils import rename_dataframe, dataframe_to_dict, drop_dataframe_columns_except, format_date

def merge_results():
    folder_path = 'resultado_consultas'
    excel_files = find_files(folder_path, None, '.xlsx')
    
    merged_results = pd.DataFrame()
    for file_path in excel_files:
        df = read_dataframe_from_excel(file_path)
        merged_results = pd.concat([merged_results, df])
    
    return merged_results

def rename_result_columns(result):
    result_renamed = None
    dict_column_names = None
    new_column_names = None
    
    dict_column_names_dataframe = read_columns_dict_dataframe()
       
    if dict_column_names_dataframe is not None:
        dict_column_names = dataframe_to_dict(dict_column_names_dataframe, "original", "nuevo")
        new_column_names = list(dict_column_names.values())
        result_renamed = rename_dataframe(result, dict_column_names)
        
    
    return result_renamed, new_column_names
    

def merge_results_and_save():
    merged_results = merge_results()
    merged_results_renamed, new_column_names = rename_result_columns(merged_results)
    
    # Dates come in a format different than expected so its necessary to format them.
    merged_results_renamed["FFIN"] = merged_results_renamed["FFIN"].apply(lambda d: format_date(d))
    merged_results_renamed["FINI"] = merged_results_renamed["FINI"].apply(lambda d: format_date(d))
    
    merged_results_filtered = drop_dataframe_columns_except(merged_results_renamed, excepted_columns = new_column_names)
    merged_results_filtered["DESC_COMP"] = "Nada"
    merged_results_filtered["CONCEPTO"] = "Nada"
    save_result_to_excel(merged_results_filtered, "Todos", folder = 'resultado_final_consultas')