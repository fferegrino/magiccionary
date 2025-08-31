from magiccionary.magic import remove_keys, keep_keys, remove_empty_keys, nested_update


def test_remove_keys_non_destructive():
    """Test that remove_keys doesn't modify the original data."""
    original = {"a": 1, "b": 2, "c": 3}
    original_copy = original.copy()

    result = remove_keys(original, ["b", "c"])

    # Check that result is correct
    assert result == {"a": 1}
    # Check that original is unchanged
    assert original == original_copy
    # Check that result is a different object
    assert result is not original


def test_keep_keys_non_destructive():
    """Test that keep_keys doesn't modify the original data."""
    original = {"a": 1, "b": 2, "c": 3}
    original_copy = original.copy()

    result = keep_keys(original, ["a", "b"])

    # Check that result is correct
    assert result == {"a": 1, "b": 2}
    # Check that original is unchanged
    assert original == original_copy
    # Check that result is a different object
    assert result is not original


def test_remove_empty_keys_non_destructive():
    """Test that remove_empty_keys doesn't modify the original data."""
    original = {"a": 1, "b": None, "c": "", "d": {}}
    original_copy = original.copy()

    result = remove_empty_keys(original)

    # Check that result is correct
    assert result == {"a": 1}
    # Check that original is unchanged
    assert original == original_copy
    # Check that result is a different object
    assert result is not original


def test_nested_update_non_destructive():
    """Test that nested_update doesn't modify the original data."""
    original = {"user": {"name": "John", "settings": {"theme": "light"}}}
    update = {"user": {"email": "john@example.com", "settings": {"notifications": True}}}
    original_copy = original.copy()

    result = nested_update(original, update)

    # Check that result is correct
    expected = {
        "user": {"name": "John", "email": "john@example.com", "settings": {"theme": "light", "notifications": True}}
    }
    assert result == expected
    # Check that original is unchanged
    assert original == original_copy
    # Check that result is a different object
    assert result is not original


def test_nested_structures_preserved():
    """Test that nested structures are properly preserved."""
    original = {
        "users": [{"name": "John", "email": "john@example.com"}, {"name": "Jane", "email": "jane@example.com"}],
        "settings": {"theme": "dark"},
    }
    original_copy = {
        "users": [{"name": "John", "email": "john@example.com"}, {"name": "Jane", "email": "jane@example.com"}],
        "settings": {"theme": "dark"},
    }

    # Test remove_keys with nested structures
    result1 = remove_keys(original, [["users", "[]", "email"]])
    assert result1["users"][0] == {"name": "John"}
    assert result1["users"][1] == {"name": "Jane"}
    assert original == original_copy

    # Test keep_keys with nested structures
    result2 = keep_keys(original, [["users", "[]", "name"], ["settings", "theme"]])
    assert result2["users"][0] == {"name": "John"}
    assert result2["users"][1] == {"name": "Jane"}
    assert result2["settings"] == {"theme": "dark"}
    assert original == original_copy
