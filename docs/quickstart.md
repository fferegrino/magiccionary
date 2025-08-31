# Quick Start Guide

This guide will help you get started with Magiccionary in just a few minutes.

## Installation

```bash
pip install magiccionary
```

## Basic Usage

### 1. Remove Keys from Dictionaries

```python
from magiccionary import remove_keys

# Simple example
data = {"name": "John", "email": "john@example.com", "age": 30}
result = remove_keys(data, ["email", "age"])
print(result)  # {"name": "John"}
print(data)    # {"name": "John", "email": "john@example.com", "age": 30} (unchanged)

# Nested example
user_data = {
    "user": {
        "profile": {
            "name": "John",
            "email": "john@example.com",
            "phone": "123-456-7890"
        },
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    }
}

result = remove_keys(user_data, ["user.profile.email", "user.profile.phone"])
print(result)
# Output:
# {
#     "user": {
#         "profile": {"name": "John"},
#         "settings": {"theme": "dark", "notifications": True}
#     }
# }
```

### 2. Keep Only Specific Keys

```python
from magiccionary import keep_keys

# Simple example
data = {"name": "John", "email": "john@example.com", "age": 30, "city": "NYC"}
result = keep_keys(data, ["name", "email"])
print(result)  # {"name": "John", "email": "john@example.com"}

# Nested example
user_data = {
    "user": {
        "profile": {
            "name": "John",
            "email": "john@example.com",
            "phone": "123-456-7890"
        },
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    }
}

result = keep_keys(user_data, ["user.profile.name", "user.settings.theme"])
print(result)
# Output:
# {
#     "user": {
#         "profile": {"name": "John"},
#         "settings": {"theme": "dark"}
#     }
# }
```

### 3. Working with Lists

```python
from magiccionary import remove_keys, keep_keys

# Remove fields from all items in a list
posts = [
    {"title": "Post 1", "content": "Hello", "draft": True, "author": "John"},
    {"title": "Post 2", "content": "World", "draft": False, "author": "Jane"}
]

result = remove_keys(posts, [["[]", "draft"], ["[]", "author"]])
print(result)
# Output:
# [
#     {"title": "Post 1", "content": "Hello"},
#     {"title": "Post 2", "content": "World"}
# ]

# Keep only specific fields from all items
result = keep_keys(posts, [["[]", "title"]])
print(result)
# Output:
# [
#     {"title": "Post 1"},
#     {"title": "Post 2"}
# ]
```

### 4. Using Wildcards

```python
from magiccionary import remove_keys, keep_keys

# Remove a field from all users
users = {
    "user1": {"name": "John", "email": "john@example.com", "age": 30},
    "user2": {"name": "Jane", "email": "jane@example.com", "age": 25},
    "user3": {"name": "Bob", "email": "bob@example.com", "age": 35}
}

result = remove_keys(users, [["*", "email"]])
print(result)
# Output:
# {
#     "user1": {"name": "John", "age": 30},
#     "user2": {"name": "Jane", "age": 25},
#     "user3": {"name": "Bob", "age": 35}
# }

# Keep only names from all users
result = keep_keys(users, [["*", "name"]])
print(result)
# Output:
# {
#     "user1": {"name": "John"},
#     "user2": {"name": "Jane"},
#     "user3": {"name": "Bob"}
# }
```

### 5. Clean Up Empty Values

```python
from magiccionary import remove_empty_keys

data = {
    "name": "John",
    "email": None,
    "phone": "",
    "settings": {},
    "posts": [
        {"title": "Post 1", "content": ""},
        {"title": "Post 2", "content": "Hello"}
    ]
}

result = remove_empty_keys(data)
print(result)
# Output:
# {
#     "name": "John",
#     "posts": [
#         {"title": "Post 1"},
#         {"title": "Post 2", "content": "Hello"}
#     ]
# }
```

### 6. Merge Dictionaries

```python
from magiccionary import nested_update

original = {"user": {"name": "John", "settings": {"theme": "light"}}}
update = {"user": {"email": "john@example.com", "settings": {"notifications": True}}}

result = nested_update(original, update)
print(result)
# Output:
# {
#     "user": {
#         "name": "John",
#         "email": "john@example.com",
#         "settings": {"theme": "light", "notifications": True}
#     }
# }
```

## Common Patterns

### API Response Cleaning

```python
from magiccionary import remove_keys, keep_keys

# Clean API response
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

# Remove internal fields
cleaned = remove_keys(api_response, [
    ["data", "users", "[]", "internal_notes"],
    ["data", "users", "[]", "created_at"],
    ["data", "users", "[]", "updated_at"],
    ["meta", "debug_info"]
])

# Or keep only specific fields
public_data = keep_keys(api_response, [
    ["data", "users", "[]", "name"],
    ["data", "users", "[]", "email"]
])
```

### Data Transformation

```python
from magiccionary import keep_keys

# Transform complex data
company_data = {
    "departments": {
        "engineering": {
            "employees": [
                {"name": "Alice", "role": "developer", "salary": 80000},
                {"name": "Bob", "role": "designer", "salary": 75000}
            ]
        },
        "marketing": {
            "employees": [
                {"name": "Charlie", "role": "manager", "salary": 90000}
            ]
        }
    }
}

# Create a simple employee list
employees = keep_keys(company_data, [
    ["departments", "*", "employees", "[]", "name"],
    ["departments", "*", "employees", "[]", "role"]
])
```

## Next Steps

- Read the [API Reference](api.md) for detailed function documentation
- Check out the [readme](../readme.md) for more examples and advanced usage
- Explore the test files for additional examples of complex operations

## Tips

1. **Use dot notation** for simple nested paths: `"user.profile.name"`
2. **Use path arrays** for complex operations: `["users", "[]", "posts", "[]", "title"]`
3. **Use wildcards** (`*`) to operate on all dictionary keys
4. **Use list traversal** (`[]`) to operate on all list items
5. **All functions create new data structures** - original data is always preserved
6. **Use `copy.deepcopy()` internally** - ensures complete independence from original data
