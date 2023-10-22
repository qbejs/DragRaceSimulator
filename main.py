# main.py

from fastapi import FastAPI, WebSocket
from managers.stage_scenario_manager import StageScenarioManager
from scenarios.normal_race_scenario import NormalRaceScenario
from cars.garage.turbo import Turbo
from cars.garage.v8 import V8

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    car_one = Turbo()
    car_two = V8()

    scenario = NormalRaceScenario(car_one, car_two)
    manager = StageScenarioManager(scenario)

    # Ustawiamy samochody w managerze
    manager.set_track_one(car_one)
    manager.set_track_two(car_two)

    # Uruchamiamy scenariusz
    responses = await manager.exec()

    # Wysyłamy odpowiedzi do klienta WebSocket
    for response in responses:
        await websocket.send_json(response)

    await websocket.close()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
