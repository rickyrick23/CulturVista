import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
from snowflake_connection import get_snowflake_connection

def load_cultural_sites():
    # Load the CSV
    df = pd.read_csv("data/cultural_tourism_sites.csv")

    # Connect to Snowflake
    conn = get_snowflake_connection()

    # Write to Snowflake
    success, nchunks, nrows, _ = write_pandas(
        conn,
        df,
        table_name='CULTURAL_SITES',
        auto_create_table=True
    )

    print(f"Upload success: {success}, rows uploaded: {nrows}")
