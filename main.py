import requests
import datetime as dt

today = str(dt.date.today())
today_split = today.split("-")
today_join = f"{today_split[0]}{today_split[1]}{today_split[2]}"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USERNAME = "xxxxxxxxxxxxxxx"
TOKEN = "xxxxxxxxxxxxxxxx"

params_pixela = {
    f"token" :{TOKEN},
    f"username" :{USERNAME},
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# creating the account
# response_pixela = requests.post(url=PIXELA_ENDPOINT, json=params_pixela)
# print(response_pixela.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_params = {
    "id" : "graph1",
    "name" : "Minutes of coding",
    "unit" : "m",
    "type" : "int",
    "color" : "kuro"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
# response_graph_pixela = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# updating my pixela
# asking how many minutes do i code
time_coding = input("How minutes do you code today?")
GRAPH_UPDATE_ENDPOINT = F"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_params['id']}"
pixela_update_params = {
    "date" : today_join,
    "quantity" : time_coding,
    }

response_update_graph = requests.post(url=GRAPH_UPDATE_ENDPOINT, json=pixela_update_params, headers=headers)
print(response_update_graph.text)