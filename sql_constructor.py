def construct_sql_query(data, query_template):
    conditions = ' or\n\t'.join([f"(a.cd_gr_val_concretos = '{value}')" for value in data])
    query = query_template.format(conditions)
    return query

if __name__ == "__main__":
    pass