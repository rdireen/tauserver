#!/usr/bin/env python3

import taulib as tl
import time
ts = tl.TauServer()
ts.clear()
ts.render()
time.sleep(1)


while(True):
    ts.set_row((255, 255, 255), 0)
    ts.set_row((255, 255, 255), 2)
    ts.set_row((255, 255, 255), 4)
    ts.render()
    time.sleep(1)
    ts.clear()
    ts.render()
    time.sleep(1)





