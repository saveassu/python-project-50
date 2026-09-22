from gendiff.formatters import format_diff
from gendiff.parser import parse_file
from gendiff.tree import build_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    return format_diff(diff, format_name)