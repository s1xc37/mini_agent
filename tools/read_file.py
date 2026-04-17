def read_file(data):
    file_path = data["file_path"]
    with open(file_path, "r") as f:
        lines = f.readlines()
    r_data = {
        "role": "assistant",
        "content": f"File - {file_path} contains: {lines}",
    }
    return r_data
