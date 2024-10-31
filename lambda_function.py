import requests
import json
import os

# Fetch Notion API token from environment variables
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

def lambda_handler(event, context):
    # Set the Notion API URL
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    # Define headers, including the API token
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    # Make a POST request to query the database
    response = requests.post(url, headers=headers)
    data = response.json()

    # Extract and log titles of the tasks
    tasks = []
    for result in data.get("results", []):
        title = result.get("properties", {}).get("Name", {}).get("title", [])
        if title:
            tasks.append(title[0]["text"]["content"])

    # Print tasks for debugging (or process as needed)
    print("Tasks in Notion database:", tasks)

    return {
        'statusCode': 200,
        'body': json.dumps({"tasks": tasks})
    }
