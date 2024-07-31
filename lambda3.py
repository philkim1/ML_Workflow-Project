import json

threshold = .93

def lambda_handler(event, context):
    
    inferences = event['inferences']
    
    meets_threshold = ((inferences[0]> threshold) | (inferences[1]>threshold))
    
    if meets_threshold:
        pass
    else:
        raise('threshold_confidence_not_met')
        
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
