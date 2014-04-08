# -*- coding:utf-8 -*-
from pylab import *
import numpy as np

if __name__ == "__main__":
    data = np.loadtxt("/home/hiro/Dropbox/univ/optimize/slides/A.mfcc")
    mean = np.mean(data,axis=0)
    X = data - mean
    covX = (X.T).dot(X)
    covX = covX/60
    eigenValues, eigenVectors = np.linalg.eig(covX)
    v1 = eigenVectors[:,0]
    v2 = eigenVectors[:,1]
    print v1
    print v2
    s = data.dot(v1)
    t = data.dot(v2)
    for i in range(len(s)):
        scatter(s[i],t[i])
        print s[i], t[i]
    xlabel("v1, eigen value = %f" % eigenValues[0])
    ylabel("v2, eigen value = %f" % eigenValues[1])
    title(u'PCA of A.mfcc')
    show()
