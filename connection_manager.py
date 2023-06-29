import redshift_connector

def create_connection(connection_data):
    conn = redshift_connector.connect(
        host=connection_data['host'],
        database=connection_data['database'],
        user=connection_data['user'],
        password=connection_data['password']
    )
    return conn

def close_connection(conn):
    conn.close()