#############################################################################
#   This script reads a csv file with IPv4 information. 
#   Checks the format and validates the IPv4 are reachable.
#   Detects the vendor of the device.
#############################################################################

# Importing libraries

import os
import csv

import time
import paramiko
import pandas as pd
import getpass
#import sqlite3

# Import my functions
from functions.store_credentials import store_credentials
from functions.validate_ipv4 import validate_ipv4_addresses
from functions.process_devices import process_devices

"""
# Function to create an SQLite table with inventory data
def create_inventory_table(input_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        IPv4_Address TEXT PRIMARY KEY,
                        Reachable TEXT,
                        Vendor TEXT)''')

    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            ipv4 = row[0]
            reachable = check_availability(ipv4)
            vendor = "Unknown"
            if reachable == "Yes":
                try:
                    with paramiko.SSHClient() as ssh:
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(ipv4, username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
                        stdin, stdout, stderr = ssh.exec_command("show version")
                        output = stdout.read().decode()
                        vendor = determine_vendor(output)
                except Exception as e:
                    pass
            cursor.execute("INSERT INTO inventory VALUES (?, ?, ?)", (ipv4, reachable, vendor))
    
    conn.commit()
    conn.close()
"""

if __name__ == "__main__":
    
    # Ask for credentials (username, password) and stores them in OS environmental variales:
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    store_credentials(username, password)
    
    # Data files
    input_csv = "input.csv"
    output_csv = "output.csv"
    log_file = "logs.txt"
    # db_file = "inventory.db"

    # This funtion verifies that IPv4 are valid and are not repeted creating a new file
    validate_ipv4_addresses(input_csv, output_csv)

    # Process the new file of verified IP Addresses, and logs the results
    process_devices(output_csv, log_file)

    # create_inventory_table(output_csv, db_file)

"""
import paramiko
import time

ip = '1.1.1.16'
username = 'testuser'
password = 'password'

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()

time.sleep(2)

output = remote_conn.recv(1000)

print(output.decode("ascii"))

b'A:MXBCNTIJ8013GTMRTLD01# '

remote_conn.send("show version\n")

time.sleep(5)

output = remote_conn.recv(5000)

print(output.decode("ascii"))

b'show version \r\nTiMOS-B-22.10.R3 both/hops64 Nokia 7250 IXR Copyright (c) 2000-2023 Nokia.\r\r\nAll rights reserved. All use subject to applicable license agreements.\r\r\nBuilt on Wed Feb 15 17:27:20 PST 2023 by builder in /builds/c/2210B/R3/panos/main/sros\r\r\nA:MXBCNTIJ8013GTMRTLD01# '
"""
