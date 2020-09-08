from aiohttp import web

routes = web.RouteTableDef()


@routes.get("")
async def index(request):
    return web.Response(text='Hello Aiohttp!')


api = web.Application()
api.add_routes(routes)
