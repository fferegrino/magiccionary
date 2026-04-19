from copy import deepcopy

from magiccionary import remove_empty_keys


def test_prunes_empty_dict_items_in_list_without_losing_neighbours():
    # Previously the entire "posts" list was deleted because one item
    # became empty. It should keep the non-empty post.
    input = {"posts": [{"title": ""}, {"title": "B"}]}
    input_copy = deepcopy(input)
    expected = {"posts": [{"title": "B"}]}

    actual = remove_empty_keys(input)

    assert actual == expected
    assert input == input_copy


def test_prunes_nested_empty_items_keeps_populated_items():
    input = {
        "posts": [
            {"nested": {}},
            {"title": "B", "content": "C"},
        ]
    }
    input_copy = deepcopy(input)
    expected = {"posts": [{"title": "B", "content": "C"}]}

    actual = remove_empty_keys(input)

    assert actual == expected
    assert input == input_copy


def test_readme_example():
    input = {
        "name": "John",
        "email": None,
        "settings": {},
        "posts": [
            {"title": "Post 1", "content": ""},
            {"title": "Post 2", "content": "Hello"},
        ],
    }
    input_copy = deepcopy(input)
    expected = {
        "name": "John",
        "posts": [
            {"title": "Post 1"},
            {"title": "Post 2", "content": "Hello"},
        ],
    }

    actual = remove_empty_keys(input)

    assert actual == expected
    assert input == input_copy


def test_removes_key_whose_value_is_empty_list():
    input = {"a": [], "b": 1}
    expected = {"b": 1}

    actual = remove_empty_keys(input)

    assert actual == expected


def test_removes_key_whose_list_becomes_empty_after_pruning():
    input = {"a": [None, "", {}], "b": 1}
    expected = {"b": 1}

    actual = remove_empty_keys(input)

    assert actual == expected


def test_prunes_empty_strings_and_nones_from_lists():
    input = {"tags": ["x", None, "", "y"]}
    expected = {"tags": ["x", "y"]}

    actual = remove_empty_keys(input)

    assert actual == expected


def test_prunes_nested_lists():
    input = {"matrix": [[1, 2], [], [None, ""], [3]]}
    expected = {"matrix": [[1, 2], [3]]}

    actual = remove_empty_keys(input)

    assert actual == expected


def test_preserves_falsy_non_empty_values():
    # False and 0 are not in the "empty" set defined by the docstring.
    input = {"flag": False, "count": 0, "empty_str": ""}
    expected = {"flag": False, "count": 0}

    actual = remove_empty_keys(input)

    assert actual == expected
