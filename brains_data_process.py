import pandas as pd
brainFile = './data/brainsize.txt'
brainFrame = pd.read_csv(brainFile)
print(brainFrame.head())
print(brainFrame.describe())

import numpy as np
import matplotlib.pyplot as plt

menDf = brainFrame[(brainFrame.Gender == 'Male')]
womenDf = brainFrame[(brainFrame.Gender == 'Female')]
menMeanSmarts = menDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(menMeanSmarts, menDf["MRI_Count"])
plt.show()

brainFrame.corr(method='pearson')
womenDf.corr(method='pearson')
menDf.corr(method='pearson')

import seaborn as sns
wcorr = womenDf.corr()
sns.heatmap(wcorr)
plt.savefig('attribute_correlations_women.png', tight_layout=True)

mcorr = menDf.corr()
sns.heatmap(mcorr)
plt.savefig('attribute_correlations_man.png', tight_layout=True)