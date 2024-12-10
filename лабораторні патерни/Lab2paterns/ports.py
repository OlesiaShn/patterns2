import json
from typing import Protocol, Any, Tuple, List, Dict
from containers import Container

class IPort(Protocol):
    """Interface for port operations.

    This interface defines the methods that any port class must implement
    to manage incoming and outgoing ships.
    """
    def incoming_ship(self, ship: Any) -> None:
        """Register an incoming ship at the port.

        Args:
            ship (Any): The ship that is arriving at the port.
        """
        pass

    def outgoing_ship(self, ship: Any) -> None:
        """Register an outgoing ship from the port.

        Args:
            ship (Any): The ship that is leaving the port.
        """
        pass

class Port(IPort):
    """Class representing a port.

    Attributes:
        id (int): The unique identifier of the port.
        coordinates (Tuple[float, float]): The geographical coordinates of the port.
        containers (List[Container]): A list of containers currently in the port.
        ships (List[Any]): A list of ships currently at the port.
        history (List[Any]): A list of ships that have previously been in the port.
    """

    def __init__(self, id: int, coordinates: Tuple[float, float]) -> None:
        """Initialize a Port instance.

        Args:
            id (int): The unique identifier of the port.
            coordinates (Tuple[float, float]): The geographical coordinates of the port.
        """
        self.id = id
        self.coordinates: Tuple[float, float] = coordinates
        self.containers: List[Container] = []
        self.ships: List[Any] = []  # Список поточних кораблів
        self.history: List[Any] = []  # Список кораблів, що вже були в порту

    def incoming_ship(self, ship: Any) -> None:
        """Register an incoming ship at the port.

        Args:
            ship (Any): The ship that is arriving at the port.

        Prints:
            A message indicating the arrival of the ship.
        """
        self.ships.append(ship)
        print(f"Ship {ship.id} has arrived at Port {self.id}.")

    def outgoing_ship(self, ship: Any) -> None:
        """Register an outgoing ship from the port.

        Args:
            ship (Any): The ship that is leaving the port.

        Prints:
            A message indicating the departure of the ship or if the ship was
            not found in the port.
        """
        if ship in self.ships:
            self.ships.remove(ship)
            self.history.append(ship)
            print(f"Ship {ship.id} has left Port {self.id}.")
        else:
            print(f"Ship {ship.id} is not in Port {self.id}.")

    def to_dict(self) -> Dict:
        """Convert the Port instance to a dictionary representation.

        Returns:
            Dict: A dictionary containing the port's attributes.
        """
        return {
            "id": self.id,
            "coordinates": self.coordinates,
            "containers": [container.to_dict() for container in self.containers],
            "ships": [ship.to_dict() for ship in self.ships],
            "history": [ship.to_dict() for ship in self.history],
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Port':
        """Create a Port instance from a dictionary representation.

        Args:
            data (Dict): A dictionary containing port attributes.

        Returns:
            Port: A new Port instance populated with data from the dictionary.
        """
        port = Port(data['id'], tuple(data['coordinates']))
        # Set containers and ships if present
        return port

    def save_to_json(self, filename: str) -> None:
        """Save the port data to a JSON file.

        Args:
            filename (str): The name of the file to save the port data.
        """
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_json(filename: str) -> 'Port':
        """Load a Port instance from a JSON file.

        Args:
            filename (str): The name of the file to load the port data from.

        Returns:
            Port: A Port instance populated with data from the JSON file.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        return Port.from_dict(data)
