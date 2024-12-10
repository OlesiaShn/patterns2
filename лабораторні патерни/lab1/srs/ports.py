import json
from typing import Protocol, Any, Tuple, List, Dict
from containers import Container

class IPort(Protocol):
    """
    Interface for ports. Describes methods for handling incoming and outgoing ships.
    """

    def incoming_ship(self, ship: Any) -> None:
        pass

    def outgoing_ship(self, ship: Any) -> None:
        pass

class Port(IPort):
    """
    Port class that stores information about ships currently at the port and those that have been processed.
    """

    def __init__(self, id: int, coordinates: Tuple[float, float]) -> None:
        self.id = id
        self.coordinates: Tuple[float, float] = coordinates
        self.containers: List[Container] = []
        self.ships: List[Any] = []  # List of current ships
        self.history: List[Any] = []  # List of ships that have been in the port

    def incoming_ship(self, ship: Any) -> None:
        """
        Adds a ship to the list of ships in the port.
        """
        self.ships.append(ship)
        print(f"Ship {ship.id} has arrived at Port {self.id}.")

    def outgoing_ship(self, ship: Any) -> None:
        """
        Removes a ship from the port and adds it to the history.
        """
        if ship in self.ships:
            self.ships.remove(ship)
            self.history.append(ship)
            print(f"Ship {ship.id} has left Port {self.id}.")
        else:
            print(f"Ship {ship.id} is not in Port {self.id}.")

    def to_dict(self) -> Dict:
        """
        Converts the port to a dictionary for future JSON storage.
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
        """
        Restores the port from a dictionary.
        """
        port = Port(data['id'], tuple(data['coordinates']))
        return port

    def save_to_json(self, file_path: str) -> None:
        """
        Saves the port information to a JSON file.
        """
        with open(file_path, 'w') as json_file:
            json.dump(self.to_dict(), json_file, indent=4)
        print(f"Port {self.id} saved to {file_path}.")

    @staticmethod
    def load_from_json(file_path: str) -> 'Port':
        """
        Loads the port from a JSON file.
        """
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return Port.from_dict(data)
