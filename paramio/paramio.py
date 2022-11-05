from typing import Any, Dict, List

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
        return _update_config_dict(element, **update_keys)

    if isinstance(element, list):
        return _update_config_list(element, **update_keys)

    if isinstance(element, str):
        return _update_config_str(element, **update_keys)

    return element


def _update_config_dict(element: Dict[str, Any], **update_keys):
    return {key: update_config(value, **update_keys) for key, value in element.items()}


def _update_config_list(element: List[Any], **update_keys):
    return [update_config(el, **update_keys) for el in element]


def _update_config_str(element: str, **update_keys):
    return element.format_map(SaveFormatting(**update_keys))
