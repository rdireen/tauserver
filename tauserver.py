import asyncio
from aiohttp import web
import taulib as tl

outstring = ""

async def game_loop():
    global outstring
    while True:
        print("looping: " + outstring)
        await asyncio.sleep(0.2)

async def start_background_task(app):
    app['dispatch'] = app.loop.create_task(game_loop())

async def cleanup_background_task(app):
    app['dispatch'].cancel()
    await app['dispatch']

async def handle(request):
    global outstring
    name = request.match_info.get('name', "default")
    outstring = name
    return web.Response(text = "Hello " + name)

app = web.Application()
#app.router.add_get('/', handle)
app.router.add_get('/input/{name}', handle)

loop = asyncio.get_event_loop()
app.on_startup.append(start_background_task)
app.on_cleanup.append(cleanup_background_task)
web.run_app(app)
