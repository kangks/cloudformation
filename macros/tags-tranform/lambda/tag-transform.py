import boto3

def handler(event, context):

    # Globals
    region = event['region']
    accountId = event['accountId']
    transformId = event['transformId']
    params = event['params']
    requestId = event['requestId']
    fragment = event['fragment']
    templateParameterValues = event['templateParameterValues']

    # Pre-define the Response
    response = {
        "requestId": requestId,
        "status": "success"
    }

    # Split the input string to dictionary
    tagString = templateParameterValues['tags']
    fragment['tag'] = dict(x.split("=") for x in tagString.split(","))
    
    response['fragment'] = fragment
    return response