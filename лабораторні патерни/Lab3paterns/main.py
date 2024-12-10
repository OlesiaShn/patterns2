from ports import Port
from ships import ShipBuilder
from containers import container_factory


def main():
    """Main function to simulate the loading and unloading of ships in ports.

    This function creates instances of ports, ships, and containers, simulates
    loading and unloading operations, calculates fuel consumption, and demonstrates
    saving and loading port data in JSON format.

    Steps:
        1. Create two ports (Kyiv and Odesa).
        2. Create two ships with different weight limits.
        3. Create containers of different types (basic, refrigerated, liquid).
        4. Load and unload containers onto/from ships.
        5. Calculate and print total fuel consumption for one ship.
        6. Simulate the arrival of a ship in a port.
        7. Save port data to a JSON file and load it back from the file.

    Example:
        >>> main()
        Total fuel consumption for Ship 101y: 13280.0 units
        Loaded Port 1 with coordinates (50.4501, 30.5234)
    """
    port1 = Port(1, (50.4501, 30.5234))  # Київ
    port2 = Port(2, (46.4825, 30.7233))  # Одеса

    ship1 = ShipBuilder().set_id(101).set_max_weight(10000).build()
    ship2 = ShipBuilder().set_id(102).set_max_weight(15000).build()

    container1 = container_factory(3, 1960)  # Легкий контейнер
    container2 = container_factory(6, 3320, 'refrigerated')  # Охолоджуваний контейнер
    container3 = container_factory(2, 4100, 'liquid')  # Рідкий контейнер

    ship1.load_container(container1)
    ship1.load_container(container2)
    ship1.unload_container(container1)

    print(f"Total fuel consumption for Ship {ship1.id}: {ship1.total_consumption()} units")

    port1.incoming_ship(ship1)
    port1.save_to_json('port1_data.json')

    loaded_port = Port.load_from_json('port1_data.json')
    print(f"Loaded Port {loaded_port.id} with coordinates {loaded_port.coordinates}")


if __name__ == "__main__":
    main()
