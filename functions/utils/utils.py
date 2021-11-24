import numpy as np
import pandas as pd
import datetime as dt
from functions.utils.dtypes import *
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
                
def _cast_series(
    data: ComparisonData,
    dtype: type,
    date_format: str = None
        ):
    """ Casts series to data type when possible
    :param data: np.ndarray
    :type data: ComparisonData
    :param dtype: Data type to cast to
    :type dtype: type
    :param date_format: Optional, strftime date format
    :type date_format: str
    :return: converted data series
    :rtype: np.ndarray
    """
    if dtype != 'datetime' or date_format is None:
        return data.apply(lambda x: _cast_if(x, dtype))
    else:
        return pd.to_datetime(data, errors = 'coerce', format = date_format)


def _cast_if(
    data: Any,
    dtype: type
    ):
    """ Tries to cast value, otherwise returns value
    :param data: data to convert
    :type data: Any
    :param dtype: Data type to convert to
    :type dtype: type
    :return: Casted dtype if possible
    :rtype: $(dtype)
    """
    try:
        res = dtype(data)
    except TypeError as e:
        res = dtype_defaults[data]
    return res

def condition(
        data: ComparisonData,
        operation: str,
        check_value: Any,
        dtype: str = None,
        date_format: str = None
        ):
    """ Performs conditional check
    :param data: List of values (python list or np.ndarray) or value to check
    :type data: ComparisonData
    :param operation: Operation to perform: one of ['=','!=','>','>=','<','<=']
    :type operation: string
    :param check_value: Value to check for
    :type check_value: Any
    :param dtype: Optional, one of ['str','datetime','int','float']
    :type dtype: str
    :param date_format: Optional, standard strftime date format to use for casting to datetime var
    :type: date_format: str
    :return: list of bools that based on condition
    :rtype: np.ndarray
    :raises: ValueError: If invalid operator passed
    """
    
    if isinstance(data, list):
        data = np.array(data)

    if operation not in operator_dict:
        raise ValueError("Operation must be one of the following: '%s'" %("','".join(operator_dict.keys())))

    # if dtype is passed, try casting
    if dtype is not None and _is_valid_dtype(dtype):
        data = _cast_series(data, dtype_dict[dtype], date_format)
        try:
            dtype_dict[dtype](check_value)
        except:
            raise TypeError("check_value must be valid dtype")

        
    result = operator_dict[operation](data, check_value)

    return result

def checkbox(
        data: ComparisonData,
        operation: str,
        check_value: Any,
        dtype: str = None,
        date_format: str = None
        ):
    """ Performs checkbox check
    :param data: List of values (python list or np.ndarray) or value to check
    :type data: ComparisonData
    :param operation: Operation to perform: one of ['=','!=','>','>=','<','<=']
    :type operation: string
    :param check_value: Value to check for
    :type check_value: Any
    :param dtype: Optional, one of ['str','datetime','int','float']
    :type dtype: str
    :param date_format: Optional, standard strftime date format to use for casting to datetime var
    :type: date_format: str
    :return: list of bools that based on condition
    :rtype: np.ndarray
    :raises: ValueError: If invalid operator passed
    """
    if dtype is not None and _is_valid_dtype(dtype):
        data = _cast_series(data, dtype_dict[dtype], date_format)
        try:
            dtype_dict[dtype](check_value)
        except:
            raise TypeError("check_value must be valid dtype")

        
    result = operator_dict[operation](data, check_value)

    return result
        
def condition1(
        data: ComparisonData,
        operation: str,
        check_value: Any,
        dtype: str = None,
        date_format: str = None
        ):
    """ Performs conditional check
    :param data: List of values (python list or np.ndarray) or value to check
    :type data: ComparisonData
    :param operation: Operation to perform: one of ['=','!=','>','>=','<','<=']
    :type operation: string
    :param check_value: Value to check for
    :type check_value: Any
    :param dtype: Optional, one of ['str','datetime','int','float']
    :type dtype: str
    :param date_format: Optional, standard strftime date format to use for casting to datetime var
    :type: date_format: str
    :return: list of bools that based on condition
    :rtype: np.ndarray
    :raises: ValueError: If invalid operator passed
    """
    if dtype is not None and _is_valid_dtype(dtype):
        data = _cast_series(data, dtype_dict[dtype], date_format)
        try:
            dtype_dict[dtype](check_value)
        except:
            raise TypeError("check_value must be valid dtype")

        
    result = operator_dict[operation](data, check_value)

    return result

def nullcheck(data: ComparisonData,
        columnlist: list,
        dtype: str = None,
        date_format: str= None):
    
    boollist=[]
    """ Performs nullcheck
    :param data: List of values (python list or np.ndarray) or value to search
    :type data: ComparisonData
    :param columnlist: List of columns within dataset
    :type columnlist: list
    """ 
    try:
        for i in range(len(columnlist)):
            if data[columnlist[i]].isnull().values.any():
                boollist.append(False)
            else:
                boollist.append(True)
            
        return boollist
    except:
        ValueError('Must be correct dtype')