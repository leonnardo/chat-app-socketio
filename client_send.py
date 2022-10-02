import websockets
import asyncio


async def client_send():
    try:
        async with websockets.connect("ws://localhost:8765", ping_timeout=None) as ws:
            while True:
                msg = input()
                await ws.send(msg)

    except Exception as exc:
        print(exc)



asyncio.run(client_send())

