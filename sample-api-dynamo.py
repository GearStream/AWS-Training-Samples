from bottle import *
import boto3


@get('/api/version')
def get_data():
    return {'success': True}


# Create a new user
@post('/api/newuser')
def create_user():
    # Get the JSON from the API request
    request_json = request.json

    # Get first name and last name from JSON, default to None
    first_name = request_json.get('first_name', default=None)
    last_name = request_json.get('last_name', default=None)

    # Insert the first_name and last_name into a DynamoDB table called my_users
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('my_users')
    table.put_item(
        Item={
            'first_name': first_name,
            'last_name': last_name
        }
    )

    # Return a boolean OK
    return {'Success': True}


# Return all users in the table
@get('/api/all_users')
def get_all_users():
    # Instantiate a dynamodb connection
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('my_users')

    # Collect all items from the table
    response = table.scan()
    items = response['Items']

    # Return them to the caller
    return items


# Delete a user from the table
@delete('api/delete_user')
def delete_user():
    # Get the JSON from the API request
    request_json = request.json

    # Get first name and last name from JSON, default to None
    first_name = request_json.get('first_name', default=None)
    last_name = request_json.get('last_name', default=None)

    # Instantiate a dynamodb connection
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('my_users')

    table.delete_item(
        Key={
            'first_name': first_name,
            'last_name': last_name
        }
    )

run(host='0.0.0.0', port=8080, reloader=True, debug=True)
