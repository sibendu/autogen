# filename: find_good_first_issue.py
import requests

def find_good_first_issue(repo_owner, repo_name):
    GITHUB_API = "https://api.github.com"
    issues_url = f"{GITHUB_API}/repos/{repo_owner}/{repo_name}/issues"
    params = {
        "state": "open",
        "labels": "good first issue"
    }
    response = requests.get(issues_url, params=params)
    if response.status_code == 200:
        issues = response.json()
        if issues:
            for issue in issues:
                print(f"Issue Title: {issue['title']}")
                print(f"Issue URL: {issue['html_url']}\n")
        else:
            print("No open 'good first issue' found.")
    else:
        print(f"Failed to fetch issues, status code: {response.status_code}")

find_good_first_issue("microsoft", "FLAML")