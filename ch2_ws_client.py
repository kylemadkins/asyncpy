import asyncio

import click
import websockets


async def client():
    async with websockets.connect("ws://localhost:8765") as ws:
        while True:
            msg = input("Send a message: ")
            await ws.send(msg)
            resp = await ws.recv()
            click.secho(resp, bold=True, fg="green")


async def main():
    click.clear()
    await asyncio.gather(client())


asyncio.run(main())
