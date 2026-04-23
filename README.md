# Using Python Lambdas Lab

This lab introduces how to build serverless applications using Python and AWS Lambda.

You will deploy a Lambda function, connect it to Amazon DynamoDB, extend it with additional functionality, and write unit tests using pytest.

---

## Learning Objectives

By the end of this lab, you will be able to:

- Understand how Python code runs inside AWS Lambda
- Interact with AWS services using `boto3`
- Structure Lambda functions using clean, testable Python patterns
- Extend a Lambda function to support CRUD operations
- Write unit tests using pytest

---

## ⚠️ Important Notes (Real-World vs Lab)

This lab simplifies some patterns for learning purposes:

| Lab Approach | Production Best Practice |
|---|---|
| One Lambda for all CRUD operations | One Lambda per endpoint/action |
| Broad IAM permissions | Least-privilege IAM policies |
| Resources created via AWS Console | Infrastructure as Code (CloudFormation, Terraform, AWS CDK) |
| Manual `.zip` upload | CI/CD pipelines |

---

## Prerequisites

Before starting, ensure your local environment meets the following requirements:

- **Python:** version 3.13 or higher
- **IDE:** [PyCharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/) is recommended
- **AWS Account:** [Provided here](https://answerdigital.awsapps.com/start) for the duration of the lab

---

## Getting Started

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Set Up a Virtual Environment

Open the project in your IDE and familiarise yourself with the Lambda handler logic and how it uses the `boto3` library to communicate with AWS services.

Then set up your virtual environment:

1. **Create** the virtual environment:
    ```bash
    python -m venv venv
    ```

2. **Activate** the environment:
    - **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    - **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

3. **Install** dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Step 3: Create a DynamoDB Table

1. Log in to the **AWS Management Console** and navigate to **DynamoDB**.
2. In the sidebar, click **Tables**, then click **Create table**.
3. Configure the following settings:
    - **Table name:** `your_name_table` (e.g., `john_doe_table`)
    - **Partition key:** `ItemID` (Type: `String`)
4. Keep all other settings as default and click **Create table**.

### Step 4: Create the Lambda Function

1. Navigate to the **Lambda** service in the AWS Console.
2. Click **Create function** and select **Author from scratch**.
3. Configure the following:
    - **Function name:** `your_name_function` (e.g., `john_doe_lambda`)
    - **Runtime:** Python 3.13
4. Click **Create function**.

### Step 5: Set Environment Variables

Your Lambda uses an environment variable to determine which DynamoDB table to use.

1. In your Lambda function, go to **Configuration → Environment variables**.
2. Click **Edit → Add environment variable**.
3. Add the following:

    | Key | Value |
    |---|---|
    | `TABLE_NAME` | `your_name_table` |


Click the Code tab
Scroll down to the Runtime settings section
Click Edit
Change Handler from lambda_function.lambda_handler to lambda_handler.lambda_handler
Click Save

### Step 6: Grant IAM Permissions

To allow the Lambda to interact with DynamoDB:

1. In your Lambda function dashboard, go to the **Configuration** tab and select **Permissions**.
2. Click on the **Role name** to open the IAM Console.
3. Click **Add permissions → Attach policies**.
4. Search for and select `AmazonDynamoDBFullAccess`, then click **Add permissions**.

### Step 7: Deploy the Code

1. Navigate back to the **Code** tab of your Lambda function.
2. Create a `.zip` file containing your Python files.
3. Click the **Upload from** dropdown and select **.zip file**.
4. Upload your file and click **Save**.

### Step 8: Test the Function

1. Go to the **Test** tab.
2. Create a new test event.
3. Click **Test**.
4. Confirm a successful response.

### Step 9: Verify Data in DynamoDB

Return to the **DynamoDB** console, select your table, and click **Explore table items** to confirm the Lambda successfully interacted with the table.

---

## Core Task: Extending the Function

You are provided with a working "get all" endpoint.

**Your task:** implement full CRUD functionality.

| Operation | Description |
|---|---|
| **Create** | Add a new item |
| **Read** | Get a single item by ID |
| **Update** | Modify an existing item |
| **Delete** | Remove an item |

### Suggested Approach

Add new methods to `food_service.py`:

```python
def create_item(data): ...
def get_item(item_id): ...
def update_item(item_id, data): ...
def delete_item(item_id): ...
```

Route logic in the handler using the event action:

```python
action = event.get("action")
```

> **Best practice:** In production, each operation would typically be a separate Lambda mapped to its own API endpoint.

---

## Unit Testing with pytest

📖 **Docs:** [https://docs.pytest.org/](https://docs.pytest.org/)

Run the test suite:

```bash
pytest
```

**Key principles:**

- Test your Python functions, not the Lambda infrastructure itself
- Keep business logic separate from AWS dependencies
- Mock external services (e.g., DynamoDB) where needed

---

## Stretch Goal (Optional): Connect Lambda to API Gateway

1. Create an **HTTP API** in API Gateway.
2. Connect it to your Lambda function.
3. Deploy and test the following endpoints:

    ```
    GET  /items
    POST /items
    ```

> **Best practice:** In production, each route maps to a separate Lambda, and API configuration is defined using Infrastructure as Code.

---

## Cleanup

> [!IMPORTANT]
> To avoid unnecessary AWS costs, delete the AWS resources you created (**DynamoDB Table** and **Lambda Function**) once you have completed the lab.
