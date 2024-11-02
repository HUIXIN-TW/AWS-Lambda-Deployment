## AWS Lambda Deployment

This project uses AWS Lambda to sync tasks between Notion and Google Calendar. The Lambda function is designed to query and create tasks in Notion and interact with Google Calendar events.

### Tech Stack

- **AWS Lambda**: A serverless compute service that runs your code in response to events and automatically manages the underlying compute resources.
- **GitHub**: A version control system for managing code and automating deployment.
- **AWS IAM**: Identity and Access Management to securely manage access to AWS services and resources.
- **Notion API**: Interacting with Notion's databases and creating or updating tasks.
- **Google Calendar API**: Integration for managing events in Google Calendar.

### Implementation Sequence

#### Step 1: Set Up GitHub Repository

1. Create a new repository on GitHub.
2. Clone the repository to your local machine:
   ```bash
   git clone git@github.com:HUIXIN-TW/AWS-Lambda-Deployment.git
   cd AWS-Lambda-Deployment
   ```

#### Step 2: Create the Lambda Function

1. **Create an IAM Role**:
   - Go to the IAM console in AWS.
   - Create a new role with the necessary permissions for Lambda execution.

2. **Create a Lambda Function**:
   - Go to the Lambda console in AWS.
   - Click on "Create function."
   - Choose "Author from scratch," set the function name, and select the runtime (Python 3.12).
   - Assign the IAM role created in the previous step.

3. **Create and Upload a Layer for Dependencies**:
   - Package your dependencies (like `requests`) into a layer.
   - Upload the layer to the Lambda layer.
   - Upload Google Calendar APIs to the Lambda layer.

#### Step 3: Integrate Notion API

- Implement the logic to query and create tasks in your Notion database using the Notion API within your Lambda function.

#### Step 4: Set Up GitHub Action for Auto-Deployment

1. Create a `.github/workflows/deploy.yml` file in your repository with the following content:

2. Push your changes to the `master` branch. GitHub Actions will automatically trigger the deployment workflow.

### Step 5: Test the Lambda Function

1. Invoke your Lambda function using the AWS Lambda console or AWS CLI to ensure it integrates correctly with the Notion API and functions as expected.
2. Monitor CloudWatch logs for debugging and verification.

### Init the program
```bash
# Step 1: Create a virtual environment named 'notionsyncgcal' in the current directory
# This isolates your project dependencies to avoid conflicts with other projects.
python3 -m venv notionsyncgcal

# Step 2: Activate the virtual environment
# This enables you to use the isolated Python environment with its own dependencies.
source notionsyncgcal/bin/activate

# Step 3: Freeze the current environment's package dependencies into 'requirements.txt'
# This generates a list of installed packages, which can be used to replicate the environment.
pip freeze > requirements.txt

# Step 4: Install the packages listed in 'requirements.txt' (if any changes were made)
# This ensures that all required packages are installed based on the frozen list.
pip install -r requirements.txt

# Create a directory for the Lambda layer to hold dependencies and other files.
mkdir lambda_layer

# Create a subdirectory for the Python packages within the layer.
mkdir -p lambda_layer/python

# Copy the client_secret.json file into the layer's python directory
# This JSON file contains credentials needed for the Google API.
cp /Users/huixinyang/Documents/CodeProject/Notion/NotionSyncGCal/token/client_secret.json lambda_layer/python/

# Copy all dependencies from the virtual environment's site-packages to the layer
# This allows your Lambda function to access these packages at runtime.
cp -r notionsyncgcal/lib/python3.9/site-packages/* lambda_layer/python/

# Step 5: Compress all contents into a zip file to upload as a Lambda layer
# This creates 'lambda_layer.zip', which includes the JSON file and all dependencies needed by the Lambda function.
cd lambda_layer
zip -r lambda_layer.zip python/
```

### Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Current Implementation vs Next Action
- [ ] Credential and API Key Storage Options
> For multi-user credential storage where security is a top priority:
Use AWS Secrets Manager if you need high security, frequent credential rotation, and are okay with slightly higher costs. This approach minimizes the risk of exposing credentials and simplifies secure access.
Use Amazon S3 if you prioritize lower cost and don’t require frequent rotation. S3 is manageable if you implement strict access control but may require additional effort to secure effectively.
