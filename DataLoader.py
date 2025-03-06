# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:41:09 2024

@author: Peter
"""
import os

import pandas as pd

class DataLoader:
    @staticmethod
    def load(path, separator=''):
        ext = os.path.splitext(path)[1]
        try:
            match ext:
                case ".xlsx":
                    return pd.read_excel(path)
                case ".csv":
                    return pd.read_csv(path, sep=separator)
                case ".txt":
                    return pd.read_csv(path, sep=separator)
                case _:
                    return None
        except:
            return None