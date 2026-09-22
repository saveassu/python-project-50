import os
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


def read_file(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read().strip()


def test_generate_diff_flat_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file('result_flat.txt')

    assert generate_diff(file1, file2) == expected