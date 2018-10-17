#!/usr/bin/env python

# Open Pixel Control client: Every other light to solid white, others dark.

import opc, time

numPairs = 256
client = opc.Client('localhost:7890')

black = [ (0,0,0), (0,0,0) ] * numPairs
white = [ (255,255,255), (0,0,0) ] * numPairs

vec1 = [(255,255,255),
        (255,255,255),
        (255,255,255),
        ]

vec2 = [(0, 0, 0),
        (0,255,255),
        (0,255,255),
        (0,255,255)
        ]

vec3 = [(0, 0, 0),
        (0,0,255),
        (0,0,255),
        (0,0,255)
        ]

vec4 = [(0, 0, 0),
        (0,255,0),
        (0,255,0),
        (0,255,0)
        ]

vec5 = [(0, 0, 0),
        (255,0,0),
        (255,0,0),
        (255,0,0)
        ]

vec6 = [(255, 0, 255),
        (255,0,255),
        (255,0,255),
        ]
# Fade to white
client.put_pixels(black)
client.put_pixels(black)
time.sleep(.1)
client.put_pixels(vec1 + vec2 + vec3 + vec4 + vec5 + vec6)
import taulib as tl
ts = tl.TauServer()
ts.set_row((255, 255, 255), 0)
ts.set_row((255, 255, 255), 2)
ts.set_row((255, 255, 255), 4)

ts.clear()
ts.render()
time.sleep(0.4)
for n in xrange(0,6):
    for m in xrange(0,3):
        ts.set_pixel((255, 0, 60*m), n, m)
        ts.render()
        time.sleep(0.5)
        ts.clear()
        ts.render()
        time.sleep(0.5)


ts.render()

