from aiohttp import web

routes = web.RouteTableDef()


@routes.get("")
async def index(request):
    """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Health check
    produces:
    - text/plain
    responses:
        "200":
            description: successful operation. Return "pong" text
        "405":
            description: invalid HTTP Method
    """
    return web.Response(text='Hello Aiohttp!')

app = web.Application()
app.add_routes(routes)
