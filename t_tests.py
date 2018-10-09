from scipy import stats
import pandas as pd
import numpy as np

data = pd.read_csv("blood_fresh_frozen.csv", index_col="Sample")

# print(data)
# data.info()

frozen_abs = data['Frozen_abs']

fresh_qubit_mean = np.mean(data['Fresh_qubit'])
frozen_qubit_mean = np.mean(data['Frozen_qubit'])
fresh_abs_mean = np.mean(data['Fresh_abs'])
frozen_abs_mean = np.mean(data['Frozen_abs'])

print("fresh qubit mean is: ", fresh_qubit_mean)
print("frozen qubit mean is: ", frozen_qubit_mean)
print("fresh absorbance mean is: ", fresh_abs_mean)
print("frozen absorbance mean is: ", fresh_abs_mean)

print("paired sample t-test for concentration: ", stats.ttest_rel(data['Fresh_qubit'], data['Frozen_qubit']))
print("paired sample t-test for absorbance: ", stats.ttest_rel(data['Fresh_abs'], data['Frozen_abs']))

