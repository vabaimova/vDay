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

    t = linspace(-10,10,100)
    
    scales = linspace(.1,1)
    i = 0

    for scale in scales:
        x = scale * (16 * pow(sin(t),3))
        y = scale * (13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))

        xlim(-20,20)
        xlabel("I love you more than anything.")
        ylim(-20,20)
        ylabel("I love you more than everything.")
        title('I Love You')
        plot(x,y,'r')
        fileNum = str(i)
        name = 'base_heart_' + fileNum.zfill(3) + '.png'
        savefig(name)
        i += 1

## The end
## But not really since my love for you never ends


if __name__ == "__main__":
    i_love_you()
