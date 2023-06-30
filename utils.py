from datetime import datetime

def rename_dataframe(dataframe, dict_names):
    renamed_dataframe = dataframe.rename(columns=dict_names)
    return renamed_dataframe

def dataframe_to_dict(dataframe, key_column, value_column):
    dict_dataframe = dataframe.set_index(key_column)[value_column].to_dict()
    return dict_dataframe

def drop_dataframe_columns_except(dataframe, excepted_columns):
    columns_to_drop = dataframe.columns.difference(excepted_columns)
    return __drop_dataframe_columns(dataframe, columns_to_drop)

def __drop_dataframe_columns(dataframe, columns):
    return dataframe.drop(columns, axis=1)

def format_date(date):
    date_result = None
    if date is not None:
        if isinstance(date, datetime):
            date_result = date.strftime("%Y%m%d")
        else:
            raise ValueError("Formato de Fecha no es correcto. Se espera datetime.Datetime")
    return date_result