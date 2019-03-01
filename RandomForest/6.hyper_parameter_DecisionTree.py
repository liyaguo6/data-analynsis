#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import classification_report

def iris_type(s):
    it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return it[s]


# 花萼长度、花萼宽度，花瓣长度，花瓣宽度
# iris_feature = 'sepal length', 'sepal width', 'petal length', 'petal width'
iris_feature = u'花萼长度', u'花萼宽度', u'花瓣长度', u'花瓣宽度'

if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    path = './iris.data'  # 数据文件路径
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    x, y = np.split(data, (4,), axis=1)
    # 为了可视化，仅使用前两列特征
    x = x[:, :2]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
    # ss = StandardScaler()
    # ss = ss.fit(x_train)

    # 或用管道构建模型框架

    # 测试数据

    # 最优超参数组合列表
    # cv_split = ShuffleSplit(n_splits=5, train_size=0.7, test_size=0.25)
    pip_count = Pipeline(
        [('ss', StandardScaler()),  # 数据标准化过程
        ('DTC', DecisionTreeClassifier())])
    params = {'DTC__max_depth': [2, 3, 4, 5],
              'DTC__criterion': ['gini', 'entropy']
              }
    model = GridSearchCV(pip_count ,
                         params,
                         refit=True,
                         return_train_score=True,  # 后续版本需要指定True才有score方法
                         cv=4)
    model = model.fit(x_train, y_train)

    print('#######best_estimator_#######\n', model.best_estimator_)  #查看表格搜索最优参数
    print('best_socre_:',model.best_score_)
    print('best_params_:', model.best_params_)



    best_model = model.best_estimator_
    predict_y = best_model.predict(x_test)
    print("#######classification_report########\n",classification_report(y_test, predict_y))

    print("best_score：",best_model.score(x_test,y_test))


