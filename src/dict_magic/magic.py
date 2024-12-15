
def _remove_keys(data, single_key_to_remove):
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
    for key in keys_to_remove:
        if isinstance(key, str):
            key = key.split(separator)
        _remove_keys(data, key)
    return data


def keep_keys(data, keys_to_keep, separator="."):
    dict_to_keep = {}
    for key in keys_to_keep:
        if isinstance(key, str):
            key = key.split(separator)
        keep = _keep_keys(data, key)
        nested_update(dict_to_keep, keep)
    return dict_to_keep


def _keep_keys(data, single_key_to_keep):
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
    elif first_key in data:
        if len(single_key_to_keep) == 1:
            dict_to_keep[first_key] = data[first_key]
        elif isinstance(data[first_key], dict):
            dict_to_keep[first_key] = _keep_keys(data[first_key], single_key_to_keep[1:])
        elif isinstance(data[first_key], list):
            dict_to_keep[first_key] = _keep_keys(data[first_key], single_key_to_keep[1:])
    return dict_to_keep

def remove_empty_keys(data):
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
    for key, value in update.items():
        if isinstance(value, dict) and key in original and isinstance(original[key], dict):
            nested_update(original[key], value)
        else:
            original[key] = value
    return original
