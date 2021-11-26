"""
Checks for specified unique values in single dataset
"""
from functions.utils.dtypes import InputData
from functions.utils import utils
from typing import Any

def uniqueness(data: InputData, columnlist: list=None, dtype: str=None):
    if type(columnlist)!=list:
        columnlist=columnlist.split(",")
        columnlist=list(columnlist)
    """ Performs uniqueness check
    :param data: List of values (python list or np.ndarray) or value to search
    :type data: ComparisonData
    :param columnlist: List of columns within dataset
    :type columnlist: list
    """ 
    # Perform check
    result = utils.uniqueness(data , columnlist , dtype)

    return result