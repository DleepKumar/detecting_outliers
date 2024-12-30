import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn 
from sklearn.datasets import load_diabetes
import seaborn as snn
diabetic_data=load_diabetes()
df=pd.DataFrame(diabetic_data.data,columns=diabetic_data.feature_names)


