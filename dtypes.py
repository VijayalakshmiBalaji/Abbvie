import pandas as pd
from typing import Any, Dict, List, Union

# define data dict type
DataDict = Dict[str, List[Any]]

# input data type can be df or DataDict
InputData = Union[pd.DataFrame, DataDict]