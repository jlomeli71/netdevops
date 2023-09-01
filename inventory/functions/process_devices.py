# Import libraries
import time
import csv
import paramiko
import os

from pprint import pprint

# Import funcions
from functions.check_availability import check_availability
from functions.determine_vendor import determine_vendor

# Function to process devices and create a log file
def process_devices(input_file, log_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # This is for skiping the header row
        header = next(csv_reader)
        print(f"Header: {header}")
        rows = list(csv_reader)
        print(type(rows))
        print(rows)
        
        print("Interrumpe aqui")

        for row in rows:
            if not row[0] == "IP Address":
                ipv4 = row[0]
                reachable, hostname = check_availability(ipv4)
                row.extend([reachable, hostname])
                vendor = "Unknown"
                output = None
                if reachable == "Yes":
                    try:
                        # Print IP Information
                        print("")
                        print("##########################################################")
                        print("##########################################################")
                        print(f"IPv4 address: {ipv4}")
                        remote_conn_pre=paramiko.SSHClient()
                        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        remote_conn_pre.connect(ipv4, username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"), look_for_keys=False, allow_agent=False)
                        remote_conn = remote_conn_pre.invoke_shell()
                        time.sleep(2)
                        output = remote_conn.recv(1000).decode("ascii")
                        try:                         
                            remote_conn.send("show version\n")
                            time.sleep(5)
                            output += remote_conn.recv(5000).decode("ascii")
                            vendor = determine_vendor(output)
                            # Temporal
                            print(f"show version: {output}")
                        except:                        
                            remote_conn.send("display version\n")
                            time.sleep(5)
                            output += remote_conn.recv(5000).decode("ascii")
                            vendor = determine_vendor(output)
                            # Temporal
                            print(f"display version: {output}")
                    except Exception as e:
                        # Print to check error type
                        print(e)
                        pass
                    log_message = f"IPv4: {ipv4}, Reachable: {reachable}, Vendor: {vendor}\n"
                    # log_message += f"Output: {output}\n"
                    with open(log_file, 'a') as log:
                        log.write(log_message)
        
        rows.insert(0, header)
        pprint(rows)

        with open("finalout.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
            