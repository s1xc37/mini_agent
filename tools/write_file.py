def write_file(data):
    path = data["file_path"]
    content = data["content"]

    with open(path, "w") as f:
        f.write(content)

    print(f"File written: {path}")