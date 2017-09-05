from sklearn import datasets

import numpy as np
from sklearn.decomposition import PCA

from pdb import set_trace

iris = datasets.load_iris()
X = iris.data
y = iris.target

pca = PCA(n_components=2)

pca.fit(X)

print(pca.explained_variance_ratio_)
print(pca.get_covariance())
set_trace()

## transform
xx = pca.transform(X)
xxx = (X-pca.mean_).dot(pca.components_.transpose())
print(X[0])
print(xx[0])
print(xxx[0])
set_trace()

## inverse

print(pca.inverse_transform(xx[0]))
set_trace()