# Magiccionary

A Python utility package for powerful dictionary manipulation, allowing you to easily remove or keep specific keys in nested dictionaries.

## Installation

```bash
pip install magiccionary
```

## Features

- Deep dictionary manipulation
- Support for nested structures including lists and dictionaries
- Wildcard key matching using "*"
- List traversal using "[]" notation

## Usage

### Remove Keys

Remove specific keys from nested dictionaries while preserving the original structure:

```python
from magiccionary import remove_keys

# Simple key removal
data = {"a": 1, "b": 2, "c": 3}
result = remove_keys(data, ["c"])
# result = {"a": 1, "b": 2}

# Nested key removal
data = {
    "a": {
        "b": {
            "c": 3,
        }
    },
    "d": 4,
}
result = remove_keys(data, [["a", "b", "c"]])
# result = {"a": {"b": {}}, "d": 4}

# Using wildcards and list traversal
data = {
    "a": {
        "list": [
            {"x": 1, "y": 2},
            {"x": 3, "y": 4}
        ]
    }
}
result = remove_keys(data, [["a", "list", "[]", "x"]])
# result = {"a": {"list": [{"y": 2}, {"y": 4}]}}
```

### Keep Keys

Keep only specific keys in nested dictionaries:

```python
from magiccionary import keep_keys

# Simple key retention
data = {"a": 1, "b": 2, "c": 3}
result = keep_keys(data, ["a", "b"])
# result = {"a": 1, "b": 2}

# Nested key retention
data = {
    "a": {
        "b": 2,
        "c": 3,
    }
}
result = keep_keys(data, [["a", "b"]])
# result = {"a": {"b": 2}}
```

## Key Path Syntax

- Use strings for top-level keys: `["key_name"]`
- Use arrays for nested paths: `[["parent", "child", "grandchild"]]`
- Use `"*"` as a wildcard to match any key at that level
- Use `"[]"` to traverse list elements

## Features

- Non-destructive operations (original dictionaries are not modified)
- Support for deeply nested structures
- Wildcard key matching
- List traversal support
- Type-safe operations

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
