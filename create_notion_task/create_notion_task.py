import requests
import os

# Fetch Notion API token and database ID from environment variables
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")


def create_notion_task(task_name, date, initiative, extra_info, location):
    # Set the Notion API URL
    url = "https://api.notion.com/v1/pages"

    # Define headers, including the API token
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }

    # Define the body of the request
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Task Name": {"title": [{"text": {"content": task_name}}]},
            "Date": {"date": {"start": date}},
            "Initiative": {
                "multi_select": [{"name": initiative}]  # Adjusted to multi_select
            },
            "Extra Info": {"rich_text": [{"text": {"content": extra_info}}]},
            "Location": {"rich_text": [{"text": {"content": location}}]},
        },
    }

    # Make a POST request to create a new task
    response = requests.post(url, headers=headers, json=payload)
    return response
