# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 11:19:41 2018
title: Python in R
@author: Joel Alcedo
"""

import quandl
import sys

def grab_from_quandl(x):
    quandl.ApiConfig.api_key = "ENTER_API_KEY_HERE"
    try:
        df = quandl.get(x)
        return df
    except quandl.errors.quandl_error.NotFoundError:
        sys.tracebacklimit = 0
        print("\nUh oh! \n\nLooks like an incorrect quandl code.")

