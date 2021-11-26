"""
Performs comparison within date range using datetime format
"""
from functions.utils.dtypes import InputData
from functions.utils import utils
from typing import Any

def date_range_search(
        data: InputData, 
        column: str, 
        min_date: str = None,
        max_date: str = None,
        min_date_col: str = None,
        max_date_col: str = None,
        date_format: str = None):
    """Perform comparison within one dataset with a single column; checks if date is within fixed range (min or max date). Can optionally pass only min/max to get truth series for dates greater/lower than passed date respectively
    :param data: dataset to work with
    :type data: InputData
    :param column: column within dataset to work with
    :type column: str
    :param min_date: minimum date to compare values to
    :type min_date: DateVar
    :param max_date: max date to compare values to
    :type max_date: DateVar
    :param min_date_col: Minimum date column to check
    :type min_date_col: str
    :param max_date_col: Maximum date column to check
    :type max_date_col: str
    :param date_format: Format of date in standard strftime
    :type date_format: str
    :return: List of boolean values based on column checked against value with operator
    :rtype: List(bool)
    :raises: ValueError: If parameter validation fails
    :raises: KeyError: If column(s) not found in data
    """

    if ((bool(min_date) or bool(max_date)) == (bool(min_date_col) or bool(max_date_col))) or not ((bool(min_date) or bool(max_date)) or (bool(min_date_col) or bool(max_date_col))):
        raise ValueError("One or two values must be passed for either pair: (min_date, max_date) or (min_date_col, max_date_col)")

    min_value = min_date if min_date is not None else data[min_date_col]
    max_value = max_date if max_date is not None else data[max_date_col]

    # Perform check
    result = utils._compare_range(data[column], min_value = min_value, max_value = max_value, dtype = 'datetime', date_format = date_format)

    return result