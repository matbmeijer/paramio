from typing import Any

from paramio.saveformatting import SaveFormatting


def update_config(element: Any, **update_keys) -> Any:
    """
    It recursively traverses a dictionary, list, or string, and replaces any string values with the
    string formatted using the `update_keys` dictionary

    Args:
      element (Any): Object to dynamically update it's elements recursively
      update_keys: Key-Values to update, defining the value as the new value to be

    Returns:
      A dictionary with the keys being the keys of the original dictionary and the values being the
    values of the original dictionary.
    """
    if isinstance(element, dict):
        return {
            key: update_config(value, **update_keys) for key, value in element.items()
        }

    if isinstance(element, list):
        return [update_config(el, **update_keys) for el in element]

    if isinstance(element, str):
        return element.format_map(SaveFormatting(**update_keys))

    return element
