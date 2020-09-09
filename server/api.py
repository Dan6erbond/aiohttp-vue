from aiohttp import web

routes = web.RouteTableDef()


@routes.get("")
async def index(request):
    """
    ---
    description: This endpoint tests the API routes.
    tags:
    - Health check
    produces:
    - text/plain
    responses:
        "200":
            description: Successful operation returns "Hello Aiohttp!"
        "405":
            description: Invalid HTTP method.
    """
    return web.Response(text='Hello Aiohttp!')

app = web.Application()
app.add_routes(routes)
