from typing import Any, Dict, List, Union

from paramio.get_parameters import get_parameters
from paramio.update_parameters import update_parameters


class Paramio:
    def __init__(self, **parameters) -> None:
        """
        Assigns the parameters to the class parameters attribute
        """
        self._parameters = parameters

    def parameterize(self, obj: Any) -> Any:
        """
        It takes an object and updates its dynamic parameters recursively with the parameters assigned to Paramio

        Args:
          obj (Any): The object to parameterize.

        Returns:
          The updated parameters.
        """
        return update_parameters(obj, **self._parameters)

    def add(self, **parameters) -> None:
        """
        This method takes in parameters and adds or updates the self._parameters dictionary depending if they exist or not
        """
        self._parameters.update(parameters)

    def delete(self, parameters: Union[List[str], str, Dict[str, str]]) -> None:
        if isinstance(parameters, str):
            parameters = [parameters]
        elif isinstance(parameters, dict):
            parameters = list(parameters.keys())

        for param in parameters:
            self._parameters.pop(param, None)

    def parameters(self):
        return self._parameters

    def missing_parameters(self, obj: Any) -> List[str]:
        av_parameters = get_parameters(obj)
        return [
            parameter
            for parameter in av_parameters
            if parameter not in self._parameters.keys()
        ]
