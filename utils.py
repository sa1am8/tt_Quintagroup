import requests
import datetime
from config import *

def get_workspaces_link():
    return API_LINK + "/workspaces/"


def get_tasks_link(workspace_id, project_id):
    return API_LINK + f"/workspaces/{workspace_id}/projects/{project_id}/tasks"


def get_task_link(workspace_id, project_id, task_id):
    return API_LINK + f"/workspaces/{workspace_id}/projects/{project_id}/tasks/{task_id}"


def get_projects_link(workspace_id):
    return API_LINK + f"/workspaces/{workspace_id}/projects"


def get_project_link(workspace_id, project_id):
    return API_LINK + f"/workspaces/{workspace_id}/projects/{project_id}"

def get_users_link(workspace_id):
    return API_LINK + f"/workspaces/{workspace_id}/users"

def get_time_entries_link(workspace_id, user_id):
    return API_LINK + f"/workspaces/{workspace_id}/user/{user_id}/time-entries"



def normal_format_to_sec(duration: str) -> int:

    """Gained str in format PT1H1M7S converting to seconds"""

    coef = {'S': 1, 'M': 60, 'H': 60 * 60}
    result = 0
    num = ''

    for i in duration[2:]:

        if i.isnumeric():
            num += i
        else:
            result += int(num) * coef[i]
            num = ''

    return result


def sec_to_normal_format(duration):
    return str(datetime.timedelta(seconds=duration))


def get_workspaces_info():
    link = get_workspaces_link()
    r = requests.get(link, headers=SECRET_HEADERS)
    return r.json()


def get_projects_info(workspace_id: str) -> dict:
    link = get_projects_link(workspace_id)
    r = requests.get(link, headers=SECRET_HEADERS)
    return r.json()


def get_project_info(workspace_id: str, project_id: str) -> dict:
    link = get_project_link(workspace_id, project_id)
    r = requests.get(link, headers=SECRET_HEADERS)
    return r.json()


def get_tasks_info(workspace_id: str, project_id: str) -> dict:
    link = get_tasks_link(workspace_id, project_id)
    r = requests.get(link, headers=SECRET_HEADERS)
    return r.json()


def get_task_info(workspace_id: str, project_id: str, task_id) -> dict:
    link = get_task_link(workspace_id, project_id, task_id)
    r = requests.get(link, headers=SECRET_HEADERS)
    return r.json()


def get_users(workspace_id):
    link = get_users_link(workspace_id)
    r = requests.get(link, headers=SECRET_HEADERS)
    return r.json()


def get_time_entries(workspace_id, user_id):
    link = get_time_entries_link(workspace_id, user_id)
    r = requests.get(link, headers=SECRET_HEADERS)
    return r.json()

