#!/usr/bin/env python3

import datetime
from glob import glob
import os


def print_result(n, s):
    print(fr"<result{n:d}>{s}</result{n:d}>")


def main():
    time_format = "%Y-%m-%dT%H:%M:%S"
    data = []

    # use all csv files in ./data/
    csvs = sorted(glob(os.path.dirname(os.path.realpath(__file__))+'/data/????-??-??T??-??-??.csv'))
    csv = csvs[-1]
    with open(csv, "r") as f:
        line = f.readlines()[-1]
        items = line.strip().split(',')
        data.append(datetime.datetime.strptime(items[0], time_format))
        for i in range(1, 5):
            data.append(float(items[i]))

    print_result(1, data[0].strftime("%H:%M"))
    print_result(2, data[1])
    print_result(3, data[2])
    print_result(4, data[4])


if __name__ == "__main__":
    main()
