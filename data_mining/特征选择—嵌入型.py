from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn.datasets import load_iris
iris = load_iris()
X,y = iris.data,iris.target
print(X)
lrSVC= LinearSVC(C=0.01,penalty='l1',dual=False).fit(X,y)
model= SelectFromModel(lrSVC,prefit=True)
x_new= model.transform(X)
print(x_new)
##l1正则化可以做变量选择，变量属于阶段性特征
##l2正则化是对变量的系数做压缩，它不能让变量系数变为0