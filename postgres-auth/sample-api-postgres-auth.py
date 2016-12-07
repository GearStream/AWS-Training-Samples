from bottle import *


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
    user_name = request_json.get('user_name', default=None)
    password = request_json.get('password', default=None)



    # Return a boolean OK
    return {'Success': True}


run(host='0.0.0.0', port=8080, reloader=True, debug=True)
