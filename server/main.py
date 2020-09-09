import asyncio
import os
import webbrowser

import psutil
from aiohttp import web
from aiohttp_swagger import setup_swagger

from api import app as api
from app import app as app
from config import config
from websocket import app as websocket

loop = asyncio.get_event_loop()

runner = None
vue_proc = None


async def start():
    global runner, vue_proc

    setup_swagger(api,
                  description=config.description,
                  title=config.title,
                  ui_version=3,
                  contact=config.contact_email,
                  api_base_url="/api",
                  swagger_url="doc")

    app.add_subapp("/api", api)

    app.add_subapp("/ws", websocket)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, config.host, config.port)
    await site.start()

    url = f"http://{config.host}:{config.port}"

    print("Running server on:", url)

    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    if config.debug:
        vue_proc = await asyncio.create_subprocess_shell(
            f"yarn --cwd {frontend_path} build --watch",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

    print("Running Vue build in watch mode:", vue_proc.pid)

    webbrowser.open(url, 2)


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
