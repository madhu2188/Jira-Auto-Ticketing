import time
import requests
import json
import config_file

JIRA_TOKEN = config_file.JIRA_TOKEN
JIRA_URL = config_file.JIRA_URL


def get_issues(summary, channel_name):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {JIRA_TOKEN}",
    }

    payload = {
        "jql": f'project = "TESITSM" AND summary ~ "{summary}" AND status != Closed AND cf[13529] = {channel_name}',
        "startAt": 0,
        "maxResults": 5000,
        "fields": ["summary", "key"],
    }

    try:
        res = requests.post(f"{JIRA_URL}/rest/api/2/search", headers=headers, json=payload)
        if res.status_code == 200:
            response = res.json()
            issues = []
            for issue in response["issues"]:
                summary = issue["fields"]["summary"]
                key = issue["key"]
                issues.append({"key": key, "summary": summary})
            return issues
        else:
            return None

    except Exception as e:
        print(e)
        return None


def create_issue(summary, channel_name):
    url = f"{JIRA_URL}/rest/api/2/issue"
    headers = {
        "Authorization": f"Bearer {JIRA_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "fields": {
            "project": {"key": "TESITSM"},
            "summary": summary,
            "description": "",
            "issuetype": {"name": "Incident"},
            "customfield_13529": {"value": channel_name},
        }
    }

    try:
        res = requests.post(url, headers=headers, data=json.dumps(payload))
        if res.status_code == 201:
            response = res.json()
            print(f"Ticket created with ID: {response['key']}")
            return f"Ticket created with ID: {response['key']}"
        else:
            return None

    except Exception as e:
        print(e)
        return None


def check_and_create_issue(summary, channel_name):
    issues = get_issues(summary, channel_name)
    if issues:
        print(f"Ticket already exists. {issues[0]['key']}")
        return f"Ticket already exists. {issues[0]['key']}"
    else:
        return create_issue(summary, channel_name)


