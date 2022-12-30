API_LINK = "https://api.clockify.me/api/v1/"
with open('secret') as file:
    SECRET_KEY = file.readline()
SECRET_HEADERS = {"X-Api-Key": SECRET_KEY}