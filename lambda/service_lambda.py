import logging
import auth_util



# Create a new user
def create_user_handler(event, context):
    logging.info("HTTP post call made to /api/new-user")
   

    # Get first name and last name from JSON, default to None
    first_name = event.get('first_name')
    last_name = event.get('last_name')
    username = event.get('username')
    password = event.get('password')

    # If you want you could use format for logging. It's more pythonie
    # logging.info('You asked me to create a new user called {} {}'.format(first_name, last_name))
    logging.info("You asked me to create a new user called %s %s", first_name, last_name)

    auth_util.create_user(username, first_name, last_name, password)

    return {'success': True}


# Login and get an auth token
def login(event, context):
    logging.info("HTTP post call made to /api/login")


    # Get first name and last name from JSON, default to None
    username = event.get('username')
    password = event.get('password')

    #logging.info('{} is trying to login'.format(username))
    logging.info("%s is trying to login", username)

    if not auth_util.validate_password(username, password):
        logging.warn("%s tried to login with an invalid password", username)
        # Not sure how you will map it in API gateway
        # leaving it as a return but could raise an exception like : raise Exception('HTTP401')
        return {'success': False} 

    # logging.info('{} successfully logged in'.format(username))
    logging.info("%s successfully logged in", username)

    token = auth_util.create_auth_token(username)
    return {'success': True, 'token': token}


# Return all users in the table
def get_all_users(event, context):
    logging.info("HTTP post call made to /api/all-users")

    # We need to implement this

    return {'success': True}


# Delete a user from the table
def delete_user(event, context):
    logging.info("HTTP delete call made to /api/delete-user")


    # Get first name and last name from JSON, default to None
    username = event.get('username')
    token = event.get('token')
    username_to_delete = event.get('username_to_delete')

    if not auth_util.validate_auth_token(username, token):
        #logging.warn('{} tried to call the delete method with an invalid token'.format(username))
        logging.warn("%s tried to call the delete method with an invalid token", username)
        # Not sure how you will map it in API gateway
        # leaving it as a return but could raise an exception like : raise Exception('HTTP401')
        return {'success': False}

    # logging.info('{} asked me to delete {}'.format(username, username_to_delete)
    logging.info("%s asked me to delete %s", username, username_to_delete)

    # We will add the code to delete later

    return {'success': True}


