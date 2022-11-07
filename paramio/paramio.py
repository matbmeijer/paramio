from typing import Any, List

from paramio.get_parameters import get_parameters
from paramio.update_parameters import update_parameters


class Paramio:
    def __init__(self, **parameters) -> None:
        """
        Assigns the parameters to the class parameters attribute
        """
        self.parameters = parameters

    def parameterize(self, obj: Any) -> Any:
        """
        It takes an object and updates its dynamic parameters recursively with the parameters assigned to Paramio

        Args:
          obj (Any): The object to parameterize.

        Returns:
          The updated parameters.
        """
        return update_parameters(obj, **self.parameters)

    def parameters(self) -> dict:
        return self.parameters

    def missing_parameters(self, obj: Any) -> List[str]:
        av_parameters = get_parameters(obj)
        return [
            parameter
            for parameter in av_parameters
            if parameter not in self.parameters.keys()
        ]
