import requests
import sys


def get_summary_name():
    filepath = "diagram_1.bpmn"
    substring = "<bpmn:documentation>Feature: "
    filename = ""
    filenameFound = False
    with open(filepath) as fp:
        line = fp.readline()
        count = 1
        while line and filenameFound is False:
            if substring in line:
                filename = line.strip()[len(substring):]
                filenameFound = True
            line = fp.readline()
            count += 1
    return filename


get_headers = {
        'Authorization': 'Basic dDAwMjAyMzc2OjVlOWQ5eWt5'  # must have proper authentication? OAUTH
    }

post_headers = {
  'Content-Type': 'application/json'
}

try:
    meta = requests.get("http://localhost:8090/rest/api/2/issue/createmeta", headers=get_headers).json()
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

project_key = meta["projects"][0]["key"]
project_name = meta["projects"][0]["name"]
issuetypes = []
for issuetype in meta["projects"][0]["issuetypes"]:
    issuetypes.append(issuetype["name"])
url = "http://localhost:8090/rest/api/2/issue/"

summary = get_summary_name()

epic_obj = {
    "fields": {
       "project":
       {
          "key": project_key
       },
       "summary": summary,
       "description": "Scenario",
       "issuetype": {
          "name": "Epic"
       }
    }
}

payload = {
    "fields": {
        "project":
            {
                "key": "EEJ"
            },
        "summary": "Feature 3",
        "description": "Scenario",
        "issuetype": {
            "name": "Epic"
        }
    }
}

post_response = requests.post(url, headers=post_headers, data=epic_obj)

print(post_response.text)
