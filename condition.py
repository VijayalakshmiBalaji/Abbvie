from functions.utils.dtypes import InputData
from functions.utils import utils
from typing import Any

def condition(
        data: InputData, 
        column: str, 
        operation: str, 
        check_value: Any):
    """Perform check based on the condition
    :param data: dataset to work with
    :type data: InputData
    :param column: column within dataset to work with
    :type column: str
    :param operation: operation to use on column
    :type operation: str
    :param check_value: value to check for
    :type check_value: Any
    :return: List of boolean values based on column checked against value with operator
    :rtype: List(bool)
    :raises: ValueError: If parameter validation fails
    """

    # Perform check
    result = utils.condition(data[column], operation, check_value)

    return result
