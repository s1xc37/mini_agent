from tools.registry import tools

def handle_action(parsed):
    action = parsed["action"]
    if action in tools:
        return tools[action](parsed)
    else:
        print("Invalid action: ", action)
