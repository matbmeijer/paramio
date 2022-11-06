from typing import Any

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
