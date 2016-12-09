from bottle import *
import logging
import auth_util

_api_version = 1.0


# GET http://server_ip:port/api/version
@get('/api/version')
def get_data():
    logging.info("HTTP get call made to /api/version")

    return {'success': True, 'version': _api_version}


# Create a new user
@post('/api/new-user')
def create_user():
    logging.info("HTTP post call made to /api/new-user")

    # Get the JSON from the API request
    request_json = request.json

    # Get first name and last name from JSON, default to None
    first_name = request_json.get('first_name', None)
    last_name = request_json.get('last_name', None)
    username = request_json.get('username', None)
    password = request_json.get('password', None)

    logging.info("You asked me to create a new user called %s %s", first_name, last_name)

    auth_util.create_user(username, first_name, last_name, password)

    return {'success': True}


# Login and get an auth token
@post('/api/login')
def login():
    logging.info("HTTP post call made to /api/login")

    # Get the JSON from the API request
    request_json = request.json

    # Get first name and last name from JSON, default to None
    username = request_json.get('username', None)
    password = request_json.get('password', None)

    logging.info("%s is trying to login", username)

    if not auth_util.validate_password(username, password):
        logging.warn("%s tried to login with an invalid password", username)
        response.status = 401
        return {'success': False}

    logging.info("%s successfully logged in", username)

    token = auth_util.create_auth_token(username)
    return {'success': True, 'token': token}


# Return all users in the table
@get('/api/all-users')
def get_all_users():
    logging.info("HTTP post call made to /api/all-users")

    # We need to implement this

    return {'success': True}


# Delete a user from the table
@delete('/api/delete-user')
def delete_user():
    logging.info("HTTP delete call made to /api/delete-user")

    # Get the JSON from the API request
    request_json = request.json

    # Get first name and last name from JSON, default to None
    username = request_json.get('username', None)
    token = request_json.get('token', None)
    username_to_delete = request_json.get('username_to_delete', None)

    if not auth_util.validate_auth_token(username, token):
        logging.warn("%s tried to call the delete method with an invalid token", username)
        response.status = 401
        return {'success': False}

    logging.info("%s asked me to delete %s", username, username_to_delete)

    # We will add the code to delete later

    return {'success': True}


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

    logging.info('Starting HTTP server')
    run(host='0.0.0.0', port=8080, reloader=True, debug=True)


main()
