# Store credentials in environment variables

# Import OS module
import os

def store_credentials(username, password):
    os.environ["USERNAME"] = username
    os.environ["PASSWORD"] = password