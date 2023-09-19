# This funtion returns input_file, output_file, log_file
# The input text file contains a list of IP address to verify
# The output csv file contains information about IP address, reachability, vendor and os system.
# The session log file contains information for troubleshooting purposes.

# Import OS moduleS
# import os

def get_file_names():
    # Get file names
    # This funtion returns input_file, output_file, log_file
    # print("Current working directory:")
    # print(os.getcwd())

    print("The input text file contains a list of IP address to verify")
    input_file = input("Enter input text file or Enter (inventory.txt):")
    if input_file == "":
        input_file = "inventory.txt"
    print("")
    print("The output csv file contains information about IP address, reachability, vendor and os system.")
    output_file = input("Enter output csv file or Enter (output.csv):")
    if output_file == "":
        output_file = "output.csv"
    print("")
    print("The session log file contains information for troubleshooting purposes.")
    log_file = input("Enter session log file or Enter (sesion.log):")
    if log_file == "":
        log_file = "session.log"
    print("")
    return input_file, output_file, log_file
