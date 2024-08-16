def lambda_handler(event, context):
    return event['id'], event['ip'], event['flag']