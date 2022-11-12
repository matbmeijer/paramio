#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any, Dict, List

from paramio.saveformatting import SaveFormatting


def update_parameters(element: Any, **parameters) -> Any:
    """
    It recursively traverses a dictionary, list, tuple or string, and replaces any string values with the
    string formatted using the `parameters` dictionary

    Args:
        element (Any): Object to dynamically update it's elements recursively
        parameters: Key-Values to update, defining the value as the new value to be

    Returns:
        A dictionary with the keys being the keys of the original dictionary and the values being the
    values of the original dictionary.
    """
    if isinstance(element, dict):
        return _update_parameters_dict(element, **parameters)

    if isinstance(element, tuple):
        return _update_parameters_tuple(element, **parameters)

    if isinstance(element, list):
        return _update_parameters_list(element, **parameters)

    if isinstance(element, str):
        return _update_parameters_str(element, **parameters)

    return element


def _update_parameters_dict(element: Dict[str, Any], **parameters) -> Dict[str, Any]:
    return {
        key: update_parameters(value, **parameters) for key, value in element.items()
    }


def _update_parameters_tuple(element: tuple, **parameters) -> tuple:
    return tuple(update_parameters(el, **parameters) for el in element)


def _update_parameters_list(element: List[Any], **parameters) -> List[Any]:
    return [update_parameters(el, **parameters) for el in element]


def _update_parameters_str(element: str, **parameters) -> str:
    return element.format_map(SaveFormatting(**parameters))
