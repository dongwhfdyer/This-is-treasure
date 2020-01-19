#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
from PyInstaller.__main__ import run
import sys
 
if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    opts = ['-F',
            '-w',
            '--paths=D:\\',
            'tb.py']
    run(opts)
