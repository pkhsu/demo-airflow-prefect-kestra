# usage.py
from prefect import flow, task
import duckdb

@task
def load_and_store_data(filepath):
    con = duckdb.connect(database=':memory:')
    # 直接加载 CSV 文件到内存数据库
    con.execute(f"CREATE TABLE dataframe AS SELECT * FROM read_csv_auto('{filepath}')")
    print("Data loaded and stored in memory...")
    con.close()
    return filepath  # 返回文件路径用于后续处理

@task
def process_data(filepath):
    con = duckdb.connect(database=':memory:')
    # 重新加载数据，因为上一步关闭了连接
    con.execute(f"CREATE TABLE dataframe AS SELECT * FROM read_csv_auto('{filepath}')")
    
    # 添加一个额外的字段 "AgeGroup"
    con.execute("""
        ALTER TABLE dataframe ADD AgeGroup VARCHAR;
        UPDATE dataframe SET AgeGroup = CASE 
            WHEN Age < 25 THEN 'Youth'
            WHEN Age BETWEEN 25 AND 59 THEN 'Adult'
            ELSE 'Senior'
        END;
    """)
    
    # 选择更新后的数据，并计算行数
    processed_data = con.execute("SELECT *, COUNT(*) OVER () AS TotalRows FROM dataframe").fetchdf()
    con.close()
    return processed_data

@flow
def use_data_flow(filepath):
    file_path = load_and_store_data(filepath)
    processed_data = process_data(file_path)
    print("Data Stored and Processed")
    # 打印处理后的数据
    print(processed_data)
    return processed_data

if __name__ == "__main__":
    # 调用流程，直接传递文件路径
    use_data_flow('sample_data.csv')
