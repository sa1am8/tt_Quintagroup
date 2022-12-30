import requests
from utils import *


class Projects:
    def get_projects_info(self):
        link = get_projects_link(self.workspace_id)
        r = requests.get(link, headers=SECRET_HEADERS)
        return r.json()

    def get_tasks_info(self, project_id: str) -> dict:
        link = get_tasks_link(self.workspace_id, project_id)
        r = requests.get(link, headers=SECRET_HEADERS)
        return r.json()

    def __init__(self, workspace_id):
        self.workspace_id = workspace_id


class Users:
    def get_users(self):
        link = get_users_link(self.workspace_id)
        r = requests.get(link, headers=SECRET_HEADERS)
        return r.json()

    def __init__(self, workspace_id):
        self.workspace_id = workspace_id


class TimeEntries:
    def get_time_entries(workspace_id, user_id):
        link = get_time_entries_link(workspace_id, user_id)
        r = requests.get(link, headers=SECRET_HEADERS)
        return r.json()

    def __init__(self, workspace_id):
        self.workspace_id = workspace_id
