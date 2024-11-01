import json
from create_notion_task.create_notion_task import create_notion_task
from query_notion_task.query_notion_task import query_notion_task

def lambda_handler(event, context):
    # Query today's tasks
    tasks = query_notion_task()

    # Print tasks for debugging (or process as needed)
    print("Today's tasks in Notion database:", tasks)

    # Logic to create a new task
    task_name = "New Task Title From AWS Lambda"
    date = "2024-11-01"
    initiative = "UWA"
    extra_info = "Additional Info By AWS Lambda"
    location = "Perth"

    # Create a new task
    response = create_notion_task(task_name, date, initiative, extra_info, location)
    
    # Log the response for debugging
    print("Create Task Response:", response.json())

    return {
        'statusCode': 200,
        'body': json.dumps({"tasks": tasks})
    }

# Mock event and context for local testing
if __name__ == "__main__":
    mock_event = {}
    mock_context = None
    print(lambda_handler(mock_event, mock_context))
