## AWS Lambda Deployment

This project automates task management by integrating AWS Lambda with the Notion API. It allows for querying and creating tasks in a Notion database seamlessly.

### Tech Stack

- **AWS Lambda**: A serverless compute service that runs your code in response to events and automatically manages the underlying compute resources.
- **GitHub**: A version control system for managing code and automating deployment.
- **AWS IAM**: Identity and Access Management to securely manage access to AWS services and resources.
- **Notion API**: An API for interacting with Notion's databases and creating or updating tasks.

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
   - Upload the layer to AWS Lambda

#### Step 3: Integrate Notion API

- Implement the logic to query and create tasks in your Notion database using the Notion API within your Lambda function.

#### Step 4: Set Up GitHub Action for Auto-Deployment

1. Create a `.github/workflows/deploy.yml` file in your repository with the following content:

2. Push your changes to the `master` branch. GitHub Actions will automatically trigger the deployment workflow.

### Step 5: Test the Lambda Function

1. Invoke your Lambda function using the AWS Lambda console or AWS CLI to ensure it integrates correctly with the Notion API and functions as expected.
2. Monitor CloudWatch logs for debugging and verification.

### Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
