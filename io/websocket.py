#!/usr/bin/env python3
import asyncio
import websockets

connected = set()

async def handler(websocket,path):
    connected.add(websocket)
    while True:
        try:
            # if path == '/':
            #     # TODO async for headerlistenner in websocket:
            async for msg in websocket:
                for conn in connected:
                    if conn != websocket:
                        await websocket.send("🏴‍☠️ Welcome @th333boo station\n⚪ Wh1t3h4t3 3th1c4l h4ck3r ⚫\n☠️ Malware researcher")

        except websockets.ConnectionClosedOK:
            break

async def th333booWebSoc():
    async with websockets.serve(handler, "127.0.0.1", 3333):
 #       await asyncio.get_event_loop().run_until_complete(th333booWebSoc)
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(th333booWebSoc())
    asyncio.Future()  # run forever
    # asyncio.get_event_loop().run_forever()

# async def th333booWebSoc():
#     async with websockets.connect("ws://localhost:8765") as websocket:
#         await websocket.send("Hello world!")
#         await websocket.recv()