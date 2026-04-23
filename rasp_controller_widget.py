#!/usr/bin/env python3

import datetime
from glob import glob
import os


def head_line(head, line, rm_chrs=["#", " ", "\n"], sep=","):
    if head != []:
        return
    for rm_chr in rm_chrs:
        line = line.replace(rm_chr, "")
    head = line.split(sep)
    return head


def unit_line(unit, line, rm_chrs=["#", " ", "\n"], sep=","):
    if unit != []:
        return
    for rm_chr in rm_chrs:
        line = line.replace(rm_chr, "")
    unit = line.split(sep)
    return unit


def data_line(data, unit, line, rm_chrs=[" ", "\n"], sep=",", comment="#"):
    if len(line) == 0 or line[0] == comment:
        return
    for rm_chr in rm_chrs:
        line = line.replace(rm_chr, "")
    sep_line = line.split(sep)
    data[0].append(datetime.datetime.strptime(sep_line[0], unit[0]))
    for i in range(1, len(data)):
        data[i].append(float(sep_line[i]))
    return data


def print_result(n, s):
    print(fr"<result{n:d}>{s}</result{n:d}>")


def main():
    head = []
    unit = []
    data = [[], [], [], [], []]

    # use all csv files in ./data/
    csvs = sorted(glob(os.path.dirname(os.path.realpath(__file__))+'/data/????-??-??T??-??-??.csv'))
    for csv in csvs:
        with open(csv, "r") as f:
            head = head_line(head, f.readline())
            unit = unit_line(unit, f.readline())
            for line in f.readlines():
                try:
                    data = data_line(data, unit, line)
                except ValueError:
                    print(f"Invalid data line in '{csv}' detected.")
                    continue

    print_result(1, data[0][-1].strftime("%H:%M"))
    print_result(2, data[1][-1])
    print_result(3, data[2][-1])
    print_result(4, data[4][-1])


if __name__ == "__main__":
    main()
