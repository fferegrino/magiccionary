"""
Magiccionary - A Python library for powerful dictionary and list manipulation.

This library provides utilities for manipulating nested dictionaries and lists
with support for wildcards, list traversal, and complex path expressions.

Main functions:
    - remove_keys: Remove specified keys from nested structures
    - keep_keys: Keep only specified keys from nested structures
    - remove_empty_keys: Remove keys with empty values
    - nested_update: Merge nested dictionaries
"""

from .magic import remove_keys, keep_keys, remove_empty_keys, nested_update  # noqa

__version__ = "0.1.4"

__all__ = ["remove_keys", "keep_keys", "remove_empty_keys", "nested_update"]
