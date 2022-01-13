import traceback
import pandas as pd
import operator as op
from dateutil.relativedelta import relativedelta


def not_null_chk(data):
    flag = False
    ls = ['null', 'Null', 'NULL', 'NaN', '', ' ', 'None', 'NaT', 'np.nan']
    if data not in ls:
        flag = True
    else:
        flag = False
    return flag

def null_chk(data):
    flag = False
    ls = ['NaT', 'null', 'Null', 'NULL', 'NaN', '', ' ', 'None', 'np.nan']
    if data in ls:
        flag = True
    else:
        flag = False
    return flag

def grade_chk(check_var, check_val: list):
    try:
        flag = False
        grade = check_val
        if (check_var) not in grade:
            flag = True
        else:
            flag = False
        return flag
    except:
        print(traceback.format_exc())
        return None

def relative_date_compare(d1, d2, oper):
    flag = False
    if oper == '==':
        try:
            if d1 == d2:
                flag = True
            else:
                flag = False
            return flag
        except:
            print(traceback.format_exc())
            return None
    elif oper == '!=':
        try:
            if d1 != d2:
                flag = True
            else:
                flag = False
            return flag
        except:
            print(traceback.format_exc())
            return None
    elif oper == '>':
        try:
            if d1 > d2:
                flag = True
            else:
                flag = False
            return flag
        except:
            print(traceback.format_exc())
            return None
    elif oper == '<':
        try:
            if d1 < d2:
                flag = True
            else:
                flag = False
            return flag
        except:
            print(traceback.format_exc())
            return None

def simple_date_compare(df1, col1, df2, oper):
    flag = False
    if oper == '==':
        try:
            for i in range(df1.shape[0]):
                df1_rec = df1.iloc[[i]]
                if [df1_rec[col1].values[0] == df2]:
                    flag = True
                    return flag, df1_rec
                else:
                    flag = False
                    return flag
        except:
            print(traceback.format_exc())
            return None
    elif oper == '!=':
        try:
            for i in range(df1.shape[0]):
                df1_rec = df1.iloc[[i]]
                if [df1_rec[col1].values[0] != df2]:
                    flag = True
                    return flag, df1_rec
                else:
                    flag = False
                    return flag
        except:
            print(traceback.format_exc())
            return None
    elif oper == '>':
        try:
            for i in range(df1.shape[0]):
                df1_rec = df1.iloc[[i]]
                if [df1_rec[col1].values[0] > df2]:
                    flag = True
                    return flag, df1_rec
                else:
                    flag = False
                    return flag
        except:
            print(traceback.format_exc())
            return None
    elif oper == '<':
        try:
            for i in range(df1.shape[0]):
                df1_rec = df1.iloc[[i]]
                if [df1_rec[col1].values[0] < df2]:
                    flag = True
                    return flag, df1_rec
                else:
                    flag = False
                    return flag
        except:
            print(traceback.format_exc())
            return None


def val_check(check_var, check_val):
    try:
        flag = False
        if check_var == check_val:
            flag = True
        else:
            flag = False
        return flag
    except:
        print(traceback.format_exc())
        return None

def duplicates(df,col):
    try:
        flag = False
        if df.duplicated([col]).any():
            flag = True
        else:
            flag = False
        return flag
    except:
        print(traceback.format_exc())
        return None  

def val_compare(df1, col1, df2, oper):
    flag = False
    if oper == '==':
        try:
            for i in range(df1.shape[0]):
                df1_rec  = df1.iloc[[i]]
                if [df1_rec[col1].values[0] == df2]:
                    flag = True
                    return flag, df1_rec
                else:
                    flag = False
                    return flag
        except:
            print(traceback.format_exc())
            return None
                
    elif oper == '!=':
        try:
            for i in range(df1.shape[0]):
                df1_rec = df1.iloc[[i]]
                if [df1_rec[col1].values[0] != df2]:
                    flag = True
                    return flag, df1_rec
                else:
                    flag = False
                    return flag
        except:
            print(traceback.format_exc())
            return None
    elif oper == '>':
        try:
            for i in range(df1.shape[0]):
                df1_rec = df1.iloc[[i]]
                if [df1_rec[col1].values[0] > df2]:
                    flag = True
                    return flag, df1_rec
                else:
                    flag = False
                    return flag
        except:
            print(traceback.format_exc())
            return None
    elif oper == '<':
        try:
            for i in range(df1.shape[0]):
                df1_rec = df1.iloc[[i]]
                if [df1_rec[col1].values[0] < df2]:
                    flag = True
                    return flag, df1_rec
                else:
                    flag = False
                    return flag
        except:
            print(traceback.format_exc())
            return None
 

