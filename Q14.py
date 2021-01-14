'''
14: Load the iris dataset, https://gist.github.com/netj/8836201, using pd.read_csv(). The four columns of the returned array correspond to
sepal length (cm)
sepal width (cm)
petal length (cm)
petal width (cm)
	Part 1. What is the Pearson correlation between the variables sepal length and petal length. Compute this using the scipy.stats.pearsonr function. It returns a 	tuple whose first element is the correlation. Write a function lengths that loads the data and returns the correlation.

	Part 2. What are the correlations between all the variables. Write a function correlations that returns an array of shape (4,4) containing the correlations. Use 	the function np.corrcoef. Which pair of variables is the most highly correlated?

	Note the input formats of both functions pearsonr and corrcoef.

'''

import pandas as pd
from scipy import stats
import numpy as np

# Loading Data & Correlations
# data_source = 'https://raw.githubusercontent.com/JunaidMB/python_competition/master/questions/iris.csv'
data_source = 'https://raw.githubusercontent.com/JunaidMB/python_competition/master/questions/iris.csv'
df = pd.read_csv(data_source, names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'], header=0)

# function returning correlation between sepal and petal length
def lengths():
    a = df['sepal length']
    b = df['petal length']
    result = stats.pearsonr(a, b)
    return result

# function returning correlation between all values
def correlations():
    #finds the correlation b/w the columns and then converts to numpy array
    n_arr = df.corr().to_numpy() 
    # finds the correlation coeff
    corcef = np.corrcoef(n_arr) 
    all_cor = pd.DataFrame(corcef, index=['sepal.length','sepal.width','petal.length','petal.width'], columns=['sepal.length','sepal.width','petal.length','petal.width']) #converts back to dataframe to show matrix of the corrcoeff
    return all_cor

print(correlations())

'''

Joke of the Question:

Parent: If all your friends jumped off a bridge, would you follow them? Machine Learning Algorithm: yes.

'''