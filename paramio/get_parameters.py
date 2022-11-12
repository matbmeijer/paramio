#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from typing import Any, Dict, List


def get_parameters(element: Any) -> Any:
    """
    It recursively traverses a dictionary, list, tuple or string, to identify any dynamic parameter
    defined with curly brackets e.g. ``{env}``

    Args:
        element (Any): Object from which to identify parameters

    Returns:
        An ordered list of the unique dynamic parameters in the object
    """

    parameters: List[str] = []

    if isinstance(element, dict):
        parameters += _get_parameters_dict(element)

    if isinstance(element, tuple):
        parameters += _get_parameters_tuple(element)

    if isinstance(element, list):
        parameters += _get_parameters_list(element)

    if isinstance(element, str):
        parameters += _get_parameters_str(element)

    return parameters


def _flatten(parameters: list) -> list:
    return [item for sublist in parameters for item in sublist]


def _ordered_unique(parameters: List[str]) -> List[str]:
    parameters_seen = set()
    parameters_seen_add = parameters_seen.add
    return [
        x for x in parameters if not (x in parameters_seen or parameters_seen_add(x))
    ]


def _get_parameters_dict(element: Dict[str, Any]) -> List[str]:
    parameters = _flatten([get_parameters(value) for value in element.values()])
    return _ordered_unique(parameters)


def _get_parameters_tuple(element: tuple) -> List[str]:
    parameters = _flatten([get_parameters(el) for el in element])
    return _ordered_unique(parameters)


def _get_parameters_list(element: List[Any]) -> List[str]:
    parameters = _flatten([get_parameters(el) for el in element])
    return _ordered_unique(parameters)


def _get_parameters_str(element: str) -> str:
    return re.findall(r"(?<={).*?(?=})", element)
