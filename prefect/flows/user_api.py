import json
import requests
from prefect import task, flow


@task
def get_users(url: str):
    req = requests.get(url=url)
    res = req.json()
    return res


@task
def save_users(users: dict, path: str):
    with open(path, "w") as f:
        json.dump(users, f)


@flow
def deployed_flow():
    URL = "https://gorest.co.in/public/v2/users"
    users = get_users(url=URL)
    save_users(users=users, path="users.json")

# Register deployment from flow via python function. Alternative is CLI.
# def deploy():
#     deployment = Deployment.build_from_flow(
#         flow=deployed_flow,
#         name="prefect-deployment"
#     )
#     deployment.apply()

if __name__ == "__main__":
    # deploy()
    deployed_flow()