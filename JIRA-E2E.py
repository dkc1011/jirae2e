import requests
import json
import sys

issue_id = "EEJ-1"  # test placeholder
#issue_id = sys.argv[1] #works with argument passed in
url = "http://localhost:8080/rest/api/2/issue/"  # must get JIRA address from jenkins?
save_path = ""
headers = {
        'Authorization': 'Basic amFzb25kb3dsaW5nODg6SXJpc2hwcmlkZTE='  # must have proper authentication? OAUTH
    }


def scenario_constructor(k, title, s):
    string = "Scenario : " + k + " " + title + "\n" + s + "\n\n"
    return string


def get_api_response():
    featureURL = url + issue_id

    featureResponse = requests.get(featureURL, headers=headers)

    return json.loads(featureResponse.text)


def retrieve_scenario_text():
    key = task['key']  # get and store key of scenario
    scenarioURL = url + key  # create URL for specific scenario from JIRA
    scenarioResponse = requests.get(scenarioURL, headers=headers)  # get scenario from JIRA
    dataScenario = json.loads(scenarioResponse.text)  # converts scenario text to JSON
    scenarioTitle = dataScenario["fields"]["summary"]  # get scenario title
    scenario = dataScenario["fields"]["description"]  # get scenario description

    return scenario_constructor(key, scenarioTitle, scenario)  # create whole scenario


def feature_file_formatter():
    return "Feature: " + dataJIRA_feature + "\n\n" + dataJIRA_subtasks_description #construct text for file


def file_creater():
    featureName = dataJIRA_feature.replace(" ", "")  # remove spaces from feature title
    featureName = featureName[0].lower() + featureName[1:]  # make first letter of feature name lowercase

    fileName = featureName + ".feature"  # construct file name

    e2eFile = open(save_path + fileName, "w+")  # open/create file with path and file name

    e2eFile.write(e2eText)  # write to file

    e2eFile.close()  # close file


dataJIRA = get_api_response() #converts text to JSON
dataJIRA_feature = dataJIRA['fields']['summary'] #gets feature title

dataJIRA_subtasks = dataJIRA['fields']['subtasks'] #get list of scenarios

dataJIRA_subtasks_description = "" #create empty string to hold scenarios

for task in dataJIRA_subtasks: #for every scenario in a feature
    dataJIRA_subtasks_description += retrieve_scenario_text()

e2eText = feature_file_formatter()

file_creater()
