#!/usr/bin/env python3

import datetime
from sys import argv
from glob import glob
import os

import numpy as np


def main():
    time_format = "%Y-%m-%dT%H:%M:%S"
    data = [[], [], [], [], []]
    # data[i], i =
    # 0 : time
    # 1 : temperature(outside)
    # 2 : temperature(inside)
    # 3 : pressure(inside)
    # 4 : humidity(inside)

    # Plot all csv files in ./data/ if no argument is passed, else plot the passed csv file.
    csvs = argv[1:] if len(argv) > 1 else sorted(glob(os.path.dirname(os.path.realpath(__file__))+'/data/????-??-??T??-??-??.csv'))
    for csv in csvs:
        with open(csv, "r") as f:
            for line in f.readlines():
                if line.startswith('#'):
                    continue
                try:
                    items = line.strip().split(',')
                    data[0].append(datetime.datetime.strptime(items[0], time_format))
                    for i in range(1, 5):
                        data[i].append(float(items[i]))
                except ValueError:
                    print("=======================================")
                    print(f"Invalid data line in '{csv}' detected:")
                    print(f"{line}")
                    print("=======================================")

    by_years = {}
    for i in range(len(data[0])):
        year = data[0][i].year
        if year not in by_years:
            by_years[year] = []
        by_years[year].append(data[1][i])

    for year in by_years:
        avg = np.median(by_years[year])
        print(f"{year}: {avg:5.2f}°C")


if __name__ == "__main__":
    main()
