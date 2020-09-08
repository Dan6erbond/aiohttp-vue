import os

from aiohttp import web

routes = web.RouteTableDef()

dist_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dist"))


@routes.get("/{base:(?!(api|ws)).*}")
async def index(request):
    html = False
    for accept in request.headers.getall('ACCEPT', []):
        if len(accept.split(",")) > 1:
            html = any(a == "text/html" for a in accept.split(","))
        else:
            html = accept == "text/html"

    if html:
        index_path = os.path.join(dist_path, "index.html")
        return web.FileResponse(index_path)
    else:
        file_path = os.path.join(dist_path, request.path[1:])
        if os.path.exists(file_path):
            return web.FileResponse(file_path)
        else:
            return web.HTTPNotFound()

routes.static("/", dist_path)
