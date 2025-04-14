import json
import urllib.request
from git_app_configs import *
from rich import print
from urllib import request


print("Running script", sys.argv[0])
print("Fetching username: ", USER)

GITHUB_URL = f"{GITHUB_API}/users/{USER}/events/public"

def fetch_data():
    responce = urllib.request.urlopen(GITHUB_URL)
    return json.load(responce)

events = fetch_data()

for event in events[:LIMIT]:
    event_type = event.get("type", "Unknown")
    repo = event.get("repo", {}).get("name", "Unknown Repo")
    created_at = event.get("created_at", "Unknown Time")

#юзал rich т.к. текст прикольный->
    print(f"[green]Type: [/green]  {event_type}")
    print(f"[cyan]Repo: [/cyan]  {repo}")
    print(f"[magenta]Date: [/magenta]  {created_at}")
    print("-" * 40)