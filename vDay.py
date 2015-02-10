#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Vera Abaimova <stormseecker@gmail.com>
#
# Distributed under terms of the MIT license.


## A program to demostrate my love for one Mark Wells

from matplotlib.pyplot import *
from numpy import *

def i_love_you():

#    scale = 1
#    scale = .5

    t = linspace(-10,10,100)
#    t = linspace(-3,3,100)

    
    scales = linspace(.1,1)
    i = 0

    for scale in scales:
        x = scale * (16 * pow(sin(t),3))
        y = scale * (13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))

        xlim(-20,20)
        ylim(-20,20)
        plot(x,y,'r')
        name = 'base_heart_' + str(i) + '.png'
        savefig(name)
        show()
        i += 1

#    x = scale * (16 * pow(sin(t),3))

#    y = scale * (13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))

#    xlim(-20,20)
#    ylim(-20,20)
#    plot(x,y,'r')
#    savefig('base_heart.png')
#    show()

## The end
## But not really since my love for you never ends


if __name__ == "__main__":
    i_love_you()
