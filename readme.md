# Magiccionary

A Python library for powerful dictionary and list manipulation with support for nested structures, wildcards, and complex path expressions.

## Features

- **Remove keys** from nested dictionaries and lists using dot notation or path arrays
- **Keep specific keys** while removing everything else
- **Wildcard support** (`*`) for operating on all dictionary keys
- **List traversal** (`[]`) for operating on all list items
- **Nested updates** for merging dictionary structures
- **Empty key removal** for cleaning up data structures

## Installation

```bash
pip install magiccionary
```

Or using uv:

```bash
uv add magiccionary
```

## Quick Start

```python
from magiccionary import remove_keys, keep_keys

# Sample data
data = {
    "user": {
        "profile": {
            "name": "John",
            "email": "john@example.com",
            "settings": {
                "theme": "dark",
                "notifications": True
            }
        },
        "posts": [
            {"title": "Post 1", "content": "Hello", "draft": True},
            {"title": "Post 2", "content": "World", "draft": False}
        ]
    }
}

# Remove specific keys
cleaned = remove_keys(data, [
    "user.profile.email",
    ["user", "posts", "[]", "draft"]
])

# Keep only specific keys
filtered = keep_keys(data, [
    "user.profile.name",
    ["user", "posts", "[]", "title"]
])
```

## API Reference

### `remove_keys(data, keys_to_remove, separator=".")`

Removes specified keys from a nested dictionary/list structure.

**Parameters:**

- `data` (dict/list): The data structure to filter
- `keys_to_remove` (list): List of keys to remove (strings or path arrays)
- `separator` (str): Separator for dot notation (default: ".")

**Returns:**

- A new data structure with specified keys removed

**Examples:**

```python
# Simple key removal
data = {"a": 1, "b": 2, "c": 3}
result = remove_keys(data, ["b", "c"])
# Result: {"a": 1}
# Original data unchanged: {"a": 1, "b": 2, "c": 3}

# Nested key removal
data = {"user": {"profile": {"name": "John", "email": "john@example.com"}}}
result = remove_keys(data, ["user.profile.email"])
# Result: {"user": {"profile": {"name": "John"}}}
# Original data unchanged

# Remove from all list items
data = {
    "posts": [
        {"title": "Post 1", "draft": True, "content": "Hello"},
        {"title": "Post 2", "draft": False, "content": "World"}
    ]
}
result = remove_keys(data, [["posts", "[]", "draft"]])
# Result: {"posts": [{"title": "Post 1", "content": "Hello"}, {"title": "Post 2", "content": "World"}]}
# Original data unchanged

# Wildcard removal (remove from all dictionary keys)
data = {
    "user1": {"name": "John", "email": "john@example.com"},
    "user2": {"name": "Jane", "email": "jane@example.com"}
}
result = remove_keys(data, [["*", "email"]])
# Result: {"user1": {"name": "John"}, "user2": {"name": "Jane"}}
# Original data unchanged
```

### `keep_keys(data, keys_to_keep, separator=".")`

Keeps only specified keys from a nested dictionary/list structure.

**Parameters:**

- `data` (dict/list): The data structure to filter
- `keys_to_keep` (list): List of keys to keep (strings or path arrays)
- `separator` (str): Separator for dot notation (default: ".")

**Returns:**

- New data structure with only specified keys

**Examples:**

```python
# Keep specific keys
data = {"a": 1, "b": 2, "c": 3}
result = keep_keys(data, ["a", "b"])
# Result: {"a": 1, "b": 2}

# Keep nested keys
data = {"user": {"profile": {"name": "John", "email": "john@example.com"}}}
result = keep_keys(data, ["user.profile.name"])
# Result: {"user": {"profile": {"name": "John"}}}

# Keep from all list items
data = {
    "posts": [
        {"title": "Post 1", "draft": True, "content": "Hello"},
        {"title": "Post 2", "draft": False, "content": "World"}
    ]
}
result = keep_keys(data, [["posts", "[]", "title"]])
# Result: {"posts": [{"title": "Post 1"}, {"title": "Post 2"}]}

# Wildcard keeping
data = {
    "user1": {"name": "John", "email": "john@example.com", "age": 30},
    "user2": {"name": "Jane", "email": "jane@example.com", "age": 25}
}
result = keep_keys(data, [["*", "name"]])
# Result: {"user1": {"name": "John"}, "user2": {"name": "Jane"}}
```

