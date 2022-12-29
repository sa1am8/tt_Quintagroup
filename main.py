import requests
from additional import *


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




if __name__ == "__main__":
    workspace_info = get_workspaces_info()
    total_time = 0
    date = dict()

    for workspace in workspace_info:
        workspace_id = workspace.get('id')
        projects_info = get_projects_info(workspace_id)

        users = get_users(workspace_id)
        for user in users:
            user_id = user.get('id')
            time_entries = get_time_entries(workspace_id, user_id)

            for time_entry in time_entries:

                start = time_entry.get('timeInterval').get('start').split("T")[0]
                duration = time_entry.get('timeInterval').get('duration')

                if not duration:
                    continue

                if start not in date:
                    date[start] = normal_format_to_sec(duration)
                else:
                    date[start] += normal_format_to_sec(duration)


        for project in projects_info:
            project_id = project.get('id')
            tasks_info = get_tasks_info(workspace_id, project_id)

            for task in tasks_info:
                task_id = task.get('id')
                task_info = get_task_info(workspace_id, project_id, task_id)
                total_time += normal_format_to_sec(task_info.get('duration'))
                print('\n')

                for i in task_info:
                    print(f'{i} - {task_info[i]}')

    print()
    print('Total time duration: ', sec_to_normal_format(total_time))
    print()
    for i in date:
        print(f'{i} - {sec_to_normal_format(date[i])}')
