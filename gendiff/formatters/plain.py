def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, path=""):
    lines = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]
        current_path = f"{path}.{key}" if path else key

        if node_type == "nested":
            lines.append(format_plain(node["children"], current_path))
        elif node_type == "added":
            val = to_str(node["value"])
            lines.append(
                f"Property '{current_path}' was added with value: {val}"
            )
        elif node_type == "removed":
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == "updated":
            val1 = to_str(node["value1"])
            val2 = to_str(node["value2"])
            lines.append(
                f"Property '{current_path}' was updated. From {val1} to {val2}"
            )

    return "\n".join(lines)