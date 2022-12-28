import requests

API_LINK = "https://api.clockify.me/api/v1/"
SECRET_KEY = "MGFhMjE1ZjItYzJkYS00OWE2LTk2NTctODgyNDhkNjVjNmI5"
WORKSPACES_LINK = API_LINK + "workspaces"

if __name__ == "__main__":

    r = requests.get(WORKSPACES_LINK, headers={"X-Api-Key": SECRET_KEY})
    print(r.text)
