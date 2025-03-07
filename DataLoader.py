# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:41:09 2024

@author: Peter
"""
import os

import pandas as pd

class DataLoader:
    @staticmethod
    def load(path, separator, header):
        ext = os.path.splitext(path)[1]
        try:
            match ext:
                case ".xlsx":
                    return pd.read_excel(path, header=header)
                case ".csv":
                    return pd.read_csv(path, sep=separator, header=header, engine='python')
                case ".txt":
                    return pd.read_csv(path, sep=separator, header=header, engine='python')
                case _:
                    return None
        except Exception as e:
            print(e)
            return None