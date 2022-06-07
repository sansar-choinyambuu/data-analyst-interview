#!/usr/bin/env python3

# TODO 1: complete the code so that it runs
# TODO 2: add type hints for read_csv method
# TODO 3: print only Swiss cities


def read_csv(path):
    return pd.read_csv(path)


cities = read_csv("cities.csv")
