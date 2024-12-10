from typing import Dict

class Container:
    """
    Container class that stores information about weight and calculates fuel consumption.
    """

    def __init__(self, id: int, weight: float) -> None:
        self.id = id
        self.weight = weight

    def consumption(self) -> float:
        """
        Returns the amount of fuel consumed for transporting the container.
        """
        return self.weight * 0.1

    def to_dict(self) -> Dict:
        """
        Converts the container to a dictionary for future JSON storage.
        """
        return {
            "id": self.id,
            "weight": self.weight
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Container':
        """
        Restores the container from a dictionary.
        """
        return Container(data['id'], data['weight'])


def container_factory(id: int, weight: float) -> Container:
    """
    Container factory that creates a container based on the given parameters.
    """
    return Container(id, weight)
