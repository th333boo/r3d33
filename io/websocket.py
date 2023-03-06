#!/usr/bin/env python3
import asyncio
import websockets

connected = set()

async def handler(websocket,path):
    connected.add(websocket)
    while True:
        try:
            if path == '/':
                # TODO async for headerlistenner in websocket:
                async for message in websocket:
                    for conn in connected:
                        await websocket.send("Welcome to the half demon portal \n @th333boo")

        except websockets.ConnectionClosedOK:
            break

async def th333booWebSoc():
    async with websockets.serve(handler, "127.0.0.1", 8443):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(th333booWebSoc())

# async def th333booWebSoc():
#     async with websockets.connect("ws://localhost:8765") as websocket:
#         await websocket.send("Hello world!")
#         await websocket.recv()