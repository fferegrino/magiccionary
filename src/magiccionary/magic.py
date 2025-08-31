
def _remove_keys(data, single_key_to_remove):
    """
    Internal helper function to remove a single key path from data.
    
    Args:
        data: The data structure to modify (dict or list)
        single_key_to_remove: List representing the path to the key to remove
    """
    first_key = single_key_to_remove[0]
    if first_key == "[]" and isinstance(data, list):
        for item in data:
            _remove_keys(item, single_key_to_remove[1:])
    elif first_key == "*" and isinstance(data, dict):
        for key, value in data.items():
            _remove_keys(value, single_key_to_remove[1:])
    elif len(single_key_to_remove) == 1:
        data.pop(first_key, None)
    elif first_key in data:
        if isinstance(data[first_key], dict):
            _remove_keys(data[first_key], single_key_to_remove[1:])
        elif isinstance(data[first_key], list):
            _remove_keys(data[first_key], single_key_to_remove[1:])


def remove_keys(data, keys_to_remove, separator="."):
    """
    Remove specified keys from a nested dictionary/list structure.
    
    This function modifies the data in-place and supports:
    - Dot notation for simple paths (e.g., "user.profile.name")
    - Path arrays for complex operations (e.g., ["user", "posts", "[]", "title"])
    - Wildcards ("*") to operate on all dictionary keys
    - List traversal ("[]") to operate on all list items
    
    Args:
        data: The data structure to modify (dict or list)
        keys_to_remove: List of keys to remove. Can be strings (dot notation) or path arrays
        separator: Character used to separate keys in dot notation (default: ".")
    
    Returns:
        The modified data structure (same object, modified in-place)
    
    Examples:
        >>> data = {"a": 1, "b": 2, "c": 3}
        >>> remove_keys(data, ["b", "c"])
        {"a": 1}
        
        >>> data = {"user": {"profile": {"name": "John", "email": "john@example.com"}}}
        >>> remove_keys(data, ["user.profile.email"])
        {"user": {"profile": {"name": "John"}}}
        
        >>> data = {"posts": [{"title": "Post 1", "draft": True}, {"title": "Post 2", "draft": False}]}
        >>> remove_keys(data, [["posts", "[]", "draft"]])
        {"posts": [{"title": "Post 1"}, {"title": "Post 2"}]}
    """
    for key in keys_to_remove:
        if isinstance(key, str):
            key = key.split(separator)
        _remove_keys(data, key)
    return data


def keep_keys(data, keys_to_keep, separator="."):
    """
    Keep only specified keys from a nested dictionary/list structure.
    
    This function creates a new data structure containing only the specified keys.
    Supports the same path syntax as remove_keys().
    
    Args:
        data: The data structure to filter (dict or list)
        keys_to_keep: List of keys to keep. Can be strings (dot notation) or path arrays
        separator: Character used to separate keys in dot notation (default: ".")
    
    Returns:
        A new data structure containing only the specified keys
    
    Examples:
        >>> data = {"a": 1, "b": 2, "c": 3}
        >>> keep_keys(data, ["a", "b"])
        {"a": 1, "b": 2}
        
        >>> data = {"user": {"profile": {"name": "John", "email": "john@example.com"}}}
        >>> keep_keys(data, ["user.profile.name"])
        {"user": {"profile": {"name": "John"}}}
        
        >>> data = {"posts": [{"title": "Post 1", "draft": True}, {"title": "Post 2", "draft": False}]}
        >>> keep_keys(data, [["posts", "[]", "title"]])
        {"posts": [{"title": "Post 1"}, {"title": "Post 2"}]}
    """
    dict_to_keep = {}
    for key in keys_to_keep:
        if isinstance(key, str):
            key = key.split(separator)
        keep = _keep_keys(data, key)
        nested_update(dict_to_keep, keep)
    return dict_to_keep


def _keep_keys(data, single_key_to_keep):
    """
    Internal helper function to keep a single key path from data.
    
    Args:
        data: The data structure to filter (dict or list)
        single_key_to_keep: List representing the path to the key to keep
    
    Returns:
        Dictionary containing only the specified key path
    """
    dict_to_keep = {}
    first_key = single_key_to_keep[0]

    if first_key == "[]" and isinstance(data, list):
        list_to_keep = []
        for item in data:
            list_to_keep.append(_keep_keys(item, single_key_to_keep[1:]))
        # Return the list as is
        return list_to_keep
    elif first_key == "*" and isinstance(data, dict):
        for key, value in data.items():
            dict_to_keep[key] = _keep_keys(value, single_key_to_keep[1:])
        return dict_to_keep
    elif isinstance(first_key, list):
        if isinstance(data, dict):
            return keep_keys(data, first_key)
    elif first_key in data:
        if len(single_key_to_keep) == 1:
            dict_to_keep[first_key] = data[first_key]
        elif isinstance(data[first_key], dict):
            dict_to_keep[first_key] = _keep_keys(data[first_key], single_key_to_keep[1:])
        elif isinstance(data[first_key], list):
            dict_to_keep[first_key] = _keep_keys(data[first_key], single_key_to_keep[1:])
    return dict_to_keep

def remove_empty_keys(data):
    """
    Remove keys with empty values from a nested dictionary structure.
    
    This function removes keys that have None values, empty dictionaries, or empty strings.
    It modifies the data in-place.
    
    Args:
        data: The dictionary to clean
    
    Returns:
        The modified dictionary (same object, modified in-place)
    
    Examples:
        >>> data = {"name": "John", "email": None, "settings": {}, "posts": [{"title": "Post 1", "content": ""}]}
        >>> remove_empty_keys(data)
        {"name": "John", "posts": [{"title": "Post 1"}]}
    """
    empty_keys = []
    for key, value in data.items():
        if value is None:
            empty_keys.append(key)
        elif isinstance(value, dict):
            remove_empty_keys(value)
            if not value:
                empty_keys.append(key)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    remove_empty_keys(item)
                    if not item:
                        empty_keys.append(key)
                elif isinstance(item, str):
                    if not item:
                        empty_keys.append(key)
    for key in empty_keys:
        del data[key]
    return data



def nested_update(original, update):
    """
    Update a nested dictionary with another dictionary, merging nested structures.
    
    This function recursively merges the update dictionary into the original dictionary,
    preserving existing nested structures and adding new ones.
    
    Args:
        original: The original dictionary to update
        update: The dictionary with updates to apply
    
    Returns:
        The modified original dictionary (same object, modified in-place)
    
    Examples:
        >>> original = {"user": {"name": "John", "settings": {"theme": "light"}}}
        >>> update = {"user": {"email": "john@example.com", "settings": {"notifications": True}}}
        >>> nested_update(original, update)
        {
            "user": {
                "name": "John",
                "email": "john@example.com",
                "settings": {"theme": "light", "notifications": True}
            }
        }
    """
    for key, value in update.items():
        if isinstance(value, dict) and key in original and isinstance(original[key], dict):
            nested_update(original[key], value)
        else:
            original[key] = value
    return original
