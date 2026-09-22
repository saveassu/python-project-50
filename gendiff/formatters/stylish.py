INDENT_CHAR = ' '
INDENT_SIZE = 4


def stringify(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if not isinstance(value, dict):
        return str(value)

    indent = INDENT_CHAR * (depth * INDENT_SIZE)
    lines = []
    for k, v in value.items():
        lines.append(f"{indent}    {k}: {stringify(v, depth + 1)}")

    result = "\n".join(lines)
    return f"{{\n{result}\n{indent}}}"


def format_stylish(diff, depth=1):
    indent = INDENT_CHAR * (depth * INDENT_SIZE - 2)
    lines = []

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}  {key}: {children}")
        elif node_type == 'added':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}+ {key}: {val}")
        elif node_type == 'removed':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}- {key}: {val}")
        elif node_type == 'unchanged':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}  {key}: {val}")
        elif node_type == 'updated':
            val1 = stringify(node['value1'], depth)
            val2 = stringify(node['value2'], depth)
            lines.append(f"{indent}- {key}: {val1}")
            lines.append(f"{indent}+ {key}: {val2}")

    result = "\n".join(lines)
    closing_indent = INDENT_CHAR * ((depth - 1) * INDENT_SIZE)
    return f"{{\n{result}\n{closing_indent}}}"