import os
import secrets
import boto3
import json


def make_payload(id, flag):
        # get public ip
        ip = os.popen("ec2metadata --public-ipv4").read().strip()

        payload = {
        "id": id,
        "ip": ip,
        "flag": flag # a new id
        }

        # Convert the payload to JSON string
        json_payload = json.dumps(payload)

        # Invoke the Lambda function
        response = lambda_client.invoke(
            FunctionName='test2',
            InvocationType='RequestResponse',
            Payload=json_payload
        )

        return response


lambda_client = boto3.client('lambda', region_name='eu-west-2')
file_path = '/etc/technical_test/id.txt'
directory = '/etc/technical_test'


if os.path.exists(file_path):
    # read the ID
    with open(file_path, 'r') as file:
        id = file.read()

    response = make_payload(id, False)

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

    response = make_payload(id, True)

    # Read the response
    response_payload = json.loads(response['Payload'].read())

    # Print the response (or handle it in another way)
    print(response_payload)

