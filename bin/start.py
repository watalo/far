#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:far.py
@TIME		:2022/06/23 01:35:10
@AUTHOR     :watalo
@VERSION	:0.0.x
'''

import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from far import main


if __name__ == '__main__':
    # main.run()
    print(BASE_DIR)
    main.run()