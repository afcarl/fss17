from sklearn import datasets

import numpy as np
from sklearn.mixture import GaussianMixture

from pdb import set_trace

iris = datasets.load_iris()
X = iris.data
y = iris.target

gmm = GaussianMixture(n_components=3)

gmm.fit(X)

print(gmm.weights_)
print(gmm.means_)
print(gmm.covariances_)
set_trace()

## prediction
pred = gmm.predict(X)
print(pred)
print(y)
set_trace()

## probability prediction
prob = gmm.predict_proba(X)

print(pred[0])
print(prob[0])
set_trace()