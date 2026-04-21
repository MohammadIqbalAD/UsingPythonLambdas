# UsingPythonLambdas Lab

This repository contains boilerplate code and step-by-step instructions for deploying a Python-based AWS Lambda function that interacts with an Amazon DynamoDB table.

## Prerequisites

Before starting the session, ensure your local environment meets the following requirements:

* **Python:** version 3.13 or higher.
* **IDE:** [PyCharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/) is recommended.
* **AWS Account:** Will be provided during the lab.

---

## Getting Started

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Review Code and Setup Virtual Environment
Open the project in your IDE. Familiarize yourself with the Lambda handler logic and how it utilizes the `boto3` library to communicate with AWS services. Follow the steps below to setup your virtual environment:
1. Create the virtual environment
```bash
python -m venv venv
```
2. Activate the environment
```bash
.\venv\Scripts\activate
```
3. Install packages
```bash
pip install -r requirements.txt
```

### Step 3: Create a DynamoDB Table
1.  Log in to the **AWS Management Console** and navigate to **DynamoDB**.
2.  In the sidebar, click **Tables**, then click **Create table**.
3.  Configure the following settings:
    * **Table name:** `your_name_table` (e.g., `john_doe_table`).
    * **Partition key:** `ItemID` (Type: String).
4.  Keep all other settings as default and click **Create table**.

### Step 4: Create the Lambda Function
1.  Navigate to the **Lambda** service in the AWS Console.
2.  Click **Create function** and select **Author from scratch**.
3.  Configure the following:
    * **Function name:** `your_name_function` (e.g., `john_doe_lambda`).
    * **Runtime:** Python 3.13.
    * **Architecture:** x86_64.
4.  Click **Create function**.

### Step 5: Update Environment Variables
In your local lambda code, ensure you update the environment variable or configuration string to match the name of the DynamoDB table you just created.

### Step 6: Grant IAM Permissions
To allow the Lambda to write to DynamoDB:
1.  In your Lambda function dashboard, go to the **Configuration** tab and select **Permissions**.
2.  Click on the **Role name** to open the IAM Console.
3.  Click **Add permissions** > **Attach policies**.
4.  Search for and select `AmazonDynamoDBFullAccess` and click **Add permissions**.

### Step 7: Deploy the Code
1.  Navigate back to the **Code** tab of your Lambda function.
2.  Create a `.zip` file containing your Python script.
3.  Click the **Upload from** dropdown and select **.zip file**.
4.  Upload your file and click **Save**.

### Step 8: Test the Function
1.  Go to the **Test** tab.
2.  Configure a new test event (the default JSON is usually fine for a basic test).
3.  Click the **Test** button.
4.  Verify the "Execution result" returns a 200 OK status.

### Step 9: Verify Data in DynamoDB
Return to the **DynamoDB** console, select your table, and click **Explore table items** to confirm the Lambda successfully inserted or modified an item.

---

## Cleanup
> [!IMPORTANT]  
> To avoid unnecessary AWS costs, ensure you delete the AWS resources you have created (**DynamoDB Table** / **Lambda Function**) once you have completed the lab.