### `remove_empty_keys(data)`

Removes keys with empty values (None, empty dicts, empty strings) from a nested structure.

**Parameters:**

- `data` (dict): The dictionary to clean

**Returns:**

- A new dictionary with empty keys removed

**Examples:**

```python
data = {
    "name": "John",
    "email": None,
    "settings": {},
    "posts": [
        {"title": "Post 1", "content": ""},
        {"title": "Post 2", "content": "Hello"}
    ]
}
result = remove_empty_keys(data)
# Result: {
#     "name": "John",
#     "posts": [
#         {"title": "Post 1"},
#         {"title": "Post 2", "content": "Hello"}
#     ]
# }
# Original data unchanged
```

### `nested_update(original, update)`

Updates a nested dictionary with another dictionary, merging nested structures.

**Parameters:**

- `original` (dict): The original dictionary to update
- `update` (dict): The dictionary with updates to apply

**Returns:**

- A new dictionary with the merged data

**Examples:**

```python
original = {"user": {"name": "John", "settings": {"theme": "light"}}}
update = {"user": {"email": "john@example.com", "settings": {"notifications": True}}}
result = nested_update(original, update)
# Result: {
#     "user": {
#         "name": "John",
#         "email": "john@example.com",
#         "settings": {"theme": "light", "notifications": True}
#     }
# }
# Original data unchanged
```

## Path Syntax

Magiccionary supports two path formats:

### 1. Dot Notation (String)

Use dots to separate nested keys:

```python
"user.profile.name"  # Access user -> profile -> name
```

### 2. Path Arrays (List)

Use arrays for more complex operations:

```python
["user", "posts", "[]", "title"]  # Access user -> posts -> all items -> title
```

### Special Tokens

- `"*"` - Wildcard for all dictionary keys
- `"[]"` - Wildcard for all list items

### Complex Examples

```python
# Remove 'draft' field from all posts in all users
data = {
    "users": [
        {
            "name": "John",
            "posts": [{"title": "Post 1", "draft": True}, {"title": "Post 2", "draft": False}]
        },
        {
            "name": "Jane", 
            "posts": [{"title": "Post 3", "draft": True}]
        }
    ]
}

# Remove draft field from all posts in all users
result = remove_keys(data, [["users", "[]", "posts", "[]", "draft"]])

# Keep only names and post titles
result = keep_keys(data, [
    ["users", "[]", "name"],
    ["users", "[]", "posts", "[]", "title"]
])
```

## Advanced Usage

### Working with API Responses

```python
# Clean API response by removing unnecessary fields
api_response = {
    "data": {
        "users": [
            {
                "id": 1,
                "name": "John",
                "email": "john@example.com",
                "created_at": "2023-01-01",
                "updated_at": "2023-01-02",
                "internal_notes": "Some notes"
            }
        ]
    },
    "meta": {
        "pagination": {"page": 1, "total": 100},
        "debug_info": {"request_id": "abc123"}
    }
}

# Remove internal fields and keep only essential data
cleaned = remove_keys(api_response, [
    ["data", "users", "[]", "internal_notes"],
    ["data", "users", "[]", "created_at"],
    ["data", "users", "[]", "updated_at"],
    ["meta", "debug_info"]
])

# Or keep only specific fields
filtered = keep_keys(api_response, [
    ["data", "users", "[]", "name"],
    ["data", "users", "[]", "email"]
])
```

### Data Transformation

```python
# Transform complex nested data
complex_data = {
    "departments": {
        "engineering": {
            "employees": [
                {"name": "Alice", "role": "developer", "salary": 80000, "manager": "Bob"},
                {"name": "Charlie", "role": "designer", "salary": 75000, "manager": "Bob"}
            ]
        },
        "marketing": {
            "employees": [
                {"name": "Diana", "role": "manager", "salary": 90000, "manager": None}
            ]
        }
    }
}

# Create a flat list of employees with only name and role
employees = keep_keys(complex_data, [
    ["departments", "*", "employees", "[]", "name"],
    ["departments", "*", "employees", "[]", "role"]
])

# Remove salary information from all employees
result = remove_keys(complex_data, [
    ["departments", "*", "employees", "[]", "salary"]
])
```

## Development

### Setup

1. Clone the repository
2. Install dependencies:

   ```bash
   uv sync
   ```

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
uv run ruff check .
uv run ruff format .
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [license](license) file for details.
