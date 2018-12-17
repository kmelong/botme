import json
import requests

groupme_api_token = c753aa20e3c20136c883020280fb407f
groupme_url_base = https://api.groupme.com/v3/groups?token=

headers = { 'Content-Type' : 'application/json',
            'Authorization' : 'Bearer {0}'.format(groupme_api_token)}

def get_account_info(): 