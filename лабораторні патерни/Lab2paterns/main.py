from ports import Port
from ships import Ship
from containers import container_factory

def main():
    """Main function to simulate the loading and unloading of ships in ports.

    This function creates instances of ports, ships, and containers,
    simulates loading and unloading operations, calculates fuel consumption,
    and demonstrates saving and loading port data in JSON format.
    """
    # Створення портів
    port1 = Port(1, (50.4501, 30.5234))  # Київ
    port2 = Port(2, (46.4825, 30.7233))  # Одеса

    # Створення кораблів
    ship1 = Ship(101, 10000)  # Корабель з лімітом 10000 кг
    ship2 = Ship(102, 15000)  # Корабель з лімітом 15000 кг

    # Створення контейнерів
    container1 = container_factory(3, 1960)  # Легкий контейнер
    container2 = container_factory(6, 3320)  # Важкий контейнер
    container3 = container_factory(2, 4100)  # Важкий контейнер

    # Завантаження контейнерів на корабель
    ship1.load_container(container1)  # Завантажимо легкий контейнер на перший корабель
    ship1.load_container(container2)  # Завантажимо важкий контейнер на перший корабель

    # Вивантаження контейнера
    ship1.unload_container(container1)

    # Розрахунок споживання палива
    print(f"Total fuel consumption for Ship {ship1.id}: {ship1.total_consumption()} units")

    # Корабель заходить у порт
    port1.incoming_ship(ship1)

    # Збереження даних в JSON
    port1.save_to_json('port1_data.json')

    # Завантаження з JSON
    loaded_port = Port.load_from_json('port1_data.json')
    print(f"Loaded Port {loaded_port.id} with coordinates {loaded_port.coordinates}")

if __name__ == "__main__":  # Fixed from 'if name == "main":'
    main()
