import requests
import os
from todo_app.Card import Card
import json

key = os.getenv("TRELLO_KEY")
token = os.getenv("TRELLO_TOKEN")
boardID = os.getenv("TRELLO_ID")

headers = {
   "Accept": "application/json"
}

def get_items():
    url = f"https://api.trello.com/1/boards/{boardID}/lists?key={key}&token={token}&cards=open"
    response = requests.request("GET", url, headers=headers).json() 
    items = []
    for list in response: 
        for item in list["cards"]:
            items.append(Card.card_content(item, list))
    return items

def add_item(title, description):
    list_id = get_list_id("Not Started")
    url = f"https://api.trello.com/1/cards?key={key}&token={token}&desc={description}&name={title}&idList={list_id}"
    print(requests.request("POST", url, headers=headers))

def progress_item(id: str):
    list_id_progress = get_list_id("In Progress")
    url = f"https://api.trello.com/1/cards/{id}?key={key}&token={token}&idList={list_id_progress}"
    requests.request("PUT", url, headers=headers)

def complete_item(id: str):
    list_id_complete = get_list_id("Done")
    url = f"https://api.trello.com/1/cards/{id}?key={key}&token={token}&idList={list_id_complete}"
    requests.request("PUT", url, headers=headers)

def remove_item(id: str):
    url = f"https://api.trello.com/1/cards/{id}?key={key}&token={token}"
    requests.request("DELETE", url, headers=headers)

def get_list_id(name):
    url = f"https://api.trello.com/1/boards/{boardID}/lists?key={key}&token={token}"
    response = requests.request("GET", url, headers=headers).json()
    return next(list["id"] for list in response if list["name"] == name)