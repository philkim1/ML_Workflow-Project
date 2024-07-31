import json
import sagemaker
import base64
import os
import boto3


endpoint = os.environ['ENDPOINT']
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    
    image = base64.b64decode(event['image_data'])
    
    response = runtime.invoke_endpoint(EndpointName=endpoint, ContentType='image/png', Body=image)
    
    result = response['Body'].read().decode('utf-8')
    
    result = list(map(str.strip, result.split(',')))
    
    event['inferences'] = [float(result[0].replace('[','')),float(result[1].replace(']',''))]
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }