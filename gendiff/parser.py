import json
import os

import yaml


def parse(data, format_name):
    if format_name in ('.json', 'json'):
        return json.loads(data)
    if format_name in ('.yaml', '.yml', 'yaml', 'yml'):
        return yaml.safe_load(data)
    raise ValueError(f"Unsupported format: {format_name}")


def parse_file(file_path):
    _, ext = os.path.splitext(file_path)
    with open(file_path) as f:
        content = f.read()
    return parse(content, ext.lower())