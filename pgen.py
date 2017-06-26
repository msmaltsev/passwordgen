#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string, random
try:
    import clipboard
except:
    print('could not import clipboard')

def generatePW(plen = 10, echo = True, copy_to_cb = True):
    let = string.ascii_letters + string.digits
    p = ''
    while len(p) != plen:
        p += random.choice(let)
    if echo:
        print(p)
    if copy_to_cb:
        try:
            clipboard.copy(p)
            print('copied into clipboard')
        except:
            print('could not copy password into clipboard')
    return p

if __name__ == '__main__':
    generatePW()
    
