from bottle import *
import logging

_api_version = 1.0


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

    logging.info("You asked me to create a new user called %s %s", first_name, last_name)
    return {'success': True}


# Return all users in the table
@get('/api/all-users')
def get_all_users():
    logging.info("HTTP post call made to /api/all-users")

    # We need to implement this

    return {'success': True}


# Delete a user from the table
@delete('api/delete-user')
def delete_user():
    logging.info("HTTP delete call made to /api/delete-user")

    # Get the JSON from the API request
    request_json = request.json

    # Get first name and last name from JSON, default to None
    first_name = request_json.get('first_name', None)
    last_name = request_json.get('last_name', None)
    username = request_json.get('username', None)

    logging.info("You asked me to delete a user called %s %s", first_name, last_name)


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

    logging.info('Starting HTTP server')
    run(host='0.0.0.0', port=8080, reloader=True, debug=True)


main()
