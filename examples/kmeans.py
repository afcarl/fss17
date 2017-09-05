from sklearn import datasets

import numpy as np
from sklearn.cluster import KMeans

from pdb import set_trace

iris = datasets.load_iris()
X = iris.data
y = iris.target


## clustering by Kmeans
cluster = KMeans(n_clusters=3)
cluster.fit(X)

y_predict = cluster.predict(X)

print y
print y_predict

set_trace()


## what does transform mean?
X_trans = cluster.transform(X)

c = cluster.cluster_centers_

dis1 = np.linalg.norm(c[0]-X[0])
dis2 = X_trans[0,0]

print dis1
print dis2
set_trace()
## How is inertia calculated?
inertia = sum([min(x_trans)**2 for x_trans in X_trans])

print cluster.inertia_
print inertia
set_trace()

