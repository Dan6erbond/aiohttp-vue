import asyncio
import weakref

import psutil
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/{pid}")
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    request.app['websockets'].add(ws)

    try:
        p = psutil.Process(int(request.match_info["pid"]))
    except BaseException:
        return web.HTTPServerError(reason="Process not found.")

    try:
        while True:
            await ws.send_json({
                "name": p.name(),
                "cpu": p.cpu_percent() / psutil.cpu_count(),
                "memory": p.memory_info()[1] * 0.000001,
                "memory_percent": p.memory_percent(),
            })
            await asyncio.sleep(0.5)
    finally:
        request.app['websockets'].discard(ws)

    return ws

app = web.Application()
app['websockets'] = weakref.WeakSet()

app.add_routes(routes)
