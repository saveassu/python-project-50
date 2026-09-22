import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    keys = sorted(data1.keys() | data2.keys())
    lines = []

    for key in keys:
        if key not in data1:
            lines.append(f"  + {key}: {to_str(data2[key])}")
        elif key not in data2:
            lines.append(f"  - {key}: {to_str(data1[key])}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {to_str(data1[key])}")
        else:
            lines.append(f"  - {key}: {to_str(data1[key])}")
            lines.append(f"  + {key}: {to_str(data2[key])}")

    result = "\n".join(lines)
    return f"{{\n{result}\n}}"


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)