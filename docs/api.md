# API Reference

This document provides detailed information about all public functions in the Magiccionary library.

## Core Functions

### `remove_keys(data, keys_to_remove, separator=".")`

Removes specified keys from a nested dictionary/list structure. This function creates a new data structure.

**Signature:**

```python
def remove_keys(data: Union[dict, list], keys_to_remove: List[Union[str, List[str]]], separator: str = ".") -> Union[dict, list]
```

**Parameters:**

- `data` (dict or list): The data structure to filter
- `keys_to_remove` (list): List of keys to remove. Can contain:
  - Strings using dot notation (e.g., "user.profile.name")
  - Path arrays (e.g., ["user", "profile", "name"])
- `separator` (str, optional): Character used to separate keys in dot notation. Defaults to "."

**Returns:**

- A new data structure with specified keys removed

**Examples:**

```python
from magiccionary import remove_keys

# Simple key removal
data = {"a": 1, "b": 2, "c": 3}
result = remove_keys(data, ["b", "c"])
# result is {"a": 1}
# data is unchanged: {"a": 1, "b": 2, "c": 3}

# Nested key removal with dot notation
data = {"user": {"profile": {"name": "John", "email": "john@example.com"}}}
result = remove_keys(data, ["user.profile.email"])
# result is {"user": {"profile": {"name": "John"}}}
# data is unchanged

# Remove from all list items
data = {
    "posts": [
        {"title": "Post 1", "draft": True, "content": "Hello"},
        {"title": "Post 2", "draft": False, "content": "World"}
    ]
}
result = remove_keys(data, [["posts", "[]", "draft"]])
# result is {"posts": [{"title": "Post 1", "content": "Hello"}, {"title": "Post 2", "content": "World"}]}
# data is unchanged

# Wildcard removal (remove from all dictionary keys)
data = {
    "user1": {"name": "John", "email": "john@example.com"},
    "user2": {"name": "Jane", "email": "jane@example.com"}
}
result = remove_keys(data, [["*", "email"]])
# result is {"user1": {"name": "John"}, "user2": {"name": "Jane"}}
# data is unchanged
```

### `keep_keys(data, keys_to_keep, separator=".")`

Keeps only specified keys from a nested dictionary/list structure. This function creates a new data structure.

**Signature:**
```python
def keep_keys(data: Union[dict, list], keys_to_keep: List[Union[str, List[str]]], separator: str = ".") -> Union[dict, list]
```

**Parameters:**

- `data` (dict or list): The data structure to filter
- `keys_to_keep` (list): List of keys to keep. Can contain:
  - Strings using dot notation (e.g., "user.profile.name")
  - Path arrays (e.g., ["user", "profile", "name"])
- `separator` (str, optional): Character used to separate keys in dot notation. Defaults to "."

**Returns:**

- A new data structure containing only the specified keys

**Examples:**

```python
from magiccionary import keep_keys

# Keep specific keys
data = {"a": 1, "b": 2, "c": 3}
result = keep_keys(data, ["a", "b"])
# result is {"a": 1, "b": 2}

# Keep nested keys with dot notation
data = {"user": {"profile": {"name": "John", "email": "john@example.com"}}}
result = keep_keys(data, ["user.profile.name"])
# result is {"user": {"profile": {"name": "John"}}}

# Keep from all list items
data = {
    "posts": [
        {"title": "Post 1", "draft": True, "content": "Hello"},
        {"title": "Post 2", "draft": False, "content": "World"}
    ]
}
result = keep_keys(data, [["posts", "[]", "title"]])
# result is {"posts": [{"title": "Post 1"}, {"title": "Post 2"}]}

# Wildcard keeping
data = {
    "user1": {"name": "John", "email": "john@example.com", "age": 30},
    "user2": {"name": "Jane", "email": "jane@example.com", "age": 25}
}
result = keep_keys(data, [["*", "name"]])
# result is {"user1": {"name": "John"}, "user2": {"name": "Jane"}}
```

### `remove_empty_keys(data)`

Removes keys with empty values from a nested dictionary structure. This function creates a new dictionary.

**Signature:**

```python
def remove_empty_keys(data: dict) -> dict
```

**Parameters:**

- `data` (dict): The dictionary to clean

**Returns:**

- A new dictionary with empty keys removed

**Empty values that are removed:**

- `None` values
- Empty dictionaries `{}`
- Empty strings `""`
- Empty lists `[]` (in nested structures)

**Examples:**

```python
from magiccionary import remove_empty_keys

# Remove empty values
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
# result is {
#     "name": "John",
#     "posts": [
#         {"title": "Post 1"},
#         {"title": "Post 2", "content": "Hello"}
#     ]
# }
# data is unchanged
```

### `nested_update(original, update)`

Updates a nested dictionary with another dictionary, merging nested structures. This function creates a new dictionary.

**Signature:**

```python
def nested_update(original: dict, update: dict) -> dict
```

**Parameters:**

- `original` (dict): The original dictionary to update
- `update` (dict): The dictionary with updates to apply

**Returns:**

- A new dictionary with the merged data

**Examples:**

```python
from magiccionary import nested_update

# Merge nested dictionaries
original = {"user": {"name": "John", "settings": {"theme": "light"}}}
update = {"user": {"email": "john@example.com", "settings": {"notifications": True}}}
result = nested_update(original, update)
# result is {
#     "user": {
#         "name": "John",
#         "email": "john@example.com",
#         "settings": {"theme": "light", "notifications": True}
#     }
# }
# original is unchanged

# Add new nested structures
original = {"user": {"name": "John"}}
update = {"user": {"profile": {"age": 30, "city": "New York"}}}
result = nested_update(original, update)
# result is {
#     "user": {
#         "name": "John",
#         "profile": {"age": 30, "city": "New York"}
#     }
# }
# original is unchanged
```

## Path Syntax

Magiccionary supports two path formats for specifying keys in nested structures:

### 1. Dot Notation (String)

Use dots to separate nested keys:
```python
"user.profile.name"  # Access user -> profile -> name
"posts.0.title"      # Access posts -> first item -> title
"settings.theme"     # Access settings -> theme
```

### 2. Path Arrays (List)

Use arrays for more complex operations:

```python
["user", "posts", "[]", "title"]  # Access user -> posts -> all items -> title
["*", "name"]                     # Access all top-level keys -> name
["users", "[]", "profile", "email"]  # Access users -> all items -> profile -> email
```

### Special Tokens

- `"*"` - Wildcard for all dictionary keys at that level
- `"[]"` - Wildcard for all list items at that level

### Complex Path Examples

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
remove_keys(data, [["users", "[]", "posts", "[]", "draft"]])

# Keep only names and post titles
result = keep_keys(data, [
    ["users", "[]", "name"],
    ["users", "[]", "posts", "[]", "title"]
])
```

## Error Handling

The library is designed to be forgiving and handles various edge cases gracefully:

- **Non-existent keys**: Functions silently ignore keys that don't exist
- **Type mismatches**: Functions handle cases where expected types don't match (e.g., accessing a list key in a dictionary)
- **Empty structures**: Functions handle empty dictionaries and lists appropriately

## Performance Considerations

- All functions create new data structures using `copy.deepcopy()` for safety
- This approach uses more memory but ensures data integrity and prevents accidental modifications
- Complex nested operations with wildcards may have O(n) complexity where n is the number of items being processed
- For very large datasets, consider processing in chunks or using more specific paths to avoid unnecessary iterations
