# archive.py
from prefect import flow, task
import duckdb
import os

@task
def load_data(filepath):
    con = duckdb.connect(database=':memory:')
    con.execute(f"CREATE TABLE dataframe AS SELECT * FROM read_csv_auto('{filepath}')")
    print("Data loaded into DuckDB.")
    return con  # 返回连接以复用

@task
def archive_data(con, archive_path='sample_archive.parquet'):
    # 聚合数据并创建一个新的视图
    con.execute("""
        CREATE VIEW city_counts AS
        SELECT City, COUNT(*) AS Count
        FROM dataframe
        GROUP BY City;
    """)
    
    # 将视图导出为 Parquet 文件
    con.execute(f"COPY city_counts TO '{archive_path}' (FORMAT 'parquet')")
    con.close()
    print(f"Data archived at {archive_path}")

@task
def delete_data(filepath):
    os.remove(filepath)
    print(f"Deleted original data from {filepath}")

@flow
def clean_up_data_flow(filepath):
    con = load_data(filepath)
    archive_data(con, 'sample_archive.parquet')
    delete_data(filepath)

if __name__ == "__main__":
    clean_up_data_flow('sample_data.csv')
