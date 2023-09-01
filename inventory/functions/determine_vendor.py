# Function to determine the vendor based on device output
def determine_vendor(output):
    if "Nokia" in output or "TiMOS" in output:
        return "Nokia"
    elif "IOS-XR" in output:
        return "Cisco IOS-XR"
    elif "IOS" in output:
        return "Cisco IOS"
    elif "Junos" in output:
        return "Juniper"
    elif "Huawei" in output:
        return "Huawei"
    else:
        return "Unknown"