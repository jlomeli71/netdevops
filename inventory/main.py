#############################################################################
#   This script reads a file with IPv4 information. 
#   1.- Checks the format is a valid IP address
#   2.- Validates the IPv4 are reachable.
#   3.- Detects the vendor of the device.
#############################################################################

# Importing libraries
import os
import csv

import time
import paramiko
import pandas as pd

# Import my functions
from functions.get_credentials import get_credentials_3g
from functions.validate_ipv4 import validate_ipv4_addresses
from functions.process_devices import process_devices
from functions.get_file_names import get_file_names


if __name__ == "__main__":
    # Get credentials
    username, password = get_credentials_3g()
    # print(username, password)
    
    # Data files names
    input_file, output_file, log_file = get_file_names()
    print(input_file, output_file, log_file)

    valid_ipv4_list = validate_ipv4_addresses(input_file)
    # print(valid_ipv4_list)

    # Process the new file of verified IP Addresses, and logs the results
    process_devices(valid_ipv4_list, log_file)

    # create_inventory_table(output_csv, db_file)
    