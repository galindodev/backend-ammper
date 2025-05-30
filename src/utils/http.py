import requests
import os
from ..errors.errors import ApiError


def create_link_user(username, password):
    url = os.getenv("BELVO_PHAT")  + "/api/links/"  
    auth = (os.getenv("SECRECT_ID"), os.getenv("SECRECT_PASSWORD"))   
    payload = {
        "institution": "erebor_br_retail",
        "username": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, auth=auth, headers=headers) 
        if response.status_code == 201:
            return response.json()["id"]
        else:
            error = ApiError()
            error.code = response.status_code
            error.description = "Error creating link user: " + response.text
            raise error

    except requests.exceptions.RequestException:
        raise ApiError()


def get_institutions_data():
    url = os.getenv("BELVO_PHAT") + "/api/institutions/"
    auth = (os.getenv("SECRECT_ID"), os.getenv("SECRECT_PASSWORD"))
    
    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            return response.json()
        else:
            error = ApiError()
            error.code = response.status_code
            error.description = "Error fetching institutions data: " + response.text
            raise error

    except requests.exceptions.RequestException:
        raise ApiError()
    

def get_accounts_data(link_id):
    url = os.getenv("BELVO_PHAT") + f"/api/accounts/?link={link_id}"
    auth = (os.getenv("SECRECT_ID"), os.getenv("SECRECT_PASSWORD"))
    
    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            return response.json()
        else:
            error = ApiError()
            error.code = response.status_code
            error.description = "Error fetching accounts data: " + response.text
            raise error

    except requests.exceptions.RequestException:
        raise ApiError()