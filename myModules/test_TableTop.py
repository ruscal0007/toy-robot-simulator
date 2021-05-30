# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:23:06 2021

@author: ben
"""

# test_wallet.py

import pytest
from myModules.TableTop import *


def test_default_play_area_size():
    TT = TableTop()
    assert len(TT.play_area[0]) == 5
    assert len(TT.play_area[1]) == 5
    
def test_custom_pay_area_size():
    TT = TableTop(20,50)
    assert len(TT.play_area) == 20
    assert len(TT.play_area[0]) == 50
    