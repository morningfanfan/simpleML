
class Util:
    """
    Utilities for checking data format
    static method: check_data_format -> check if the minimum component of data is a number
    static method: check_index_formax -> check if data is an int number, else raise an error 
    """
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
