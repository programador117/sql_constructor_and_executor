from connection_manager import create_connection, close_connection

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetch_dataframe()
    cursor.close()
    return data
