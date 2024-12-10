from ports import Port
from ships import ShipBuilder, LightWeightShipBuilder, MediumShipBuilder, HeavyShipBuilder
from containers import container_factory

def main():
    """
    Main function to run the port system simulation.
    Creates ports, ships, containers, loads and unloads containers,
    simulates ship movements, and saves data in JSON.
    """

    # Create ports
    port1 = Port(1, (50.4501, 30.5234))  # Kyiv
    port2 = Port(2, (46.4825, 30.7233))  # Odesa

    # Using Builder to create ships
    ship_builder = ShipBuilder()

    light_ship = ship_builder.set_id(101).set_max_weight(5000).set_builder(LightWeightShipBuilder()).build()
    medium_ship = ship_builder.set_id(102).set_max_weight(10000).set_builder(MediumShipBuilder()).build()
    heavy_ship = ship_builder.set_id(103).set_max_weight(15000).set_builder(HeavyShipBuilder()).build()

    # Create containers
    container1 = container_factory(1, 2000)  # Lightweight container
    container2 = container_factory(2, 3500)  # Heavy container
    container3 = container_factory(3, 4000)  # Heavy container

    # Load containers onto ships
    light_ship.load_container(container1)
    medium_ship.load_container(container2)
    heavy_ship.load_container(container3)

    # Unload container
    light_ship.unload_container(container1)

    # Calculate fuel consumption
    print(f"Total fuel consumption for Ship {light_ship.id}: {light_ship.total_consumption()} units")

    # Ship enters port
    port1.incoming_ship(light_ship)

    # Save data to JSON
    port1.save_to_json('port1_data.json')

    # Load from JSON
    loaded_port = Port.load_from_json('port1_data.json')
    print(f"Loaded Port {loaded_port.id} with coordinates {loaded_port.coordinates}")

if __name__ == "__main__":
    main()
