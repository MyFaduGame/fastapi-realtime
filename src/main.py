from fastapi import FastAPI
from loguru import logger
from json import dumps
from fastapi import Depends, FastAPI, WebSocket, WebSocketDisconnect

from .module.websocket import ConnectionManager

manager = ConnectionManager()

app = FastAPI()

@app.get("/test")
async def test():
    logger.info("test endpoint invoked")
    return "Hello world"

@app.websocket("/websocket")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            logger.info(data)
            await websocket.send_json(dumps(data))
    except WebSocketDisconnect:
        await manager.disconnect(websocket)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)