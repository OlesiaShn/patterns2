class SingletonMeta(type):
    """A metaclass for implementing the Singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SettingsManager(metaclass=SingletonMeta):
    """Global settings for a smart home."""
    def __init__(self):
        self.settings = {
            "temperature": 22,
            "lighting_mode": "warm",
        }

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key)


class EnergyManager(metaclass=SingletonMeta):
    """Power consumption management."""
    def monitor_usage(self):
        return "Energy usage is being monitored."

    def optimize_energy(self):
        return "Energy usage has been optimized."


class LightingSystem:
    """Lighting system."""
    def activate(self):
        return "Lighting system turned on."

    def deactivate(self):
        return "Lighting system turned off."

    def adjust_brightness(self, level):
        return f"Brightness set to {level}."


class ClimateControlSystem:
    """Climate control system."""
    def activate(self):
        return "Climate control started."

    def deactivate(self):
        return "Climate control stopped."

    def set_temperature(self, target_temp):
        return f"Temperature set to {target_temp}°C."


class EntertainmentSystem:
    def play_music(self):
        return "Music is playing."

    def stop_music(self):
        return "Music stopped."

    def set_volume(self, level):
        return f"Volume set to {level}."


class SecuritySystem:
    """Security system."""
    def activate(self):
        return "Security system armed."

    def deactivate(self):
        return "Security system disarmed."


class VoiceControl:
    def __init__(self, facade):
        self.facade = facade

    def execute_command(self, command):
        commands_map = {
            "turn on lights": self.facade.turn_lighting_on,
            "arm security": self.facade.activate_security,
            "set temperature": lambda: self.facade.start_climate(22),
        }
        action = commands_map.get(command.lower(), lambda: "Command not recognized.")
        return action()


class SmartHomeFacade:
    """Facade for simplified access to subsystems."""
    def __init__(self):
        self.settings = SettingsManager()
        self.energy = EnergyManager()
        self.lighting = LightingSystem()
        self.climate = ClimateControlSystem()
        self.security = SecuritySystem()
        self.entertainment = EntertainmentSystem()
        self.voice_control = VoiceControl(self)

    def turn_lighting_on(self):
        return self.lighting.activate()

    def turn_lighting_off(self):
        return self.lighting.deactivate()

    def adjust_brightness(self, level):
        return self.lighting.adjust_brightness(level)

    def start_climate(self, temperature=None):
        response = self.climate.activate()
        if temperature:
            response += f" {self.climate.set_temperature(temperature)}"
        return response

    def stop_climate(self):
        return self.climate.deactivate()

    def activate_security(self):
        return self.security.activate()

    def deactivate_security(self):
        return self.security.deactivate()
