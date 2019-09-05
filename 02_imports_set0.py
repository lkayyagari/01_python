
import pandas as pd
import numpy as np


#visualization
import matplotlib.pylab as plt
get_ipython().magic('matplotlib inline')
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4
from mpl_toolkits.mplot3d import axes3d, Axes3D
import seaborn as sns


#pre-processing
from sklearn.model_selection import train_test_split


#modeling
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier  
from sklearn.ensemble import RandomForestClassifier
from xgboost.sklearn import XGBClassifier


#post-modeling
from sklearn import cross_validation, metrics   
from sklearn.grid_search import GridSearchCV

import datetime as datetime
import time

from sas7bdat import SAS7BDAT









