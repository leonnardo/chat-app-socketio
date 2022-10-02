from time import strftime, localtime
import websockets
import asyncio

CLIENTS = set()

async def broadcast():
    while True:
        message = strftime("[%Y-%m-%d %H:%M:%S]", localtime())
        websockets.broadcast(CLIENTS, message)
        await asyncio.sleep(5)

async def recv(ws):
    async for msg in ws:
        print(f'Message from client: {msg}')
        websockets.broadcast(CLIENTS, msg)

async def listen(ws):
    print("A client just connected")
    CLIENTS.add(ws)

    try:
        await asyncio.gather(broadcast(), recv(ws))

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        CLIENTS.remove(ws)

async def main():
    async with websockets.serve(listen, "", 8765, ping_timeout=None):
        print("Server listening to port 8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())


