import json
import boto3

s3 = boto3.client('s3')

# Bedrock client used to interact with APIs around models
bedrock = boto3.client(
    service_name='bedrock', 
    region_name='us-east-1'
)

# Bedrock Runtime client used to invoke and question the models
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

def bedrockDemo(event, context):
    # Grab bucket name and text file from event 
    s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file = event["Records"][0]["s3"]["object"]["key"]

    # Read the text file and convert the contents to string type
    data = s3.get_object(Bucket=s3_bucket, Key=s3_file)
    contents = data['Body'].read()
    text = contents.decode("utf-8")

    # Specify model we want to use and create prompt
    modelId = "ai21.j2-ultra-v1"
    prompt="Given the article provided at the end of the prompt, summarize the article. Here is the article: {}".format(text)
    
    # The payload provided to Bedrock 
    body = json.dumps(
        {
            "prompt": prompt, 
            "maxTokens": 2049,
            "temperature": 0.7,
            "topP": 1,
            "stopSequences":[],
            "countPenalty":{"scale":0},
            "presencePenalty":{"scale":0},
            "frequencyPenalty":{"scale":0}
        }
    )

    # The call made to the model
    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=modelId,
        accept='application/json',
        contentType='application/json'
    )
    response_body = json.loads(response.get('body').read())

    # The response from the model
    answer = json.dumps(response_body.get("completions")[0].get("data").get("text"))
    print("Summarizing the article...")
    print(answer)
    
    return {
        'statusCode': 200,
        'body': json.dumps({ "Answer": answer })
    }
