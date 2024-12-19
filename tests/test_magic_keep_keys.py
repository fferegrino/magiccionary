from magiccionary.magic import keep_keys


def test_keep_multiple_ultra_nested():
    input = {
        "a": {
            "b": [
                {"c": {"d": 1, "e": [{"f": 1, "g": 2}]}, "d": 2, "e": 3},
                {"c": {"d": 1, "e": [{"f": 1, "g": 2}]}, "d": 2, "e": 3},
            ],
            "c": [
                {"c": {"d": 1, "e": [{"f": 1, "g": 2}]}, "d": 2, "e": 3},
                {"c": {"d": 1, "e": [{"f": 1, "g": 2}]}, "d": 2, "e": 3},
            ]
        },
    }

    expected = {
        "a": {
            "b": [
                {"c": {"d": 1, "e": [{"f": 1}]}, "d": 2},
                {"c": {"d": 1, "e": [{"f": 1}]}, "d": 2},
            ],
            "c": [
                {"c": {"d": 1, "e": [{"f": 1}]}, "d": 2},
                {"c": {"d": 1, "e": [{"f": 1}]}, "d": 2},
            ]
        }
    }
    actual = keep_keys(input, [
        ["a", "*", "[]", [["c", ["d", ["e", "[]", "f"]]], "d"]]
    ])

    assert actual == expected

def test_keep_multiple_in_dict():
    input = {
        "a": {
            "b": [
                {"c": 1, "d": 2, "e": 3},
                {"c": 1, "d": 2, "e": 3},
            ]
        },
    }

    expected = {
        "a": {
            "b": [
                {"c": 1, "d": 2},
                {"c": 1, "d": 2},
            ]
        }
    }
    actual = keep_keys(input, [["a", "b", "[]", ["c", "d"]]])

    assert actual == expected

def test_keep_mixed_list():
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
                "one": [{"a": 1}, {}],
            },
            "bb": {
                "one": 1,
            },
        },
        "b": {
            "bb": {
                "one": 1,
                "two": 2,
            },
        },
    }
    actual = keep_keys(input, [["*", "*", "one", "[]", "a"], ["a", "bb", "one"], ["b"]])

    assert actual == expected


def test_keep_arbitrary_dict_keys():
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
            "b1": {"c": 1},
            "b2": {"c": 2},
            "b3": {},
        }
    }

    actual = keep_keys(input, [["a", "*", "c"]])

    assert actual == expected


def test_keep_with_list_level():
    input = {
        "a": [
            {"b": 1},
            {"c": 2},
        ]
    }
    expected = {
        "a": [
            {},
            {"c": 2},
        ]
    }
    actual = keep_keys(input, [["a", "[]", "c"]])

    assert actual == expected


def test_keep_simple_two_level():
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
    actual = keep_keys(input, [["a", "b"]])

    assert actual == expected


def test_keep_simple_non_existing_key():
    input = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    input_copy = input.copy()
    expected = {}
    actual = keep_keys(input, ["x", "z"])

    assert actual == expected
    assert input == input_copy


def test_keep_simple():
    input = { "a": 1, "b": 2, "c": 3, }
    expected = { "a": 1, "b": 2, }
    input_copy = input.copy()
    
    actual = keep_keys(input, ["a", "b"])

    assert actual == expected
    assert input == input_copy


