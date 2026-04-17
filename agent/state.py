import json

def create_initial_state(role, content, is_json_format=True):
    # with open("prompts/system.txt", "r") as f:
    #     lines = f.readlines()
    if is_json_format:
        return [
            {
                "role": role,
                "content": json.dumps(content),
            }
        ]
    return [
        {
            "role": role,
            "content": "".join(content),
        }
    ]
