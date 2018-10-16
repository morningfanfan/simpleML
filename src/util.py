"""
Utilities for checking data format
"""


def check_data_format(data):
    if not isinstance(data, list):
        raise ValueError

    def check(data):
        for row in data:
            if isinstance(row, list):
                check(row)
            elif type(row) == int or type(row) == float:
                continue
            else:
                raise ValueError

    check(data)


def check_idx_format(idx):
    return int(idx)
