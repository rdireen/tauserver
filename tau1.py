
import tauserver
import taulib as tl
import math
import traceback

tau = tl.TauLibs()

def play_test_coroutine():
    for x in range(0, 10):
        tau.set_row((0, 25*x, 0), 1)
        tau.render()
        yield x

    for x in range(0, 10):
        tau.set_row((0, 255 - 25*x, 0), 1)
        tau.render()
        yield x

    tau.set_row((0, 0, 0), 1)
    tau.render()
    yield 0

def play_test2_coroutine():
    for x in range(0, 10):
        tau.set_row((0, 25*x, 0), 3)
        tau.render()
        yield x

    for x in range(0, 10):
        tau.set_row((0, 255 - 25*x, 0), 3)
        tau.render()
        yield x

    tau.set_row((0, 0, 0), 3)
    tau.render()
    yield 0

def boot_up_coroutine():
    try:
        for x in range(0, 10, 1):
            tau.set_row((0, 0, 25*x), 5)
            tau.render()
            yield x

        for x in range(0, 10,1 ):
            tau.set_row((0, 0, 25*x), 3)
            tau.render()
            yield x

        for x in range(1, 10):
            tau.set_row((0, 0, 25*x), 1)
            tau.render()
            yield x

        for x in range(1, 10):
            tau.set_row((25*x, 25*x, 25*x), 0)
            tau.set_row((25*x, 25*x, 25*x), 2)
            tau.set_row((25*x, 25*x, 25*x), 4)
            tau.render()
            yield x
    except Exception as e:
        traceback.print_exc()

def clear_coroutine():
    tau.clear()
    tau.render()
    yield 0



animus = {}
animus['play'] = play_test_coroutine
animus['play2'] = play_test2_coroutine
animus['boot'] = boot_up_coroutine
animus['clear'] = clear_coroutine

tauserver.set_animations(animus)
tauserver.run()
