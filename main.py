from query_constructor_by_table import construct_sql_queries_for_all_cases
from all_queries_executor import execute_sql_queries_for_all_cases
from results_manager import merge_results_and_save

if __name__ == '__main__':
    construct_sql_queries_for_all_cases()
    execute_sql_queries_for_all_cases()
    merge_results_and_save()
