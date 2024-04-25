# creation.py
from prefect import flow, task
import duckdb
import os

# 生成示例 CSV 数据
def generate_sample_csv():
    csv_content = """Name,Age,City
Alice,25,New York
Bob,30,Los Angeles
Charlie,22,Chicago
Diana,35,Houston
Evan,28,Phoenix"""
    with open('sample_data.csv', 'w') as f:
        f.write(csv_content)
    return 'sample_data.csv'

# 数据创建
@task
def create_data():
    filepath = generate_sample_csv()
    con = duckdb.connect(database=':memory:')
    data = con.execute(f"SELECT * FROM read_csv_auto('{filepath}')").fetchdf()
    con.close()
    return data

# Flow1 Creation
@flow
def create_data_flow():
    data = create_data()
    return data

if __name__ == "__main__":
    create_data_flow()