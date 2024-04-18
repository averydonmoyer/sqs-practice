import boto3 
import json 

sqs = boto3.client('sqs') 
QueueUrl='https://sqs.us-east-1.amazonaws.com/211125649415/myqueue'

response = sqs.get_queue_attributes(
    QueueUrl=QueueUrl, 
    AttributeNames=[
        'All'
    ]
)
print(response['Attributes']['ApproximateNumberOfMessages']) 