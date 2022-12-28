import datetime

API_LINK = "https://api.clockify.me/api/v1/"
SECRET_KEY = "MGFhMjE1ZjItYzJkYS00OWE2LTk2NTctODgyNDhkNjVjNmI5"
SECRET_HEADERS = {"X-Api-Key": SECRET_KEY}


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


def normal_format_to_sec(duration):
    coef = {'S': 1, 'M': 60, 'H': 60 * 60}
    result = 0
    num = ''
    print(duration)
    for i in duration[2:]:

        if i.isnumeric():
            num += i
        else:
            result += int(num) * coef[i]
            num = ''

    return result


def sec_to_normal_format(duration):
    return str(datetime.timedelta(seconds=duration))
