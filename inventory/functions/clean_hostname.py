
def clean_hostname(output):
    if ":" in output:
        index = output.index(":")
        output = output[index+1:]
    if "#" in output:
        index = output.index("#")
        output = output[:index]
    return output