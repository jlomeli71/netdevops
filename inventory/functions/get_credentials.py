# Get credentials from environment variables

# Import OS module
import os
from dotenv import load_dotenv
# take environment variables from .env file
load_dotenv()  


def get_credentials_3g():
    # User credentials for users in VPN 3G
    ssh_user = os.getenv("SSH_USER_3G")
    ssh_pass = os.getenv("SSH_PASS_3G")
    return ssh_user, ssh_pass


def get_credentials_imp():
    #User credentials for users in implementation fase
    imp_user = os.getenv("SSH_USER_IMP")
    imp_pass = os.getenv("SSH_PASS_IMP")
    return imp_user, imp_pass

# username, password = get_credentials_3g()
# print(username, password)

