import os
import secrets
import boto3
import json


lambda_client = boto3.client('lambda', region_name='eu-west-2')
file_path = '/etc/technical_test/id.txt'
directory = '/etc/technical_test'

if os.path.exists(file_path):
    # read the ID
    with open(file_path, 'r') as file:
        id = file.read()

        payload = {
            "id": id,
            "ip": "PUTIP",
            "flag": "flag"
        }

        # Convert the payload to JSON string
        json_payload = json.dumps(payload)

        # Invoke the Lambda function
        response = lambda_client.invoke(
            FunctionName='test2',  # replace with your Lambda function name
            InvocationType='RequestResponse',  # for synchronous invocation
            Payload=json_payload
        )

        # Read the response
        response_payload = json.loads(response['Payload'].read())

        # Print the response (or handle it in another way)
        print(response_payload)


else:
    # make a directory
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass
    # make an ID and write to file
    new_id = secrets.token_hex(3)
    with open(file_path, 'w') as file:
        file.write(new_id)

