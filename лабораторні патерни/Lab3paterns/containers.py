from abc import ABC, abstractmethod
from typing import Dict, Self


class Container(ABC):
    """Abstract base class for containers.

    Attributes:
        id (int): The unique identifier for the container.
        weight (float): The weight of the container.
    """

    def __init__(self, id: int, weight: float) -> None:
        """Initializes a Container instance.

        Args:
            id (int): The unique identifier for the container.
            weight (float): The weight of the container.
        """
        self.id = id
        self.weight = weight

    @abstractmethod
    def consumption(self) -> float:
        """Abstract method to calculate fuel consumption.

        This method must be implemented by subclasses to calculate fuel consumption
        based on container's type and weight.

        Returns:
            float: The fuel consumption of the container.
        """
        pass

    def __eq__(self, other: Self) -> bool:
        """Checks equality between two containers.

        Args:
            other (Self): The container to compare against.

        Returns:
            bool: True if both containers have the same type and weight, False otherwise.
        """
        return (self.__class__.__name__ == other.__class__.__name__ and
                self.weight == other.weight)

    def to_dict(self) -> Dict:
        """Converts the Container instance to a dictionary representation.

        Returns:
            Dict: A dictionary containing the container's attributes.
        """
        return {
            "type": self.__class__.__name__,
            "id": self.id,
            "weight": self.weight
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Container':
        """Creates a Container instance from a dictionary.

        Args:
            data (Dict): A dictionary containing container attributes.

        Returns:
            Container: A new Container instance based on the data provided.

        Raises:
            ValueError: If the container type is unknown.
        """
        if data["type"] == "BasicContainer":
            return BasicContainer(data['id'], data['weight'])
        elif data["type"] == "HeavyContainer":
            return HeavyContainer(data['id'], data['weight'])
        elif data["type"] == "RefrigeratedContainer":
            return RefrigeratedContainer(data['id'], data['weight'])
        elif data["type"] == "LiquidContainer":
            return LiquidContainer(data['id'], data['weight'])
        else:
            raise ValueError("Unknown container type")


class BasicContainer(Container):
    """Class representing a basic container.

    Attributes:
        UNIT_CONSUMPTION (float): Unit consumption rate for basic containers.
    """

    UNIT_CONSUMPTION = 2.5

    def consumption(self) -> float:
        """Calculates fuel consumption for basic containers.

        Returns:
            float: The fuel consumption of the basic container.
        """
        return BasicContainer.UNIT_CONSUMPTION * self.weight


class HeavyContainer(Container):
    """Class representing a heavy container.

    Attributes:
        UNIT_CONSUMPTION (float): Unit consumption rate for heavy containers.
    """

    UNIT_CONSUMPTION = 3.0

    def consumption(self) -> float:
        """Calculates fuel consumption for heavy containers.

        Returns:
            float: The fuel consumption of the heavy container.
        """
        return HeavyContainer.UNIT_CONSUMPTION * self.weight


class RefrigeratedContainer(Container):
    """Class representing a refrigerated container.

    Attributes:
        UNIT_CONSUMPTION (float): Unit consumption rate for refrigerated containers.
    """

    UNIT_CONSUMPTION = 3.5

    def consumption(self) -> float:
        """Calculates fuel consumption for refrigerated containers.

        Returns:
            float: The fuel consumption of the refrigerated container.
        """
        return RefrigeratedContainer.UNIT_CONSUMPTION * self.weight


class LiquidContainer(Container):
    """Class representing a liquid container.

    Attributes:
        UNIT_CONSUMPTION (float): Unit consumption rate for liquid containers.
    """

    UNIT_CONSUMPTION = 4.0

    def consumption(self) -> float:
        """Calculates fuel consumption for liquid containers.

        Returns:
            float: The fuel consumption of the liquid container.
        """
        return LiquidContainer.UNIT_CONSUMPTION * self.weight


def container_factory(id: int, weight: float, type_: str = 'basic') -> Container:
    """Factory function to create a container based on its weight and type.

    Args:
        id (int): The unique identifier for the container.
        weight (float): The weight of the container.
        type_ (str, optional): The type of the container ('basic', 'refrigerated', 'liquid'). Defaults to 'basic'.

    Returns:
        Container: An instance of a BasicContainer, HeavyContainer, RefrigeratedContainer, or LiquidContainer
        based on the provided weight and type.
    """
    if type_ == 'refrigerated':
        return RefrigeratedContainer(id, weight)
    elif type_ == 'liquid':
        return LiquidContainer(id, weight)
    elif weight <= 3000:
        return BasicContainer(id, weight)
    else:
        return HeavyContainer(id, weight)
