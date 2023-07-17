import asyncio

from quart import Quart, websocket, render_template, jsonify
import redis.asyncio as redis


app = Quart(__name__)


conn = set()


@app.websocket("/ws")
async def ws():
    db = redis.Redis()
    conn.add(websocket._get_current_object())
    try:
        while True:
            msg = await websocket.receive()
            await db.rpush("messages", msg)
            await db.close()
            await asyncio.gather(*[c.send(msg) for c in conn])
    finally:
        conn.remove(websocket._get_current_object())


@app.route("/messages")
async def messages():
    db = redis.Redis()
    msgs = await db.lrange("messages", 0, -1)
    await db.close()
    return jsonify([m.decode("utf-8") for m in msgs])


@app.route("/")
async def home():
    return await render_template("home.html")


app.run(use_reloader=True, port=3000)
