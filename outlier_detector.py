import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as snn
from Zscore import df

def outlier(data=df,column=None):
    q1,q3 =np.percentile(data[column],[25,75])
    iqr=q3-q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    without_outliers=data[(data[column] > lower_bound) | (data[column] < upper_bound)]
    outliers=data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    snn.boxplot(without_outliers)
    plt.show()
    return outliers
    
print(outlier(df,"bmi"))    
    

