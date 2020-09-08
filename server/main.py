import asyncio
import os

from aiohttp import web
import psutil
import weakref

from app import routes as app_routes
from api import routes as api_routes
from websocket import routes as websocket_routes

loop = asyncio.get_event_loop()

runner = None
vue_proc = None


async def start():
    global runner, vue_proc

    app = web.Application()
    app['websockets'] = weakref.WeakSet()

    app.add_routes(api_routes)
    app.add_routes(websocket_routes)
    app.add_routes(app_routes)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "127.0.0.1", 8080)
    await site.start()

    print("Running server on: http://127.0.0.1:8080")

    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    vue_proc = await asyncio.create_subprocess_shell(
        f"yarn --cwd {frontend_path} build --watch",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    print("Running Vue build in watch mode:", vue_proc.pid)


def main():
    loop.create_task(start())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        if runner:
            print("Killing application server.")
            loop.run_until_complete(runner.cleanup())
        if vue_proc:
            print("Killing Vue build process:", vue_proc.pid)
            p = psutil.Process(vue_proc.pid)
            p.terminate()


if __name__ == "__main__":
    main()
