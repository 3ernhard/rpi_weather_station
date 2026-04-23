#!/usr/bin/env python3

import datetime
from glob import glob
import os


def print_result(n, s):
    print(fr"<result{n:d}>{s}</result{n:d}>")


def main():
    head = "time,t_outside,t_inside,pressure,humidity".split(',')
    unit = "%Y-%m-%dT%H:%M:%S,°C,°C,hPa,%".split(',')
    data = [[], [], [], [], []]

    # use all csv files in ./data/
    csvs = sorted(glob(os.path.dirname(os.path.realpath(__file__))+'/data/????-??-??T??-??-??.csv'))
    for csv in csvs:
        with open(csv, "r") as f:
            for line in f.readlines():
                if line.startswith('#'):
                    continue
                try:
                    items = line.strip().split(',')
                    data[0].append(datetime.datetime.strptime(items[0], unit[0]))
                    for i in range(1, 5):
                        data[i].append(float(items[i]))
                except ValueError:
                    print("=======================================")
                    print(f"Invalid data line in '{csv}' detected:")
                    print(f"{line}")
                    print("=======================================")

    print_result(1, data[0][-1].strftime("%H:%M"))
    print_result(2, data[1][-1])
    print_result(3, data[2][-1])
    print_result(4, data[4][-1])


if __name__ == "__main__":
    main()
