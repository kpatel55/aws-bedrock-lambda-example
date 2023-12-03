# Amazon Bedrock Lambda Demo

A simple demo of Amazon Bedrock via a Python function running on AWS Lambda using Serverless Framework. The deployed function includes an event definition that triggers a Lambda invocation when a .txt file is uploaded to an S3 bucket. The lambda function then reads in the contents of the file and asks Jurassic-2 Ultra to summarize the text via a call to Bedrock.

## Usage

### Deployment

In order to deploy the example, you'll need to specify a globally unique bucket name in the serverless.yml file on line 40. Then run the following command:

```
$ sls deploy
```

After running deploy, you should see output similar to:

```bash
Deploying aws-bedrock-serverless to stage dev (us-east-1)

✔ Service deployed to stack aws-bedrock-serverless-dev (111s)

functions:
  bedrockDemo: aws-bedrock-serverless-dev-bedrockDemo (4.2 kB)
```

### Invocation

After successful deployment, you can trigger the deployed function by uploading the sample txt file in this directory to S3 using the following command:

```
aws s3 cp sample-medium-article.txt s3://your_bucket_name_here
```

This should result in a response similar to the following in your Lambda function CloudWatch logs:

```
The article provides an introduction to AWS CloudWatch Composite Alarms,
which are alarms that determine the state by monitoring the states of other alarms...
```
