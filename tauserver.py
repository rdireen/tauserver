import asyncio
from aiohttp import web

outstring = ""

animations = {}
crouts = []

#*****************************************************************************
# Cllop through all the coroutines and play them
#*****************************************************************************
async def game_loop():
    global crouts 
    while True:
        for n, crout in enumerate(crouts):
            try:
                next(crout)
            except StopIteration:
                del crouts[n]

        await asyncio.sleep(0.2)
        #tau.render()

    app['dispatch'] = app.loop.create_task(game_loop())

#*****************************************************************************
# Setup and tear down background game_loop 
#*****************************************************************************
async def start_background_task(app):
    app['dispatch'] = app.loop.create_task(game_loop())

async def cleanup_background_task(app):
    app['dispatch'].cancel()
    await app['dispatch']

#*****************************************************************************
# Handle HTTP GET from browser 
#*****************************************************************************
async def handle(request):
    global crouts 
    global animations
    name = request.match_info.get('name', "default")
    if name in animations:
        crouts.append(animations[name]())
        
    return web.Response(text = "Playing: " + name)

def set_animations(animus):
    global animations
    animations = animus
#*****************************************************************************
# Setup the application and start the server 
#*****************************************************************************
def run():
    print("No longer Gage")
    app = web.Application()
    #app.router.add_get('/', handle)
    app.router.add_get('/input/{name}', handle)

    loop = asyncio.get_event_loop()
    app.on_startup.append(start_background_task)
    app.on_cleanup.append(cleanup_background_task)
    web.run_app(app)

if __name__ == "__main__":
    run()
