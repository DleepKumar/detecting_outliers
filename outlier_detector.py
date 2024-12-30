import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
from Zscore import df

def removal_box_plot(data,column,thresold):
    sns.boxplot(data[column])
    plt.title(f"original box plot of {column}")
    plt.show()
    removed_outliers=data[data[column]<=thresold]
    sns.boxplot(removed_outliers[column])
    plt.title(f"without outliers box plot of {column}")
    plt.show()
    return removed_outliers

print(removal_box_plot(df,"bmi",0.12))    
    

