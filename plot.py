#!/usr/bin/env python3

import datetime
from sys import argv
from glob import glob
import os

import numpy as np
from matplotlib import pyplot as plt


def main():
    time_format = "%Y-%m-%dT%H:%M:%S"
    data = [[], [], [], [], []]

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

    # data[i], i =
    # 0 : time
    # 1 : temperature(outside)
    # 2 : temperature(inside)
    # 3 : pressure(inside)
    # 4 : humidity(inside)
    t_delta = datetime.datetime.now()-data[0][-1]
    t_d = t_delta.days
    t_h, rem = divmod(t_delta.seconds, 3600)
    t_m, t_s = divmod(rem, 60)
    print('Last measurement was ', end='')
    if t_d != 0:
        print(f'{t_d:d} days ', end='')
    if t_h != 0:
        print(f'{t_h:d} hours ', end='')
    if t_m != 0:
        print(f'{t_m:d} minutes ', end='')
    print(f'{t_s:d} seconds ', end='')
    print('ago.')

    mean_in_temp = np.mean(data[2])
    mean_out_temp = np.mean(data[1])

    # 1 = no humidity, 0 = humidity
    if 0:
        plt.title(data[0][-1].strftime("%d. %b, %H:%M"))
        plt.ylabel('°C')
        plt.xlim((data[0][0], data[0][-1]))
        plt.plot(data[0], data[2], color='tab:blue', label=f'inside:  {data[2][-1]:.1f} <{mean_in_temp:.1f}> °C')
        plt.plot(data[0], data[1], color='tab:red', label=f'outside: {data[1][-1]:.1f} <{mean_out_temp:.1f}> °C')
        ax1.axhline(18, color='black', linewidth=0.5)
        ax1.axhline(24, color='black', linewidth=0.5)
        plt.tick_params(axis="x", rotation=45)
        plt.legend()

    else:
        mean_in_hum = np.mean(data[4])
        fig, (ax1, ax2) = plt.subplots(2)

        ax1.set(title=data[0][-1].strftime("%d. %b, %H:%M"))
        ax1.set(ylabel='°C')
        ax1.set(xlim=(data[0][0], data[0][-1]))
        ax1.plot(data[0], data[2], color='tab:blue', label=f'inside:  {data[2][-1]:.1f} <{mean_in_temp:.1f}> °C')
        ax1.plot(data[0], data[1], color='tab:red', label=f'outside: {data[1][-1]:.1f} <{mean_out_temp:.1f}> °C')
        ax1.axhline(18, color='black', linewidth=0.5)
        ax1.axhline(24, color='black', linewidth=0.5)
        ax1.tick_params(axis="x", rotation=45)
        ax1.legend()

        ax2.set(ylabel='%')
        ax2.set(xlim=(data[0][0], data[0][-1]))
        ax2.plot(data[0], data[4], color='tab:blue', label=f'inside: {data[4][-1]:.1f} <{mean_in_hum:.1f}> %')
        ax2.axhline(40, color='black', linewidth=0.5)
        ax2.axhline(60, color='black', linewidth=0.5)
        ax2.tick_params(axis="x", rotation=45)
        ax2.legend()

    plt.show()


if __name__ == "__main__":
    main()
