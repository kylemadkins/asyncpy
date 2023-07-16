import asyncio

from quart import Quart, websocket, render_template
from quart import g


app = Quart(__name__)


conn = set()


@app.websocket("/ws")
async def ws():
    conn.add(websocket._get_current_object())
    try:
        while True:
            msg = await websocket.receive()
            await asyncio.gather(*[c.send(msg) for c in conn])
    finally:
        conn.remove(websocket._get_current_object())


@app.route("/")
async def home():
    return await render_template("home.html")


app.run(use_reloader=True, port=3000)
