def read_file(data):
    file_path = data["file_path"]
    lines = open(file_path, "r").readlines()
    r_data = {
        "role": "assistant",
        "content": f"File - {file_path} contains: {lines}",
    }
    return r_data
