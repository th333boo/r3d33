#!/usr/bin/env python3
import asyncio
import websockets
import ssl

class TB_WebSocket():
    async def listen ():
        url = "wss://localhost:3333"
        async with websockets.connect(url) as th333boo_websocket:
            await th333boo_websocket.send("Hello world!")
            while True:
                msg = await th333boo_websocket.recv()
                print(msg)
    asyncio.get_event_loop().run_until_complete(listen())
#    asyncio.run(listen())
TB_WebSocket()  