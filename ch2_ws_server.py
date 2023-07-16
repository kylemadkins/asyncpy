import asyncio

import websockets
import click


async def handler(ws):
    while True:
        try:
            msg = await ws.recv()
            await ws.send(f'Received "{msg}"')
        except websockets.ConnectionClosedOK:
            break


async def main():
    click.clear()
    PORT = 8765
    async with websockets.serve(handler, "localhost", PORT):
        click.secho(f"Listening for WebSocket connections on port {PORT}")
        await asyncio.Future()


asyncio.run(main())
