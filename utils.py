import numpy as np
import pandas as pd
import datetime as dt
from functions.utils.dtypes import InputData
from typing import Any
import operator as op

operator_dict = {
        '=' : op.eq,
        '!=' : op.ne,
        '>' : op.gt,
        '<' : op.lt,
        '>=' : op.ge,
        '<=' : op.le
        }

dtype_dict = {
        'str' : str,
        'datetime' : pd.to_datetime,
        'int' : int,
        'float' : float
        }

dtype_defaults = {
        'str' : '',
        'datetime' : pd.to_datetime('NaT'),
        'int' : np.nan,
        'float' : np.nan
        }

def _is_valid_dtype(dtype):
        if dtype not in dtype_dict:
                raise TypeError("Dtype must be one of the following: '%s'"%("','".join(dtype_dict.keys())))


def condition(
        data: InputData,
        operation: str,
        check_value: Any,
        dtype: str = None,
        ):
    """ Performs conditional check
    :param data: List of values (python list or np.ndarray) or value to check
    :type data: datetime or str
    :param operation: Operation to perform: one of ['=','!=','>','>=','<','<=']
    :type operation: string
    :param check_value: Value to check for
    :type check_value: Any
    :param dtype: Optional, one of ['str','datetime','int','float']
    :type dtype: str
    :return: list of bools that based on condition
    :rtype: np.ndarray
    :raises: ValueError: If invalid operator passed
    """
        
    result = operator_dict[operation](data, check_value)

    return result


        



