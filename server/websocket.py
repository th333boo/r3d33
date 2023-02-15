#!/usr/bin/env python3
import asyncio
import websockets
import ssl

class TB_WebSocket():
    async def hello():
        async with websockets.connect("wss://localhost:3333") as websocket:
            await websocket.send("Hello world!")
            await websocket.recv()
    asyncio.run(hello())
TB_WebSocket()  