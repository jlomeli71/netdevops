import socket
import csv

def validate_ipv4(ipv4):
    try:
        socket.inet_aton(ipv4)
        return True
    except socket.error:
        return False

# Function to read and validate IPv4 addresses from a CSV file
def validate_ipv4_addresses(input_file):
    unique_ipv4_addresses = set()
    valid_ipv4_addresses = []
    with open(input_file, 'r') as file:
        ipv4s = file.read().splitlines()
        for ipv4 in ipv4s:
            if validate_ipv4(ipv4) and ipv4 not in unique_ipv4_addresses:
                valid_ipv4_addresses.append(ipv4)
                unique_ipv4_addresses.add(ipv4)

    return valid_ipv4_addresses