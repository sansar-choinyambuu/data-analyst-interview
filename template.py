#!/usr/bin/env python3

# TODO 1: complete the code so that it runs
# TODO 2: add type hints for read_csv method
# TODO 3: export only Swiss cities as parquet file


def read_csv(path):
    return pd.read_csv(path)


cities = read_csv("cities.csv")
