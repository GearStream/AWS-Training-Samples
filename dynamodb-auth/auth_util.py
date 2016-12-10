import random
import string
import boto3

dynamodb = boto3.resource(
    'dynamodb',
    region_name='eu-west-1'
)

table = dynamodb.Table('docker-test')


# Insert a new user into the database, obviously in real life we should encrypt the password!
def create_user(user_name, first_name, last_name, password):
    table.put_item(
        Item={
            'user_name': user_name,
            'first_name': first_name,
            'last_name': last_name,
            'password': password,
        }
    )


# Generate an auth token and add it to the database for a given user, assuming the user exists
def create_auth_token(username):
    token = _generate_random_token()

    table.update_item(
        Key={
            'user_name': username,
        },
        UpdateExpression='SET auth_token = :val1',
        ExpressionAttributeValues={
            ':val1': token
        }
    )

    return token


# Load the expected auth token from the db, check if it matches the supplied one for this user
def validate_auth_token(user_name, token_to_test):
    response = table.get_item(
        Key={
            'user_name': user_name,
        }
    )
    item = response['Item']

    return item.get('auth_token') == token_to_test


# Load the expected password from the db, check if it matches the supplied one for this user
def validate_password(user_name, password_to_test):
    response = table.get_item(
        Key={
            'user_name': user_name,
        }
    )
    item = response['Item']

    return item.get('password') == password_to_test


# Generate a random string of length 10
def _generate_random_token():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
