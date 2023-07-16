from pprint import pprint
import asyncio
import json

import aiohttp


urls = [
    "https://pokeapi.co/api/v2/pokemon/ditto",
    "https://pokeapi.co/api/v2/pokemon/dragonite",
    "https://pokeapi.co/api/v2/pokemon/snorlax",
]


def write_to_file(data):
    with open("repo_data.json", "w") as f:
        json.dump(data, f)


async def fetch(session, url):
    async with session.get(url) as resp:
        body = await resp.json()
        return body


async def main():
    async with aiohttp.ClientSession() as session:
        data = await asyncio.gather(*[fetch(session, url) for url in urls])
        write_to_file(data)

    with open("repo_data.json", "r") as f:
        first = json.load(f)[0]
        pprint([ability for ability in first["abilities"]])


asyncio.run(main())
