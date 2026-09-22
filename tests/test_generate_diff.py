import os
import pytest
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


def read_file(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read().strip()


@pytest.mark.parametrize('file1_name, file2_name', [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml'),
])
def test_generate_diff_stylish(file1_name, file2_name):
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    expected = read_file('result_stylish.txt')

    assert generate_diff(file1, file2, 'stylish') == expected

@pytest.mark.parametrize("file1_name, file2_name", [
    ("file1.json", "file2.json"),
    ("file1.yml", "file2.yml"),
])
def test_generate_diff_plain(file1_name, file2_name):
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    expected = read_file("result_plain.txt")

    assert generate_diff(file1, file2, "plain") == expected