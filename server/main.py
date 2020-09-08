import asyncio

from aiohttp import web

from .api import api
from .app import app

loop = asyncio.get_event_loop()
runners = list()


def main():
    async def start():
        async def start_site(app, address="127.0.0.1", port=8080):
            runner = web.AppRunner(app)
            runners.append(runner)
            await runner.setup()
            site = web.TCPSite(runner, address, port)
            await site.start()

        await start_site(app)
        await start_site(api, port=8081)

    loop.create_task(start())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        for runner in runners:
            loop.run_until_complete(runner.cleanup())


if __name__ == "__main__":
    main()
