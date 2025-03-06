# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:38:03 2024

@author: Peter
"""

# Sekcja deklaracji
import sys, os
import DataLoader as dl
import numpy as np

def main() -> int:
    args = sys.argv[1:]
    arg_pairs = np.array_split(args, len(args))
    print(arg_pairs)

    x = dl.DataLoader()
    x.load(os.path.join(os.getcwd(),"Dane","Excel.xlsx"))
    return 0
    
	
# Punkt wejscia do programu
if __name__ == '__main__':
    sys.exit(main())