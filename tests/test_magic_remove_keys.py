from magiccionary.magic import remove_keys


def test_simple_one_non_existing_key():
    input = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    expected = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    actual = remove_keys(input, ["z"])

    assert actual == expected
    assert expected == input


def test_simple_one_non_existing_key_list():
    input = {
        "a": {
            "b": {
                "c": {
                    "d": 1,
                },
            },
        }
    }
    expected = {
        "a": {
            "b": {
                "c": {
                    "d": 1,
                },
            },
        }
    }
    actual = remove_keys(input, [["a", "c", "*", "z"]])

    assert actual == expected
    assert expected == input


def test_mixed_list():
    input = {
        "a": {
            "aa": {
                "one": [{"a": 1}, {"b": 2}],
                "two": 2,
            },
            "bb": {
                "one": 1,
                "two": 2,
            },
        },
        "b": {
            "bb": {
                "one": 1,
                "two": 2,
            },
        },
    }

    expected = {
        "a": {
            "aa": {
                "one": [{}, {"b": 2}],
                "two": 2,
            },
            "bb": {
                "two": 2,
            },
        },
    }
    actual = remove_keys(input, [["*", "*", "one", "[]", "a"], ["a", "bb", "one"], ["b"]])

    assert actual == expected
    assert expected == input


def test_mixed_removables_2():
    input = {
        "a": {
            "aa": {
                "one": [{"a": 1}, {"b": 2}],
                "two": 2,
            },
            "bb": {
                "one": 1,
                "two": 2,
            },
        },
        "b": {
            "bb": {
                "one": 1,
                "two": 2,
            },
        },
    }

    expected = {
        "a": {
            "aa": {
                "one": [{}, {"b": 2}],
                "two": 2,
            },
            "bb": {
                "one": 1,
                "two": 2,
            },
        },
        "b": {
            "bb": {
                "one": 1,
                "two": 2,
            },
        },
    }
    actual = remove_keys(input, [["*", "*", "one", "[]", "a"]])

    assert actual == expected
    assert expected == input


def test_mixed_removables():
    input = {
        "a": {
            "list": [
                {
                    "a": {
                        "one": 1,
                    },
                    "b": {
                        "one": 1,
                        "two": 2,
                    },
                },
                {
                    "a": {
                        "one": 1,
                    },
                    "d": {
                        "one": 1,
                        "two": 2,
                    },
                },
            ],
        }
    }

    expected = {
        "a": {
            "list": [
                {
                    "a": {},
                    "b": {
                        "two": 2,
                    },
                },
                {
                    "a": {},
                    "d": {
                        "two": 2,
                    },
                },
            ],
        }
    }
    actual = remove_keys(input, [["a", "list", "[]", "*", "one"]])

    assert actual == expected
    assert expected == input


def test_arbitrary_dict_keys():
    input = {
        "a": {
            "b1": {
                "hello": "world",
                "c": 1,
            },
            "b2": {
                "hello": "world",
                "c": 2,
            },
            "b3": {
                "hello": "world",
                "d": 2,
            },
        }
    }

    expected = {
        "a": {
            "b1": {"hello": "world"},
            "b2": {"hello": "world"},
            "b3": {"hello": "world", "d": 2},
        }
    }

    actual = remove_keys(input, [["a", "*", "c"]])

    assert actual == expected
    assert expected == input


def test_with_list_level():
    input = {
        "a": [
            {"b": 1},
            {"c": 2},
        ]
    }
    expected = {
        "a": [
            {"b": 1},
            {},
        ]
    }
    actual = remove_keys(input, [["a", "[]", "c"]])

    assert actual == expected
    assert expected == input


def test_simple_one_level():
    input = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    expected = {
        "a": 1,
        "b": 2,
    }
    actual = remove_keys(input, ["c"])

    assert actual == expected
    assert expected == input


def test_simple_two_level():
    input = {
        "a": {
            "b": 2,
            "c": 3,
        }
    }
    expected = {
        "a": {
            "b": 2,
        }
    }
    actual = remove_keys(input, [["a", "c"]])

    assert actual == expected
    assert expected == input


def test_simple_three_level():
    input = {
        "a": {
            "b": {
                "c": 3,
            }
        },
        "d": 4,
    }
    expected = {
        "a": {"b": {}},
        "d": 4,
    }
    actual = remove_keys(input, [["a", "b", "c"]])

    assert actual == expected
    assert expected == input