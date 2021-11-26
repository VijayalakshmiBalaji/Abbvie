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
    
    """ Performs nullcheck
    :param data: List of values (python list or np.ndarray) or value to search
    :type data: ComparisonData
    :param columnlist: List of columns within dataset
    :type columnlist: list
    """ 
    try:
        for i in range(len(columnlist)):
            if data[columnlist[i]].isnull().values().any():
                boollist.append(False)
            else:
                boollist.append(True)
            
        return boollist
    except:
        ValueError('Must be correct dtype')
        
        
def _compare_range(
        data: ComparisonData,
        min_value: Any = None,
        max_value: Any = None,
        dtype: str = 'str',
        date_format: str = None
        ):
    """Compares values within range (or below/above if only max/min supplied respectively)
    :param data: data to compare
    :type data: ComparisonData
    :param min_value: Minimum value for range comparison
    :type min_value: Any
    :param max_value: Maximum value for range comparison
    :type max_value: Any
    :param dtype: data type to be used for comparison, defaults to string
    :type dtype: str
    :param date_format: strftime format for date (optional)
    :type date_format: str
    :return: Truth series based on comparison
    :rtype: np.ndarray
    :raises: ValueError: Invalid arguments passed
    """

    has_min = has_max = True

    if _is_valid_dtype(dtype):
        data = _cast_series(data, dtype_dict[dtype], date_format)
        try:
            if min_value is None and max_value is None:
                raise ValueError("Minimum and/or Max must be passed to compare range")
            if min_value is not None:
                if isinstance(min_value, str):
                    min_value = dtype_dict[dtype](min_value)
                else:
                    min_value = _cast_series(min_value, dtype_dict[dtype], date_format)
            else:
                has_min = False
            if max_value is not None:
                if isinstance(max_value, str):
                    max_value = dtype_dict[dtype](max_value)
                else:
                    max_value = _cast_series(max_value, dtype_dict[dtype], date_format)
            else:
                has_max = False
                
        except:
            raise TypeError("check_value must be valid dtype")


        if has_min and has_max:
            return (data > min_value) & (data < max_value)
        elif has_min:
            return (data > min_value)
        else:
            return (data < max_value)
        
        
def uniqueness(data: ComparisonData,
        columnlist: list,
        dtype: str = None,
        date_format: str= None):
    """ Performs uniqueness check
    :param data: List of values (python list or np.ndarray) or value to search
    :type data: ComparisonData
    :param columnlist: List of columns within dataset
    :type columnlist: list
    """     
    boollist=[]
    try:
        for i in range(len(columnlist)):
            if data[columnlist[i]].is_unique==True:
                boollist.append(True)
            else:
                boollist.append(False)
            
        return boollist
    except:
        ValueError('Must be correct dtype')