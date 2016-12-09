import random
import string
import psycopg2


# Insert a new user into the database, obviously in real life we should encrypt the password!
def create_user(user_name, first_name, last_name, password):
    query = 'INSERT INTO gearstream.user_table (user_name, first_name, last_name, password) VALUES (%s, %s, %s, %s)'

    _execute_sql(query, (user_name, first_name, last_name, password))


# Generate an auth token and add it to the database for a given user, assuming the user exists
def create_auth_token(username):
    token = _generate_random_token()
    query = 'UPDATE gearstream.user_table SET token=%s WHERE user_name=%s'

    _execute_sql(query, (token, username))
    return token


# Load the expected auth token from the db, check if it matches the supplied one for this user
def validate_auth_token(user_name, token_to_test):
    query = 'SELECT token FROM gearstream.user_table WHERE user_name = %s'
    token_in_db = _execute_query(query, (user_name,))

    return token_in_db[0] == token_to_test


# Load the expected password from the db, check if it matches the supplied one for this user
def validate_password(user_name, password_to_test):
    query = 'SELECT password FROM gearstream.user_table WHERE user_name = %s'
    password_in_db = _execute_query(query, (user_name,))[0]

    return password_in_db == password_to_test


def _execute_sql(sql, values):
    conn = _get_connection()
    cursor = conn.cursor()

    cursor.execute(sql, values)

    cursor.close()
    conn.close()


def _execute_query(sql, values):
    conn = _get_connection()
    cursor = conn.cursor()

    cursor.execute(sql, values)
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data


def _get_connection():
    conn = psycopg2.connect("dbname='gearstream' user='postgres' host='postgres' password='password'")
    conn.autocommit = True
    return conn


# Generate a random string of length 10
def _generate_random_token():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
