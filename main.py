# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:38:03 2024

@author: Peter
"""

# Cheat sheet:
# py main.py -i ./Dane/plaintext.txt -o ./results/res.txt -d ./results/image.png -s "\s+" -so " " -e "54"
# py main.py -i ./Dane/CSV.csv -o ./results/res.csv -d ./results/image.png -h 0 -s ";" -so ";" -e "Category"
# py main.py -i ./Dane/Excel.xlsx -o ./results/res.xlsx -d ./results/image.png -h 0 -e "Category"
import sys, os
from DataLoader import DataLoader
from pathlib import Path
from DataDescriber import DataDescriber
from DataDrawer import DataDrawer
from DataSaver import DataSaver
from DatraProcessor import DataProcessor


def main() -> int:
    args = sys.argv[1:]
    args = dict(zip([args[i] for i in range(0, len(args), 2)], [args[i] for i in range(1, len(args), 2)]))

    if not "-i" in args or not "-o" in args or not "-d" in args:
        print("usage: -i <input_path> -o <output_path> -d <graph_output_path> [-e <category_column>] [-s <input_separator>] [-so <output_separator>] [-h <header_lines>]")
        return 1

    data = DataLoader.load(os.path.abspath(args["-i"]), args.get("-s", ' '), (int(args.get("-h", None)) if args.get("-h", None) is not None else None))
    if data is None:
        return 1

    path = Path(os.path.dirname(os.path.abspath(args["-d"])))
    path.mkdir(parents=True, exist_ok=True)

    path = Path(os.path.dirname(os.path.abspath(args["-o"])))
    path.mkdir(parents=True, exist_ok=True)

    DataDescriber.describe(data, args.get("-e", None))
    DataDrawer.draw(data, args.get("-e", None), os.path.abspath(args.get("-d")))

    processed = DataProcessor.process(data, args.get("-e", None))
    DataSaver.save(processed, os.path.abspath(args.get("-o", None)), args.get("-so", ' '), (int(args.get("-h", None)) if args.get("-h", None) is not None else None))

    return 0

if __name__ == '__main__':
    sys.exit(main())