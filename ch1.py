import asyncio
from datetime import datetime

import click


async def sleep_and_print(seconds):
  print(f"Starting sleep for {seconds} seconds...")
  await asyncio.sleep(seconds)
  print(f"Finished sleep for {seconds} seconds")
  return seconds


async def main():
  await asyncio.gather(*[sleep_and_print(i+1) for i in range(10)])


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
