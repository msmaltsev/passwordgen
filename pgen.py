#!/usr/bin/python
# -*- coding: utf-8 -*-

import string, random
try:
    import clipboard
except:
    print('could not import clipboard')

def generatePW(plen = 10, echo = True, cb = True):
    let = string.ascii_letters + string.digits
    p = ''
    while len(p) != plen:
        p += random.choice(let)
    if echo:
        print(p)
    if cb:
        try:
            clipboard.copy(p)
        except:
            print('could not copy password into clipboard')
    return p

if __name__ == '__main__':
    generatePW()