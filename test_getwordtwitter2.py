#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:53:59 2020

@author: taimaame
"""


from getwordtwitter2 import get_all_tweets

def test_get_all_tweets():
    assert get_all_tweets('a','b') != []
