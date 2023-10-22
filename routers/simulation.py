from fastapi import APIRouter, WebSocket
from managers.stage_manager import StageManager
from utils.response_creator import ResponseCreator

router = APIRouter()
stage_manager = StageManager()


@router.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        handler = stage_manager.get_handler(data)
        if handler:
            event_data = handler.get_response()
            response = ResponseCreator.create_response(event_data["event"], event_data)
            await websocket.send_json(response)
        elif data == "disconnect":
            await websocket.close()
            break
