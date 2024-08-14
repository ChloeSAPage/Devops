import os
import secrets


# file_path = '/etc/technical_test/id.txt'
# directory = '/etc/technical_test'
file_path = 'technical_test/id.txt'
directory = 'technical_test'

if os.path.exists(file_path):
    # read the ID
    with open(file_path, 'r') as file:
        id = file.read()
        print(id)
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

