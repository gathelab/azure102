import requests
# pprint is used to format the JSON response
from pprint import pprint

subscription_key = "699d78bf82cb4546a1c11f13bac3952f"
endpoint = "https://devailanguage8080.cognitiveservices.azure.com/"

language_api_url = endpoint + "/text/analytics/v3.0/languages"

documents = {"documents": [
    {"id": "1", "text": "This is a document written in English."},
    {"id": "2", "text": "Este es un document escrito en Español."},
    {"id": "3", "text": "这是一个用中文写的文件"}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)
