import snowflake.connector

def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user='Rohit23',
        password='UVNHehnU2hnDTci',
        account='tvscjko-dq93650',
        warehouse='COMPUTE_WH',
        database='TEST_DB',
        schema='PUBLIC'
    )
    return conn
