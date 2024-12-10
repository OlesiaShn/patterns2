from containers import Container
from typing import List, Dict
from typing import Protocol

class IShip(Protocol):
    """Interface for ship operations.

    This interface defines the methods that any ship class must implement
    to load and unload containers.
    """
    def load_container(self, container: Container) -> None:
        """Load a container into the ship.

        Args:
            container (Container): The container to be loaded into the ship.
        """
        pass

    def unload_container(self, container: Container) -> None:
        """Unload a container from the ship.

        Args:
            container (Container): The container to be unloaded from the ship.
        """
        pass

class Ship:
    """Class representing a ship.

    Attributes:
        id (int): The unique identifier of the ship.
        max_weight (float): The maximum weight capacity of the ship.
        containers (List[Container]): A list of containers currently loaded on the ship.
    """

    def __init__(self, id: int, max_weight: float) -> None:
        """Initialize a Ship instance.

        Args:
            id (int): The unique identifier of the ship.
            max_weight (float): The maximum weight capacity of the ship.
        """
        self.id = id
        self.max_weight = max_weight
        self.containers: List[Container] = []

    def load_container(self, container: Container) -> None:
        """Load a container into the ship.

        Args:
            container (Container): The container to be loaded.

        Prints:
            A message indicating whether the container was loaded or if
            it exceeds the weight limit.
        """
        total_weight = sum(c.weight for c in self.containers) + container.weight
        if total_weight <= self.max_weight:
            self.containers.append(container)
            print(f"Container {container.id} loaded into Ship {self.id}.")
        else:
            print(f"Cannot load container {container.id} into Ship {self.id}: exceeds weight limit.")

    def unload_container(self, container: Container) -> None:
        """Unload a container from the ship.

        Args:
            container (Container): The container to be unloaded.

        Prints:
            A message indicating whether the container was successfully unloaded
            or if it was not found on the ship.
        """
        if container in self.containers:
            self.containers.remove(container)
            print(f"Container {container.id} unloaded from Ship {self.id}.")
        else:
            print(f"Container {container.id} not found on Ship {self.id}.")

    def total_consumption(self) -> float:
        """Calculate the total fuel consumption of the ship.

        Returns:
            float: The total fuel consumption based on the containers on board.
        """
        return sum(container.consumption() for container in self.containers)

    def to_dict(self) -> Dict:
        """Convert the Ship instance to a dictionary representation.

        Returns:
            Dict: A dictionary containing the ship's attributes.
        """
        return {
            "id": self.id,
            "max_weight": self.max_weight,
            "containers": [container.to_dict() for container in self.containers]
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Ship':
        """Create a Ship instance from a dictionary representation.

        Args:
            data (Dict): A dictionary containing ship attributes.

        Returns:
            Ship: A new Ship instance populated with data from the dictionary.
        """
        ship = Ship(data['id'], data['max_weight'])
        ship.containers = [Container.from_dict(c) for c in data['containers']]
        return ship
