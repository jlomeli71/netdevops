import socket
import csv

# Function to read and validate IPv4 addresses from a CSV file
def validate_ipv4_addresses(input_file, output_file):
    unique_ipv4_addresses = set()
    valid_ipv4_addresses = []

    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            ipv4 = row[0]
            if validate_ipv4(ipv4) and ipv4 not in unique_ipv4_addresses:
                valid_ipv4_addresses.append([ipv4])
                unique_ipv4_addresses.add(ipv4)

    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header
        csv_writer.writerow(["IPv4 Address", "Availability", "Hostname"])
        # Write the rest of the IPv4 address after validation
        print(f"Writing {len(valid_ipv4_addresses)} IPv4 address after validation")
        csv_writer.writerows(valid_ipv4_addresses)

# Function to validate the format of an IPv4 address
def validate_ipv4(ipv4):
    try:
        socket.inet_aton(ipv4)
        return True
    except socket.error:
        return False