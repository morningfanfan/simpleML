"""
Utilities for checking data format
"""


class Util:
    @staticmethod
    def check_data_format(data):
        if not isinstance(data, list):
            raise ValueError

        def check(data):
            for row in data:
                if isinstance(row, list):
                    check(row)
                elif type(row) == int or type(row) == float:
                    continue  # data should be numbers
                else:
                    raise ValueError

        check(data)  # demension of data is uncertain

    @staticmethod
    def check_idx_format(idx):
        return int(idx)
