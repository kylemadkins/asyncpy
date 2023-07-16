from datetime import datetime
from pprint import pprint
import asyncio

import click
import requests
import aiohttp


urls = [
    "http://httpbin.org/get?text=python",
    "http://httpbin.org/get?text=is",
    "http://httpbin.org/get?text=fun",
    "http://httpbin.org/get?text=and",
    "http://httpbin.org/get?text=useful",
    "http://httpbin.org/get?text=you",
    "http://httpbin.org/get?text=can",
    "http://httpbin.org/get?text=almost",
    "http://httpbin.org/get?text=do",
    "http://httpbin.org/get?text=anything",
    "http://httpbin.org/get?text=with",
    "http://httpbin.org/get?text=it",
]  # 12 requests


def get_args_sync(url):
    return requests.get(url).json()["args"]


async def get_args_async(session, url):
    async with session.get(url) as resp:
        data = await resp.json()
        return data["args"]


async def main():
    async with aiohttp.ClientSession() as session:
        data = await asyncio.gather(*[get_args_async(session, url) for url in urls])
        pprint(data)


# Sync vs. async requests
start = datetime.now()
pprint([get_args_sync(url) for url in urls])
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")

start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
