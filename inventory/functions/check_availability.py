import paramiko
import time
import os

from functions.clean_hostname import clean_hostname

def check_availability(ipv4):
    try:
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(ipv4, username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"), look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        time.sleep(2)
        output = remote_conn.recv(1000).decode("ascii")
        # Just to check,        
        print(output)
        return "Yes", clean_hostname(output) 

    except Exception as e:
        print(e)
        return "No", None
