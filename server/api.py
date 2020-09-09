import psutil
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/processes")
async def index(request):
    """
    ---
    description: Returns a list of running system processes.
    tags:
    - System Monitoring
    produces:
    - application/json
    responses:
        "200":
            description: Successful operation returns a JSON array of system processes.
        "405":
            description: Invalid HTTP method.
    """
    return web.json_response([
        process.as_dict(attrs=[
            "pid",
            "name",
            "username",
            "create_time",
            "exe",
        ])
        for process in psutil.process_iter()
    ])


@routes.get("/processes/{pid:\d+}")
async def get(request):
    """
    ---
    description: Fetch the information for a specific system process.
    tags:
    - System Monitoring
    produces:
    - application/json
    parameters:
    - in: path
      name: pid
      description: The process ID.
      required: true
      schema:
        type: number
    responses:
        "200":
            description: Successful operation returns a JSON object the system process.
        "405":
            description: Invalid HTTP method.
    """
    process = psutil.Process(int(request.match_info["pid"]))
    return web.json_response(process.as_dict(attrs=[
        "pid",
        "name",
        "username",
        "create_time",
        "exe",
    ]))

app = web.Application()
app.add_routes(routes)
