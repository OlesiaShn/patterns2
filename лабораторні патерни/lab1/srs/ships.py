from containers import Container
from typing import List, Dict

class IShip:
    """
    Interface for all ships, defining the required methods for ship functionality.
    """

    def load_container(self, container: Container) -> None:
        raise NotImplementedError

    def unload_container(self, container: Container) -> None:
        raise NotImplementedError

    def total_consumption(self) -> float:
        raise NotImplementedError

class Ship(IShip):
    """
    Ship class responsible for main operations with containers, such as loading and unloading.
    """

    def __init__(self, id: int, max_weight: float) -> None:
        self.id = id
        self.max_weight = max_weight
        self.containers: List[Container] = []

    def load_container(self, container: Container) -> None:
        """
        Load a container onto the ship.
        """
        total_weight = sum(c.weight for c in self.containers) + container.weight
        if total_weight <= self.max_weight:
            self.containers.append(container)
            print(f"Container {container.id} loaded onto Ship {self.id}.")
        else:
            print(f"Cannot load container {container.id} onto Ship {self.id}: exceeds weight limit.")

    def unload_container(self, container: Container) -> None:
        """
        Unload a container from the ship.
        """
        if container in self.containers:
            self.containers.remove(container)
            print(f"Container {container.id} unloaded from Ship {self.id}.")
        else:
            print(f"Container {container.id} not found on Ship {self.id}.")

    def total_consumption(self) -> float:
        """
        Calculate total fuel consumption based on the containers on board.
        """
        return sum(container.consumption() for container in self.containers)

    def to_dict(self) -> Dict:
        """
        Convert the ship to a dictionary for saving to JSON.
        """
        return {
            "id": self.id,
            "max_weight": self.max_weight,
            "containers": [container.to_dict() for container in self.containers]
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Ship':
        """
        Restore a ship from a dictionary.
        """
        ship = Ship(data['id'], data['max_weight'])
        ship.containers = [Container.from_dict(c) for c in data['containers']]
        return ship

class ShipBuilder:
    """
    Builder pattern for creating different types of ships.
    """

    def __init__(self):
        self._id = None
        self._max_weight = None
        self._builder = None

    def set_id(self, id: int):
        self._id = id
        return self

    def set_max_weight(self, max_weight: float):
        self._max_weight = max_weight
        return self

    def set_builder(self, builder):
        self._builder = builder
        return self

    def build(self) -> Ship:
        """
        Build the ship based on provided parameters and ship type.
        """
        if not all([self._id, self._max_weight, self._builder]):
            raise ValueError("All parameters (id, max_weight, builder) must be provided")
        return self._builder.create_ship(self._id, self._max_weight)

class LightWeightShipBuilder:
    """
    Builder for lightweight ships.
    """
    @staticmethod
    def create_ship(id: int, max_weight: float) -> Ship:
        return Ship(id, max_weight)

class MediumShipBuilder:
    """
    Builder for medium ships.
    """
    @staticmethod
    def create_ship(id: int, max_weight: float) -> Ship:
        return Ship(id, max_weight)

class HeavyShipBuilder:
    """
    Builder for heavy ships.
    """
    @staticmethod
    def create_ship(id: int, max_weight: float) -> Ship:
        return Ship(id, max_weight)
