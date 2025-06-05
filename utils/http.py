import requests
import os
from errors.errors import ApiError


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
    

def get_accounts_data():
    url = os.getenv("BELVO_PHAT") + "/api/accounts"
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
    
def get_transactions_data(account_id, link_id):
    url = os.getenv("BELVO_PHAT") + f"/api/transactions/?account={account_id}&link={link_id}"
    auth = (os.getenv("SECRECT_ID"), os.getenv("SECRECT_PASSWORD"))
    
    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            return response.json()
        else:
            error = ApiError()
            error.code = response.status_code
            error.description = "Error fetching transactions data: " + response.text
            raise error

    except requests.exceptions.RequestException:
        raise ApiError()