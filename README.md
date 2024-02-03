# Amazon Bedrock Lambda Demo

A simple demo of Amazon Bedrock via a Python function running on AWS Lambda using Serverless Framework. The deployed function includes an event definition that triggers a Lambda invocation when a .txt file is uploaded to an S3 bucket. The lambda function then reads in the contents of the file and asks Jurassic-2 Ultra to summarize the text via a call to Bedrock.

This guide assumes you've already obtained access to the Jurassic-2 Ultra model for your AWS account. If not, instructions on how to do so can be found here: https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html

The Medium article related to this demo can be found here: https://medium.com/@kpatel55/autoscaling-bedrock-requests-using-lambda-and-serverless-framework-4738fcafd78c

## Usage

### Deployment

In order to deploy the example, you'll need to specify a globally unique bucket name in the serverless.yml file on lines 21 and 57. Then run the following commands to install the autoscaling plugin and to deploy:

```
npm install serverless-provisioned-concurrency-autoscaling
sls deploy
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

This should result in a response similar to the following in your Lambda function's CloudWatch logs:

```
The article provides an introduction to AWS CloudWatch Composite Alarms,
which are alarms that determine the state by monitoring the states of other alarms...
```
