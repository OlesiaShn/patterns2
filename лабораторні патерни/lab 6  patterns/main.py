from fastapi import FastAPI
from smart_home import SmartHomeFacade
from bridge import RemoteController

app = FastAPI()

smart_home = SmartHomeFacade()

lighting_controller = RemoteController(smart_home.lighting)
climate_controller = RemoteController(smart_home.climate)
security_controller = RemoteController(smart_home.security)


@app.get("/light/on")
def enable_light():
    return {"status": lighting_controller.enable()}

@app.get("/light/off")
def disable_light():
    return {"status": lighting_controller.disable()}

@app.get("/light/brightness/{level}")
def adjust_light_brightness(level: int):
    return {"status": smart_home.adjust_brightness(level)}

@app.get("/climate/on")
def activate_climate():
    return {"status": climate_controller.enable()}

@app.get("/climate/off")
def deactivate_climate():
    return {"status": climate_controller.disable()}

@app.get("/climate/temperature/{temp}")
def update_climate_temperature(temp: int):
    return {"status": smart_home.start_climate(temperature=temp)}

@app.get("/security/arm")
def enable_security_mode():
    return {"status": security_controller.enable()}

@app.get("/security/disarm")
def disable_security_mode():
    return {"status": security_controller.disable()}
