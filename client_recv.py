import websockets
import asyncio


async def client_recv():
    try:
        async with websockets.connect("ws://localhost:8765", ping_timeout=None) as ws:
            async for msg in ws:
                print(msg)
    except Exception as exc:
        print(exc)


asyncio.run(client_recv())

