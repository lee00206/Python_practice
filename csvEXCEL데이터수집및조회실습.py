import sqldf
import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\문정과 멀티미디어실\\Desktop\\Data Preprocessing\\data\\doc_use_log.csv")\
     .sample(frac=0.01, replace=False)

#from pandasql import *

q="""
    SELECT \
        ext, \
        count(ext) as count, \
        count(distinct sessionid) as unq_sess \
    FROM df \
    GROUP BY ext \
    ORDER BY count DESC \
    """

print(sqldf(q, locals()).to_string())
