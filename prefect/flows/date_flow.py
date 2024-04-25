from datetime import datetime
from prefect import task, flow


@task
def get_datetime():
    return datetime.now()

@flow(name="Date Flow")
def my_flow():
    date = get_datetime()
    print(date)
    return date

if __name__ == "__main__":
    my_flow()