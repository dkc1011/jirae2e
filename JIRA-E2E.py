import re
import subprocess
import requests
import json
import sys
# issue_id = "EEJ-1"  # test placeholder
issue_name = "new_bpmn"
# issue_id = sys.argv[1] #works with argument passed in
# issue_name = sys.argv[1] #works with argument passed in
url_name = "http://localhost:8080/rest/api/2/search?jql=summary~"  # must get JIRA address from jenkins?
url_id = "http://localhost:8080/rest/api/2/issue/"
save_path = ""
headers = {
        'Authorization': 'Basic amFzb25kb3dsaW5nODg6SXJpc2hwcmlkZTE='  # must have proper authentication? OAUTH
    }


def scenario_constructor(k, title, s):
    string = "Scenario : " + k + " " + title + "\n" + s + "\n\n"
    return string


def get_api_response():
    featureURL = url_name + issue_name
    #featureURL = url_id + issue_id

    try:
        featureResponse = requests.get(featureURL, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    return json.loads(featureResponse.text)


def retrieve_scenario_text():
    key = task['key']  # get and store key of scenario
    scenarioURL = url_id + key  # create URL for specific scenario from JIRA
    scenarioResponse = requests.get(scenarioURL, headers=headers)  # get scenario from JIRA
    dataScenario = json.loads(scenarioResponse.text)  # converts scenario text to JSON
    scenarioTitle = dataScenario["fields"]["summary"]  # get scenario title
    scenario = dataScenario["fields"]["description"]  # get scenario description

    return scenario_constructor(key, scenarioTitle, scenario)  # create whole scenario


def feature_file_formatter():
    return "Feature: " + feature_id_generator() + " " + feature_name_format() + "\n\n" + dataJIRA_subtasks_description #construct text for file


def file_creator():
    # featureName = dataJIRA_feature.replace(" ", "")  # remove spaces from feature title
    # featureName = featureName[0].lower() + featureName[1:]  # make first letter of feature name lowercase

    fileName = dataJIRA_feature + ".feature"  # construct file name

    e2eFile = open(save_path + fileName, "w+")  # open/create file with path and file name

    e2eFile.write(e2eText)  # write to file

    e2eFile.close()  # close file


def feature_name_format():
    feature_name = dataJIRA_feature[0].upper() + dataJIRA_feature[1:] #makes first letter of feature name uppercase
    feature_name = re.sub(r"(\w)([A-Z])", r"\1 \2", feature_name) #add spaces before upper case letters
    return feature_name


def feature_id_generator():
    feature_id = dataJIRA_issues['key']
    return feature_id


# def branch_creator():
#     subprocess.run(["git", "checkout", "-b", dataJIRA_feature])


dataJIRA = get_api_response() #converts text to JSON

if dataJIRA["total"] != 0:

    for issue in dataJIRA['issues']:
        if issue['fields']['issuetype']['name'] == 'Task':
            dataJIRA_issues = issue

    dataJIRA_fields = dataJIRA_issues['fields']
    dataJIRA_feature = dataJIRA_fields['summary']
    #print(dataJIRA_feature)
    dataJIRA_subtasks = dataJIRA_fields['subtasks'] #get list of scenarios
    #print(dataJIRA_subtasks)

    dataJIRA_subtasks_description = "" #create empty string to hold scenarios


    for task in dataJIRA_subtasks: #for every scenario in a feature
        dataJIRA_subtasks_description += retrieve_scenario_text()

    e2eText = feature_file_formatter()

    #branch_creator()

    file_creator()

else:
    print("No features found for ", issue_name)