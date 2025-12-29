from pathlib import Path
import duckdb

DATA_PATH = Path(__file__).parent / "data"


def query_duckdb(sql_code: str, parameters=None):
    with duckdb.connect(DATA_PATH / "movies.duckdb") as conn:
        # if parameters:
        cursor = conn.execute(sql_code, parameters)
        # else:
        #     cursor = conn.execute(sql_code)

        lower = sql_code.strip().lower()
        if lower.startswith(("select", "from", "desc", "pragma")):
            return cursor.df()

