import requests
import json
import os
from datetime import datetime

# Fetch Notion API token from environment variables
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

def query_notion_task():
    # Set the Notion API URL
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    # Get today's date in the format Notion expects (YYYY-MM-DD)
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Define headers, including the API token
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    # Define the filter to only get today's tasks
    filter_payload = {
        "filter": {
            "property": "Date",  # Change this to your date property name
            "date": {
                "equals": today
            }
        }
    }

    # Make a POST request to query the database with the filter
    response = requests.post(url, headers=headers, json=filter_payload)
    data = response.json()

    # Extract and log titles of the tasks
    tasks = []
    for result in data.get("results", []):
        title = result.get("properties", {}).get("Task Name", {}).get("title", [])
        if title:
            tasks.append(title[0]["text"]["content"])

    return tasks
