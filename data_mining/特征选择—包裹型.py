from sklearn.feature_selection import RFE
from sklearn.linear_model import  LinearRegression
from sklearn.datasets import load_boston
boston = load_boston()
X = boston['data']
y = boston['target']
names = boston['feature_names']
lr= LinearRegression()
rfe = RFE(lr,n_features_to_select=1)
rfe.fit(X,y)
print(rfe.ranking_)
# print(list(zip((map(lambda x:x,rfe.ranking_)),names)))
# print(names)
print(sorted(zip(map(lambda x:round(x,4),rfe.ranking_),names)))