from abc import ABC, abstractmethod
from typing import Dict, Self


class Container(ABC):
    """Abstract base class for containers.

    Attributes:
        id (int): The unique identifier for the container.
        weight (float): The weight of the container.
    """

    def __init__(self, id: int, weight: float) -> None:
        """Initialize a Container instance.

        Args:
            id (int): The unique identifier for the container.
            weight (float): The weight of the container.
        """
        self.id = id
        self.weight = weight

    @abstractmethod
    def consumption(self) -> float:
        """Calculate the fuel consumption based on the container's weight.

        Returns:
            float: The fuel consumption of the container.
        """
        pass

    def __eq__(self, other: Self) -> bool:
        """Check for equality between two Container instances.

        Args:
            other (Self): The other container to compare against.

        Returns:
            bool: True if both containers have the same type and weight, False otherwise.
        """
        return (self.__class__.__name__ == other.__class__.__name__ and
                self.weight == other.weight)

    def to_dict(self) -> Dict:
        """Convert the Container instance to a dictionary representation.

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
        """Create a Container instance from a dictionary representation.

        Args:
            data (Dict): A dictionary containing container attributes.

        Returns:
            Container: A new Container instance populated with data from the dictionary.

        Raises:
            ValueError: If the container type is unknown.
        """
        if data["type"] == "BasicContainer":
            return BasicContainer(data['id'], data['weight'])
        elif data["type"] == "HeavyContainer":
            return HeavyContainer(data['id'], data['weight'])
        else:
            raise ValueError("Unknown container type")


class BasicContainer(Container):
    """Class representing a basic container.

    Inherits from the Container class and calculates fuel consumption
    based on a predefined unit consumption rate.
    """

    UNIT_CONSUMPTION = 2.5

    def __init__(self, id: int, weight: float) -> None:
        """Initialize a BasicContainer instance.

        Args:
            id (int): The unique identifier for the container.
            weight (float): The weight of the container.
        """
        super().__init__(id, weight)

    def consumption(self) -> float:
        """Calculate the fuel consumption for the basic container.

        Returns:
            float: The fuel consumption of the basic container.
        """
        return BasicContainer.UNIT_CONSUMPTION * self.weight


class HeavyContainer(Container):
    """Class representing a heavy container.

    Inherits from the Container class and calculates fuel consumption
    based on a predefined unit consumption rate.
    """

    UNIT_CONSUMPTION = 3.0

    def __init__(self, id: int, weight: float) -> None:
        """Initialize a HeavyContainer instance.

        Args:
            id (int): The unique identifier for the container.
            weight (float): The weight of the container.
        """
        super().__init__(id, weight)

    def consumption(self) -> float:
        """Calculate the fuel consumption for the heavy container.

        Returns:
            float: The fuel consumption of the heavy container.
        """
        return HeavyContainer.UNIT_CONSUMPTION * self.weight


def container_factory(id: int, weight: float) -> Container:
    """Factory function to create a container based on its weight.

    Args:
        id (int): The unique identifier for the container.
        weight (float): The weight of the container.

    Returns:
        Container: A BasicContainer or HeavyContainer instance based on the weight.
    """
    if weight <= 3000:
        return BasicContainer(id, weight)
    else:
        return HeavyContainer(id, weight)
