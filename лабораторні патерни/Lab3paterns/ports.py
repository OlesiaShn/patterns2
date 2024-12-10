import json
from typing import Tuple, List, Dict
from containers import Container


class Ship:
    """Class representing a ship.

    This is a placeholder class to represent ships that dock in ports.
    It should be extended with attributes and methods to handle ship-specific functionality.
    """
    pass


class Port:
    """Class representing a port where ships dock and unload containers.

    Attributes:
        id (int): The unique identifier of the port.
        coordinates (Tuple[float, float]): The geographical coordinates of the port.
        containers (List[Container]): A list of containers currently in the port.
        ships (List[Ship]): A list of ships currently docked in the port.
        history (List[Ship]): A list of ships that have previously docked at the port.
    """

    def __init__(self, id: int, coordinates: Tuple[float, float]):
        """Initializes a Port instance.

        Args:
            id (int): The unique identifier of the port.
            coordinates (Tuple[float, float]): The geographical coordinates of the port.
        """
        self.id = id
        self.coordinates: Tuple[float, float] = coordinates
        self.containers: List[Container] = []
        self.ships: List[Ship] = []
        self.history: List[Ship] = []

    def incoming_ship(self, ship: Ship):
        """Registers an incoming ship at the port.

        Args:
            ship (Ship): The ship that is arriving at the port.
        """
        self.ships.append(ship)
        print(f"Ship {ship.id} has arrived at Port {self.id}.")

    def outgoing_ship(self, ship: Ship) -> None:
        """Registers an outgoing ship from the port.

        If the ship is found in the port, it is moved to the history list after departure.

        Args:
            ship (Ship): The ship that is leaving the port.

        Prints:
            A message indicating whether the ship has left the port, or if the ship was not found.
        """
        if ship in self.ships:
            self.ships.remove(ship)
            self.history.append(ship)
            print(f"Ship {ship.id} has left Port {self.id}.")
        else:
            print(f"Ship {ship.id} is not in Port {self.id}.")

    def to_dict(self) -> Dict:
        """Converts the Port instance to a dictionary representation.

        Returns:
            Dict: A dictionary containing the port's attributes, including its containers, ships, and history.
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
        """Creates a Port instance from a dictionary.

        Args:
            data (Dict): A dictionary containing port attributes.

        Returns:
            Port: A new Port instance populated with data from the dictionary.
        """
        port = Port(data['id'], tuple(data['coordinates']))
        return port

    def save_to_json(self, filename: str) -> None:
        """Saves the port's data to a JSON file.

        Args:
            filename (str): The name of the file where the port's data will be saved.
        """
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_json(filename: str) -> 'Port':
        """Loads a Port instance from a JSON file.

        Args:
            filename (str): The name of the file from which to load the port's data.

        Returns:
            Port: A new Port instance populated with data from the JSON file.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        return Port.from_dict(data)
